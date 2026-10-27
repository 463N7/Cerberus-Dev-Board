"""Check generated pages, internal targets, and the publication's CAD boundary."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            self.ids.add(values["id"])
        for attr in ("href", "src"):
            if attr in values:
                self.links.append(values[attr])


def main():
    errors = []
    files = list(DOCS.glob("*.html"))
    parsed = {}
    for file in files:
        parser = Links()
        parser.feed(file.read_text(encoding="utf-8"))
        parsed[file.resolve()] = parser
    for file, parser in parsed.items():
        for link in parser.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            if url.path == "/Cerberus-Dev-Board/":
                target = DOCS / "index.html"
            else:
                target = (file.parent / unquote(url.path)).resolve() if url.path else file
            if not target.is_relative_to(DOCS.resolve()):
                errors.append(f"Site link leaves docs/: {file.name} -> {link}")
            elif not target.is_file():
                errors.append(f"Missing target: {file.name} -> {link}")
            elif url.fragment and target in parsed and unquote(url.fragment) not in parsed[target].ids:
                errors.append(f"Missing anchor: {file.name} -> {link}")
    banned = {".kicad_sch", ".sch", ".net", ".dsn", ".brd", ".gbr", ".gerber"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.relative_to(ROOT).parts:
            continue
        if path.suffix.lower() in banned:
            errors.append(f"Excluded design file: {path.relative_to(ROOT)}")
        if path.suffix.lower() in {".kicad_pcb", ".kicad_pro", ".kicad_mod", ".kicad_sym"}:
            if not path.is_relative_to(ROOT / "hardware" / "expansion"):
                errors.append(f"CAD outside expansion area: {path.relative_to(ROOT)}")
    if len(files) != 12:
        errors.append(f"Expected 11 reference pages + 404; found {len(files)}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked {len(files)} pages: local links/anchors valid; no excluded design files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
