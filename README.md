# Cerberus Dev Board

The hardware and programming reference for the Cerberus handheld development board: ESP32-S3 + ESP32-C5, ST7796 display, GT911 touch, microSD, battery monitoring, and expansion interfaces.

**[Open the developer website](https://463n7.github.io/Cerberus-Dev-Board/)** · **[USB firmware installer](https://463n7.github.io/Cerberus-Flasher/)**

This repository documents the device itself, independently of a particular firmware application. **No Cerberus main-device schematics, PCB sources, fabrication files, or netlists are included.** Expansion-board PCB files have a separate, clearly marked home under [`hardware/expansion/`](hardware/expansion/README.md). Schematic files are excluded from this repository.

## Developer reference

| Guide | Contents |
| --- | --- |
| [Start here](content/getting-started.md) | Identify the board, install firmware, build, and recover USB |
| [Hardware](content/hardware.md) | Base-board processors, memory, buses, and power devices |
| [Pinouts](content/pinouts.md) | Base-board interfaces, labeled expansion breakout, and six-C5 expansion pinout; RF/NFC map not published during early testing |
| [Expansion add-ons](content/expansion.md) | Six-C5 bank and RF/NFC board; both in testing |
| [Programming](content/programming.md) | Toolchain, source layout, memory setup, protocol, and bring-up |
| [Batteries](content/batteries.md) | Tested batteries, “should fit” candidates, dimensions, polarity, and test evidence |
| [Antennas](content/antennas.md) | Radio-specific antenna requirements, connector checks, and comparison records |
| [Troubleshooting](content/troubleshooting.md) | USB, C5, display, touch, SD, battery, and expansion issues |
| [Downloads](content/downloads.md) | Firmware, reusable pin definitions, examples, and expansion CAD location |
| [Reference and testing](content/revisions.md) | Base-board reference, add-on testing status, and remaining measurements |

Cerberus uses an **S3 N16R2, one onboard C5, and 1-bit SDMMC with a 40 MHz maximum target**. The C5 memory specification uses the smallest standard [C5-WROOM option](https://documentation.espressif.com/esp32-c5-wroom-1_wroom-1u_datasheet_en.html): **N4, 4 MB flash and no PSRAM**. Sentinel's current 2 MB firmware layout is a separate software allocation. The RF/NFC board and six-C5 bank are optional expansion add-ons, both in testing. The expansion breakout table identifies contact positions as viewed from its labeled face.

## Maintaining the website

Edit the Markdown in `content/`, then generate the static website:

```powershell
python -m pip install -r requirements.txt
python tools/build_site.py
python tools/check_site.py
python -m http.server 8765 --directory docs
```

Open `http://localhost:8765/`. Commit both the Markdown sources and generated `docs/`. GitHub Pages serves `main:/docs`. The repository check verifies generated content, local links, and the no-schematics boundary.

## Compatibility reports

Use the [battery, antenna, or documentation issue templates](https://github.com/463N7/Cerberus-Dev-Board/issues/new/choose). Include exact model numbers, board revision, measurements, test conditions, and photographs that do not reveal device schematics. “Should fit” is a dimensional estimate, not a tested battery recommendation.

No general hardware license is granted by publishing this reference. Expansion CAD and example code will need explicit license notices before broader reuse is advertised. Linked firmware projects retain their own terms.
