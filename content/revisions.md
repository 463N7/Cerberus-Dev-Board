# Reference and testing

This reference covers the **base Cerberus board**: ESP32-S3 N16R2, one onboard ESP32-C5 with a 4 MB flash / no-PSRAM memory baseline, ST7796 display, GT911 touch, shared I²C, native USB, and 1-bit SDMMC with a 40 MHz maximum clock target.

## Base-board reference

The [Cerberus pin definitions](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/shared/cerberus_pins.h) list the built-in signal mappings. The [firmware build guide](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/docs/SENTINEL_BUILD.md) covers the application memory layout and programming workflow. SDMMC uses a 40 MHz maximum setting; the card and firmware negotiate the actual clock.

The C5 memory specification uses the smallest standard WROOM option, **N4: 4 MB flash and no PSRAM**. Sentinel's current 2 MB firmware layout is a separate software allocation.

## Expansion add-on status

| Expansion add-on | Status | Completed checks | Testing scope |
| --- | --- | --- | --- |
| Six-C5 bank | **In testing** | Six 4 MB WROOM modules passed programming verification | Assembled multi-radio operation and integration |
| RF/NFC board | **Early testing** | No published pin map | Design and wiring development |

Both are optional add-ons to the base board. The six-C5 signal assignments are listed on the [pinouts page](pinouts.md).

## Documentation changelog

| Date | Change |
| --- | --- |
| 2026-10-27 | Initial Cerberus Dev Board hardware and programming reference |
| 2026-10-27 | Set C5 memory baseline to WROOM N4: 4 MB flash, no PSRAM |
| 2026-10-27 | Focused the reference on the base board and set SDMMC target to 40 MHz |
| 2026-10-27 | Confirmed BQ25895 on shared I²C0, GPIO8/9 at 0x6A; removed the RF/NFC map and download during early testing |
| 2026-10-27 | Added labeled expansion breakout contact order, processor domains, photo, and CSV |
| 2026-10-27 | Listed each expansion GPIO individually; removed power and ground contacts from the table and CSV |
| 2026-10-27 | Added four tested batteries: PL 606090, PL 505573, PL 695084, and BATMAX BT-PS3, with a reference photo |

Use the [documentation issue form](https://github.com/463N7/Cerberus-Dev-Board/issues/new?template=documentation.yml) for corrections and supporting evidence. Hardware results should identify the firmware, date, attached add-on, and test conditions.
