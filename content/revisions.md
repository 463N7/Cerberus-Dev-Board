# Reference and testing

This reference covers the **base Cerberus board**: ESP32-S3 N16R2, one onboard ESP32-C5 with a 4 MB flash / no-PSRAM memory baseline, ST7796 display, GT911 touch, shared I²C, native USB, and 1-bit SDMMC with a 40 MHz maximum clock target.

## Base-board reference

The [Cerberus pin definitions](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/shared/cerberus_pins.h) establish the built-in signal mappings. The [firmware build guide](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/docs/SENTINEL_BUILD.md) documents the application memory layout and programming workflow. The website's 40 MHz SDMMC target requires matching firmware configuration; actual clock and stability depend on the card and assembled device.

The C5 memory specification uses the smallest standard WROOM option, **N4: 4 MB flash and no PSRAM**. Sentinel's current 2 MB firmware layout is a separate software allocation.

## Expansion add-on status

| Expansion add-on | Status | Recorded progress | Remaining validation |
| --- | --- | --- | --- |
| Six-C5 bank | **In testing** | Six 4 MB WROOM modules passed programming verification | Assembled multi-radio operation and integration |
| RF/NFC board | **In testing** | Current signal map documented | Wiring, power, firmware integration, and assembled operation |

Neither add-on is a different base-board model. Their signal assignments are listed separately on the [pinouts page](pinouts.md).

## Records still needed

1. Connector photos with pin 1 and viewing side, plus a continuity-verified physical header map and mating connector details.
2. Expansion supply contacts and current ratings.
3. Battery connector/polarity, configured charge limits, enclosure cavity measurements, and exact tested battery models.
4. Antenna connector and module part numbers, with band-specific compatibility results.
5. Expansion KiCad PCB files, assembly notes, and matching validation records.
6. Card-specific SDMMC read/write and cold-start results at the 40 MHz target.

## Documentation changelog

| Date | Change |
| --- | --- |
| 2026-10-27 | Initial Cerberus Dev Board hardware and programming reference |
| 2026-10-27 | Set C5 memory baseline to WROOM N4: 4 MB flash, no PSRAM |
| 2026-10-27 | Focused the reference on the base board; set SDMMC target to 40 MHz; consolidated both expansion add-on maps on Pinouts and marked both in testing |

Use the [documentation issue form](https://github.com/463N7/Cerberus-Dev-Board/issues/new?template=documentation.yml) for corrections and supporting evidence. Hardware results should identify the firmware, date, attached add-on, and test conditions.
