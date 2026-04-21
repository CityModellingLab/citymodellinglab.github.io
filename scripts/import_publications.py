#!/usr/bin/env python3
"""Import BibTeX entries into Hugo publication page bundles.

This intentionally implements only the small BibTeX surface the site needs:
entries with key/value fields, nested braces, quoted strings, and standard
`and`-separated authors. It avoids the old external Academic converter so the
GitHub Action stays predictable.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path


TYPE_MAP = {
    "article": "article-journal",
    "inproceedings": "paper-conference",
    "conference": "paper-conference",
    "proceedings": "paper-conference",
    "unpublished": "manuscript",
    "misc": "manuscript",
    "preprint": "manuscript",
}


def strip_wrapping(value: str) -> str:
    value = value.strip().rstrip(",").strip()
    if len(value) >= 2 and value[0] == "{" and value[-1] == "}":
        value = value[1:-1]
    elif len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        value = value[1:-1]
    return value.strip()


def clean_tex(value: str) -> str:
    value = strip_wrapping(value)
    value = re.sub(r"[{}]", "", value)
    replacements = {
        r"\&": "&",
        r"\'": "",
        r"\`": "",
        r'\"': "",
        r"\~": "",
    }
    for src, dst in replacements.items():
        value = value.replace(src, dst)
    return re.sub(r"\s+", " ", value).strip()


def split_entries(text: str) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    i = 0
    while True:
        start = text.find("@", i)
        if start == -1:
            break
        brace = text.find("{", start)
        if brace == -1:
            break
        entry_type = text[start + 1 : brace].strip().lower()
        depth = 0
        end = brace
        for end in range(brace, len(text)):
            char = text[end]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    break
        if depth != 0:
            raise ValueError(f"Unclosed BibTeX entry starting at byte {start}")
        body = text[brace + 1 : end]
        key, _, fields = body.partition(",")
        if key.strip():
            entries.append((entry_type, key.strip(), fields.strip()))
        i = end + 1
    return entries


def split_fields(fields_text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    i = 0
    while i < len(fields_text):
        while i < len(fields_text) and fields_text[i] in " \t\r\n,":
            i += 1
        name_start = i
        while i < len(fields_text) and re.match(r"[A-Za-z0-9_-]", fields_text[i]):
            i += 1
        name = fields_text[name_start:i].strip().lower()
        while i < len(fields_text) and fields_text[i].isspace():
            i += 1
        if not name or i >= len(fields_text) or fields_text[i] != "=":
            break
        i += 1
        while i < len(fields_text) and fields_text[i].isspace():
            i += 1
        value_start = i
        if i < len(fields_text) and fields_text[i] in '{"':
            opener = fields_text[i]
            closer = "}" if opener == "{" else '"'
            depth = 0
            i += 1
            while i < len(fields_text):
                char = fields_text[i]
                if opener == "{" and char == "{":
                    depth += 1
                elif opener == "{" and char == "}":
                    if depth == 0:
                        i += 1
                        break
                    depth -= 1
                elif opener == '"' and char == closer and fields_text[i - 1] != "\\":
                    i += 1
                    break
                i += 1
        else:
            while i < len(fields_text) and fields_text[i] != ",":
                i += 1
        fields[name] = fields_text[value_start:i].strip()
    return fields


def format_author(name: str) -> str:
    name = clean_tex(name)
    if "," in name:
        last, first = [part.strip() for part in name.split(",", 1)]
        return f"{first} {last}".strip()
    return name


def split_authors(value: str) -> list[str]:
    return [format_author(part) for part in re.split(r"\s+and\s+", strip_wrapping(value)) if part.strip()]


def slugify(title: str, year: str, authors: list[str]) -> str:
    words = re.findall(r"[a-z0-9]+", title.lower())
    while words and words[0] in {"a", "an", "the"}:
        words.pop(0)
    prefix = ""
    if authors:
        prefix = re.sub(r"[^a-z0-9]+", "-", authors[0].split()[-1].lower()).strip("-")
    base_words = words[:5]
    base = "-".join([part for part in [prefix, *base_words] if part]).strip("-") or "publication"
    if year:
        base = f"{base}-{year}"
    return base


def bib_key(text: str) -> str:
    entries = split_entries(text)
    return entries[0][1] if entries else ""


def existing_bundles(output_dir: Path) -> dict[str, Path]:
    bundles: dict[str, Path] = {}
    if not output_dir.exists():
        return bundles
    for cite in output_dir.glob("*/cite.bib"):
        try:
            key = bib_key(cite.read_text(encoding="utf-8"))
        except Exception:
            continue
        if key:
            bundles[key] = cite.parent
    return bundles


def yaml_quote(value: str) -> str:
    value = value.replace("\\", "\\\\").replace("'", "''")
    return f"'{value}'"


def yaml_list(name: str, values: list[str]) -> list[str]:
    if not values:
        return []
    lines = [f"{name}:"]
    lines.extend(f"- {item}" for item in values)
    return lines


def publication_venue(entry_type: str, fields: dict[str, str]) -> str:
    venue = (
        fields.get("journal")
        or fields.get("journaltitle")
        or fields.get("booktitle")
        or fields.get("publisher")
        or fields.get("organization")
        or ""
    )
    venue = clean_tex(venue)
    return f"*{venue}*" if venue else ""


def render_index(entry_type: str, fields: dict[str, str]) -> str:
    title = clean_tex(fields.get("title", "Untitled publication"))
    authors = split_authors(fields.get("author", ""))
    year = clean_tex(fields.get("year", ""))
    date = clean_tex(fields.get("date", ""))
    if not date:
        date = f"{year}-01-01" if year else datetime.utcnow().date().isoformat()
    publish_date = f"{date}T00:00:00Z" if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date) else date
    pub_type = TYPE_MAP.get(entry_type, "manuscript")
    venue = publication_venue(entry_type, fields)
    abstract = clean_tex(fields.get("abstract", ""))
    doi = clean_tex(fields.get("doi", ""))
    tags = [clean_tex(tag) for tag in re.split(r"\s*,\s*", strip_wrapping(fields.get("keywords", ""))) if tag.strip()]

    lines = [
        "---",
        f"title: {yaml_quote(title)}",
    ]
    lines.extend(yaml_list("authors", authors))
    lines.extend(
        [
            f"date: {yaml_quote(date)}",
            f"publishDate: {yaml_quote(publish_date)}",
            "publication_types:",
            f"- {pub_type}",
        ]
    )
    if venue:
        lines.append(f"publication: {yaml_quote(venue)}")
    if doi:
        lines.append(f"doi: {doi}")
    if abstract:
        lines.append(f"abstract: {yaml_quote(abstract)}")
    lines.extend(yaml_list("tags", tags))
    lines.extend(["---", ""])
    return "\n".join(lines)


def import_publications(bib_path: Path, output_dir: Path) -> int:
    text = bib_path.read_text(encoding="utf-8").strip()
    if not text:
        print(f"{bib_path} is empty; no publications imported.")
        return 0

    entries = split_entries(text)
    if not entries:
        print(f"{bib_path} contains no BibTeX entries; no publications imported.")
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    known_bundles = existing_bundles(output_dir)
    for entry_type, key, fields_text in entries:
        fields = split_fields(fields_text)
        title = clean_tex(fields.get("title", key))
        year = clean_tex(fields.get("year", ""))
        authors = split_authors(fields.get("author", ""))
        bundle = known_bundles.get(key)
        if bundle is None:
            bundle = output_dir / slugify(title, year, authors)
        bundle.mkdir(parents=True, exist_ok=True)
        raw_entry = f"@{entry_type}{{{key},\n{fields_text}\n}}\n"
        (bundle / "cite.bib").write_text(raw_entry, encoding="utf-8")
        (bundle / "index.md").write_text(render_index(entry_type, fields), encoding="utf-8")
        print(f"Imported {bundle.name}")
    return len(entries)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("bib", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    count = import_publications(args.bib, args.output)
    print(f"Imported {count} publication(s).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Publication import failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
