# Downloads and project links

## Firmware

| Resource | Purpose |
| --- | --- |
| [Cerberus USB Installer](https://463n7.github.io/Cerberus-Flasher/) | Guided installation through the device USB connection |
| [Cerberus Sentinel source](https://github.com/463N7/Cerberus-Sentinel) | Application and built-in driver reference |
| [Installer source](https://github.com/463N7/Cerberus-Flasher) | Public web installer and release metadata |

Use matched release images and each package's checksums and offsets. This reference does not copy firmware binaries into a second release channel.

## Developer files

| File / folder | What is included | Status |
| --- | --- | --- |
| [Cerberus board pin header](https://github.com/463N7/Cerberus-Dev-Board/blob/main/examples/cerberus_board_pins.h) | S3 and onboard C5 signal constants | GPIO definitions |
| [Read-only I²C identification example](https://github.com/463N7/Cerberus-Dev-Board/blob/main/examples/i2c-identify/main/main.c) | Probe GT911/MAX17048 addresses and log ACK results | Standalone ESP-IDF example; hardware testing pending |
| [Expansion breakout CSV](assets/expansion-breakout-pinout.csv) | 25 GPIO signals with processor, printed label, and side; power and ground omitted | View from the labeled face; top to bottom on each side |
| [Expansion breakout photo](assets/expansion-breakout.jpg) | Labeled face and GPIO group orientation | Full-size JPEG |
| [Tested battery photo](assets/tested-batteries.jpg) | Four tested packs and their printed labels | Full-size JPEG; see the [battery list](batteries.md#tested-batteries) |
| [Six-C5 WROOM expansion CSV](assets/c5-expansion-pinout.csv) | S3 CS slots and WROOM expansion SPI mapping | Expansion add-on still in testing; GPIO assignments only |
| [Expansion KiCad area](https://github.com/463N7/Cerberus-Dev-Board/tree/main/hardware/expansion) | Revision folders for expansion PCB/project files and footprints | Prepared; no CAD release uploaded yet |

The six-C5 bank is in testing. The RF/NFC add-on is in early testing and has no published pinout or download.

## What belongs here

The repository accepts development documentation, reviewed pin definitions, examples, compatibility records, and explicitly identified expansion PCB files. Main-device schematics, PCB files, netlists, Gerbers, and board fabrication archives are outside this publication. Schematic files are excluded throughout the repository.

Before adding a manufacturing download, identify the exact expansion revision, supported Cerberus revision, connector orientation, KiCad version, license, and test status. Only mark a layout ready for fabrication when its review and validation records support that claim.
