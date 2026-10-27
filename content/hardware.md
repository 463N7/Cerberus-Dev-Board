# Hardware overview

The production Cerberus reference is the **ESP32-S3 N16R2** device with one onboard **ESP32-C5**, ST7796 LCD, GT911 touch, microSD, native USB, and battery support.

## Built-in features

| Feature | Device / interface | Development notes |
| --- | --- | --- |
| Main processor | ESP32-S3, up to 240 MHz in the board profile | Runs UI, display, touch, storage, and USB |
| S3 memory | 16 MB flash / 2 MB quad PSRAM | Confirmed on a production unit; use the N16R2 configuration |
| Radio coprocessor | ESP32-C5 | Wi-Fi 2.4/5 GHz, BLE, and 802.15.4 depend on firmware support |
| Onboard C5 memory | 8 MB physical flash detected on one tested unit | Sentinel uses a conservative 2 MB partition budget; verify each unit |
| Display | ST7796, 320 × 480 portrait, RGB565 | SPI2 at 40 MHz in Sentinel; landscape is firmware dependent |
| Touch | GT911 | Shared I²C, 7-bit address `0x5D`; INT on GPIO7; no dedicated reset connection |
| microSD | 1-bit SDMMC | CLK36 / CMD37 / DAT0 35; up to 20 MHz in reference firmware |
| USB | ESP32-S3 native USB | GPIO19 D− / GPIO20 D+; serial, programming, and firmware-dependent device modes |
| Battery fuel gauge | MAX17048 | Shared I²C at `0x36`; voltage and state-of-charge estimate |
| Battery charger | BQ25895, identified in prior board design discussion | I²C address `0x6A` per TI; assembled bus access and charger settings need confirmation |
| Expansion | Shared SPI3 and additional GPIOs | Physical header numbering/orientation awaits an as-built connector record |

The C5 silicon supports the listed radio families; an installed application may expose only a subset. Support for 802.15.4 does not itself establish a complete Zigbee or Thread application. The base device has no built-in LoRa, CC1101, nRF24, NFC reader, or GPS in this reference.

## Bus ownership

| Peripheral | S3 interface | Reference setting |
| --- | --- | --- |
| Display | SPI2 | 40 MHz, separate from the radio bus |
| Onboard C5 + compatible expansion | SPI3 | Sentinel onboard link 40 MHz; other devices need their own settings |
| microSD | SDMMC | 1-bit, up to 20 MHz |
| Touch + gauge | I²C0 | 400 kHz in Sentinel |
| C5 programming | UART | 115200 baud, 8N1 through the temporary USB bridge |

The older wardriving transport uses a different SPI protocol and a conservative 250 kHz radio clock. Do not mix its C5 image with Sentinel or assume its IRQ39 wiring replaces the current READY44 handshake.

## Board and application variants

| Configuration | Memory / routing distinction | Compatibility |
| --- | --- | --- |
| Production N16R2 | 16 MB flash, 2 MB quad PSRAM, 1-bit SDMMC | Baseline for these docs and Sentinel |
| Earlier prototype | SD SPI used GPIO38 as CS / DAT3 test control | Do not use GPIO38 for expansion until routing and firmware are checked |
| R8 development / Arcade | 8 MB octal PSRAM in the R8 game profile | Not a drop-in production memory configuration; GPIO35–37 conflict with octal memory use |
| Six-C5 bank | Six additional C5 modules, individual selects | Optional expansion hardware and matching firmware |
| RF/NFC board | E01/E07/CC1101/PN532/GPS concepts | Planning variants; no assembled revision is certified here |

## Electrical and mechanical reference

Treat S3/C5 signals as **3.3 V logic**. Do not connect 5 V signal outputs directly or infer supply capability from a GPIO label. Verify a peripheral's logic voltage separately from its supply input.

Keep GPIO19/20 for USB, memory pins for flash/PSRAM, and GPIO0/3/45/46 startup strapping requirements intact. Do not treat an unassigned GPIO as physically exposed or safe to repurpose. The production SD pull-up network means GPIO38 is not an SD control in the production firmware.

The following need board-specific measurement before being advertised: expansion-rail current limits, charger input/charge limits, battery connector part number/polarity, enclosure battery cavity, board outline, mounting holes, antenna connector part numbers, and physical header numbering. A component's datasheet maximum is not the assembled board's rating.

## References

- [Public production pin definitions](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/shared/cerberus_pins.h)
- [Sentinel build and memory profile](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/docs/SENTINEL_BUILD.md)
- [Recorded first-board flash detection](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/docs/FIRST_BOARD_FLASH.md)
- [Espressif ESP32-C5 capabilities](https://www.espressif.com/en/products/socs/esp32-c5)
- [Espressif ESP32-S3 GPIO restrictions](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/gpio.html)
- [Analog Devices MAX17048](https://www.analog.com/en/products/max17048.html)
- [TI BQ25895 product and datasheet](https://www.ti.com/product/BQ25895)
