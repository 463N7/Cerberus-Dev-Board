"""Build the GitHub Pages site from the repository's Markdown sources."""
from pathlib import Path
import csv
import html
import json
import re
from html.parser import HTMLParser

import markdown

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    ("index", "Overview", "A developer reference for the Cerberus handheld."),
    ("getting-started", "Start here", "Identify, install, build, and recover your Cerberus."),
    ("hardware", "Hardware", "Processors, memory, built-in features, and electrical constraints."),
    ("pinouts", "Pinouts", "Base-board GPIOs, labeled expansion breakout connections, and the six-C5 add-on pinout."),
    ("expansion", "Expansion add-ons", "Six-C5 and RF/NFC add-ons, both in testing, plus expansion KiCad files."),
    ("programming", "Programming", "Toolchain, memory settings, drivers, protocol, and bring-up."),
    ("batteries", "Batteries", "Tested batteries and should-fit candidates, with evidence."),
    ("antennas", "Antennas", "Radio-specific antenna compatibility and test records."),
    ("troubleshooting", "Troubleshooting", "Recover USB and diagnose the built-in interfaces."),
    ("downloads", "Downloads", "Firmware links, pin definitions, examples, and expansion files."),
    ("revisions", "Reference + testing", "Base-board reference, add-on testing status, and documentation history."),
]


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def local_markdown_links(body):
    def replace(match):
        url = match.group(1)
        if ":" not in url and not url.startswith("//"):
            url = re.sub(r"\.md(?=#|$)", ".html", url)
        return 'href="' + url + '"'
    return re.sub(r'href="([^"]+)"', replace, body)


def export_addon_pinouts(assets, heading, filename):
    """Keep downloadable add-on tables in sync with the Pinouts page source."""
    source = (ROOT / "content" / "pinouts.md").read_text(encoding="utf-8")
    match = re.search(r"^## " + re.escape(heading) + r"\n(.*?)(?=^## |\Z)", source, re.M | re.S)
    if match is None:
        raise ValueError(f"Missing add-on pinout section: {heading}")
    rows, section, headers = [], "", []
    for line in match.group(1).splitlines():
        if line.startswith("### "):
            section, headers = line[4:], []
        elif line.startswith("|"):
            cells = [cell.strip().replace("`", "").replace("**", "") for cell in line.strip("|").split("|")]
            if all(re.fullmatch(r":?-+:?", cell.replace(" ", "")) for cell in cells):
                continue
            if not headers:
                headers = cells
                continue
            if headers[0] == "Device":
                device, signal, connection, notes = cells
            elif headers[0] == "Device / connection":
                device, signal, connection, notes = cells[0], "Supply / setup", "", cells[1]
            else:
                device = "Expansion C5" if headers[1] == "Expansion C5 GPIO" else "Shared bus / S3"
                signal, connection, notes = cells
                if device == "Expansion C5":
                    notes = "S3 connection: " + notes
            rows.append([section, device, signal, connection, notes, "In testing"])
        else:
            headers = []
    with (assets / filename).open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(["section", "device", "signal", "connection", "notes", "status"])
        writer.writerows(rows)


def export_breakout_pinouts(assets):
    """Export individual breakout GPIO signals from their documentation table."""
    source = (ROOT / "content" / "pinouts.md").read_text(encoding="utf-8")
    section = source.split("## Expansion breakout connections\n", 1)[1].split("\n## ", 1)[0]
    rows = []
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells[0] not in ("ESP32-C5", "ESP32-S3"):
            continue
        processor, gpio, label, side = cells
        rows.append([processor, gpio, label, side, "Labeled face; top to bottom on each side"])
    if len(rows) != 25:
        raise ValueError(f"Expected 25 breakout GPIO signals, found {len(rows)}")
    with (assets / "expansion-breakout-pinout.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(["processor", "gpio", "printed_label", "side", "view"])
        writer.writerows(rows)


def build():
    output = ROOT / "docs"
    assets = output / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    for name in ("style.css", "site.js", "mark.svg", "cerberus-logo.svg", "expansion-breakout.jpg", "tested-batteries.jpg"):
        (assets / name).write_bytes((ROOT / "site" / name).read_bytes())
    (output / ".nojekyll").write_text("", encoding="utf-8")
    index = []
    for slug, title, description in PAGES:
        source = (ROOT / "content" / f"{slug}.md").read_text(encoding="utf-8")
        converter = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list"])
        body = local_markdown_links(converter.convert(source))
        body = re.sub(r"(<table>.*?</table>)", r'<div class="table-scroll">\1</div>', body, flags=re.S)
        plain = PlainText()
        plain.feed(body)
        index.append({"title": title, "url": f"{slug}.html", "text": " ".join(plain.parts)})
        links = []
        for number, (key, label, _) in enumerate(PAGES):
            current = ' aria-current="page"' if key == slug else ''
            links.append(f'<a href="{key}.html"{current}><span>{number:02}</span>{html.escape(label)}</a>')
        navigation = "".join(links)
        # Metadata and all asset URLs stay relative so the project Pages subpath works.
        page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | Cerberus Dev Board</title><meta name="description" content="{html.escape(description, quote=True)}">
<meta name="theme-color" content="#101817"><link rel="icon" href="assets/cerberus-logo.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/style.css"><script src="assets/site.js" defer></script></head>
<body class="{'home' if slug == 'index' else 'reference'}"><a class="skip" href="#main">Skip to content</a>
<header class="topbar"><a class="brand" href="index.html"><img src="assets/mark.svg" alt="" width="34" height="34"><span>CERBERUS<small>DEV BOARD</small></span></a><span class="top-label">HARDWARE / SOFTWARE / EXPANSION</span><a class="github" href="https://github.com/463N7/Cerberus-Dev-Board">GitHub <span aria-hidden="true">↗</span></a><button class="menu-button" type="button" aria-controls="sidebar" aria-expanded="false">Menu</button></header>
<aside id="sidebar" class="sidebar"><p class="nav-heading">DEVELOPER REFERENCE</p><nav aria-label="Documentation">{navigation}</nav><div class="sidebar-note"><span class="status-dot"></span>Cerberus base board<p>One onboard C5<br>Quad PSRAM · 1-bit SDMMC<br>40 MHz SDMMC target</p></div><a class="installer-link" href="https://463n7.github.io/Cerberus-Flasher/">Open USB installer ↗</a></aside>
<div class="workspace"><div class="utility"><span>REFERENCE / {html.escape(title.upper())}</span><div class="search-wrap"><label class="sr-only" for="site-search">Search all documentation</label><input id="site-search" type="search" autocomplete="off" placeholder="Search documentation…"><div id="search-results" class="search-results" hidden aria-label="Search results" aria-live="polite"></div></div></div>
<main id="main" tabindex="-1"><div class="page-eyebrow">CERBERUS DEV BOARD <span>/</span> {'DEVELOPER HUB' if slug == 'index' else 'TECHNICAL REFERENCE'}</div><article>{body}</article><div class="page-end"><a href="https://github.com/463N7/Cerberus-Dev-Board/blob/main/content/{slug}.md">View page source ↗</a><a href="https://github.com/463N7/Cerberus-Dev-Board/issues/new/choose">Suggest a correction ↗</a></div></main>
<footer><span>CERBERUS / BUILD. EXPERIMENT. DOCUMENT.</span><span>Reference updated October 27, 2026</span></footer></div></body></html>'''
        (output / f"{slug}.html").write_text(page, encoding="utf-8", newline="\n")
    (assets / "search-index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    export_addon_pinouts(assets, "Six-C5 expansion add-on — in testing", "c5-expansion-pinout.csv")
    export_breakout_pinouts(assets)
    (output / "404.html").write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found | Cerberus Dev Board</title><link rel="icon" href="https://463n7.github.io/Cerberus-Dev-Board/assets/cerberus-logo.svg" type="image/svg+xml"><body style="font-family:system-ui;padding:3rem;max-width:40rem"><h1>Page not found</h1><p>That reference may have moved.</p><a href="/Cerberus-Dev-Board/">Open Cerberus Dev Board</a></body></html>''', encoding="utf-8")
    print(f"Built {len(PAGES)} pages, the 25-GPIO breakout CSV, and six-C5 pinout CSV.")


if __name__ == "__main__":
    build()
