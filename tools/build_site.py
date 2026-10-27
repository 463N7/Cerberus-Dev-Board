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
    ("pinouts", "Built-in pinouts", "GPIO assignments and bus connections for every built-in interface."),
    ("expansion", "Expansion boards", "C5 bank pinouts, RF/NFC plans, and expansion KiCad files."),
    ("programming", "Programming", "Toolchain, memory settings, drivers, protocol, and bring-up."),
    ("batteries", "Batteries", "Tested batteries and should-fit candidates, with evidence."),
    ("antennas", "Antennas", "Radio-specific antenna compatibility and test records."),
    ("troubleshooting", "Troubleshooting", "Recover USB and diagnose the built-in interfaces."),
    ("downloads", "Downloads", "Firmware links, pin definitions, examples, and expansion files."),
    ("revisions", "Revisions + evidence", "Board variants, verification status, and documentation history."),
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


def build():
    output = ROOT / "docs"
    assets = output / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    for name in ("style.css", "site.js", "mark.svg"):
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
<meta name="theme-color" content="#101817"><link rel="icon" href="assets/mark.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/style.css"><script src="assets/site.js" defer></script></head>
<body class="{'home' if slug == 'index' else 'reference'}"><a class="skip" href="#main">Skip to content</a>
<header class="topbar"><a class="brand" href="index.html"><img src="assets/mark.svg" alt="" width="34" height="34"><span>CERBERUS<small>DEV BOARD</small></span></a><span class="top-label">HARDWARE / SOFTWARE / EXPANSION</span><a class="github" href="https://github.com/463N7/Cerberus-Dev-Board">GitHub <span aria-hidden="true">↗</span></a><button class="menu-button" type="button" aria-controls="sidebar" aria-expanded="false">Menu</button></header>
<aside id="sidebar" class="sidebar"><p class="nav-heading">DEVELOPER REFERENCE</p><nav aria-label="Documentation">{navigation}</nav><div class="sidebar-note"><span class="status-dot"></span>Production N16R2<p>One onboard C5<br>Quad PSRAM · 1-bit SDMMC</p></div><a class="installer-link" href="https://463n7.github.io/Cerberus-Flasher/">Open USB installer ↗</a></aside>
<div class="workspace"><div class="utility"><span>REFERENCE / {html.escape(title.upper())}</span><div class="search-wrap"><label class="sr-only" for="site-search">Search all documentation</label><input id="site-search" type="search" autocomplete="off" placeholder="Search documentation…"><div id="search-results" class="search-results" hidden aria-label="Search results" aria-live="polite"></div></div></div>
<main id="main" tabindex="-1"><div class="page-eyebrow">CERBERUS DEV BOARD <span>/</span> {'DEVELOPER HUB' if slug == 'index' else 'TECHNICAL REFERENCE'}</div><article>{body}</article><div class="page-end"><a href="https://github.com/463N7/Cerberus-Dev-Board/blob/main/content/{slug}.md">View page source ↗</a><a href="https://github.com/463N7/Cerberus-Dev-Board/issues/new/choose">Suggest a correction ↗</a></div></main>
<footer><span>CERBERUS / BUILD. EXPERIMENT. DOCUMENT.</span><span>Reference updated October 27, 2026</span></footer></div></body></html>'''
        (output / f"{slug}.html").write_text(page, encoding="utf-8", newline="\n")
    (assets / "search-index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (assets / "c5-expansion-pinout.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(["signal", "s3_gpio", "wroom_c5_gpio", "xiao_c5_gpio", "scope"])
        for row in [("MOSI",11,10,9,"shared bus"),("SCLK",12,8,8,"shared bus"),("MISO",13,9,10,"shared bus")]:
            writer.writerow(row)
        for slot, pin in enumerate([14,15,41,42,45,48], start=1):
            writer.writerow([f"R{slot} CS",pin,23,7,"one module per slot; not physical header order"])
    (output / "404.html").write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found | Cerberus Dev Board</title><body style="font-family:system-ui;padding:3rem;max-width:40rem"><h1>Page not found</h1><p>That reference may have moved.</p><a href="/Cerberus-Dev-Board/">Open Cerberus Dev Board</a></body></html>''', encoding="utf-8")
    print(f"Built {len(PAGES)} documentation pages and downloadable expansion CSV.")


if __name__ == "__main__":
    build()
