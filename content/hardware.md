# Hardware overview

The base Cerberus board uses an **ESP32-S3 N16R2** with one onboard **ESP32-C5**, ST7796 LCD, GT911 touch, microSD, native USB, and battery support.

## Built-in features

| Feature | Device / interface | Development notes |
| --- | --- | --- |
| Main processor | ESP32-S3, up to 240 MHz in the board profile | Runs UI, display, touch, storage, and USB |
| S3 memory | 16 MB flash / 2 MB quad PSRAM | Use the N16R2 configuration |
| Radio coprocessor | ESP32-C5 | Wi-Fi 2.4/5 GHz, BLE, and 802.15.4 depend on firmware support |
| Onboard C5 memory | 4 MB flash / no PSRAM | Minimum ESP32-C5-WROOM-1/1U N4 configuration; Sentinel currently uses a 2 MB firmware layout |
| Display | ST7796, 320 × 480 portrait, RGB565 | SPI2 at 40 MHz in Sentinel; landscape is firmware dependent |
| Touch | GT911 | Shared I²C, 7-bit address `0x5D`; INT on GPIO7; no dedicated reset connection |
| microSD | 1-bit SDMMC, up to 40 MHz | CLK36 / CMD37 / DAT0 35; configure firmware for the 40 MHz maximum target |
| USB | ESP32-S3 native USB | GPIO19 D− / GPIO20 D+; serial, programming, and firmware-dependent device modes |
| Battery fuel gauge | MAX17048 | Shared I²C at `0x36`; voltage and state-of-charge estimate |
| Battery charger | BQ25895 | Shared I²C0: SDA GPIO8, SCL GPIO9, address `0x6A`; battery charging and power-path control |
| Expansion | Shared SPI3 and additional GPIOs | RF/NFC and six-C5 expansion add-ons; both in testing |

The C5 memory specification uses the smallest standard WROOM configuration listed by Espressif: **N4, with 4 MB Quad SPI flash and no PSRAM**. Firmware can use a smaller partition layout within that capacity.

The C5 silicon supports the listed radio families; an installed application may expose only a subset. Support for 802.15.4 does not itself establish a complete Zigbee or Thread application. The base device has no built-in LoRa, CC1101, nRF24, NFC reader, or GPS in this reference.

## Bus ownership

| Peripheral | S3 interface | Reference setting |
| --- | --- | --- |
| Display | SPI2 | 40 MHz, separate from the radio bus |
| Onboard C5 + compatible expansion | SPI3 | Sentinel onboard link 40 MHz; other devices need their own settings |
| microSD | SDMMC | 1-bit, up to 40 MHz; actual clock negotiated by card and firmware |
| Touch + gauge + charger | I²C0 | SDA GPIO8 / SCL GPIO9; 400 kHz in Sentinel |
| C5 programming | UART | 115200 baud, 8N1 through the temporary USB bridge |

Configure firmware for 1-bit SDMMC with a 40 MHz maximum clock. See the [configuration example](programming.md#sdmmc-1-bit-40-mhz-configuration).

## Optional expansion add-ons

| Add-on | Features | Status |
| --- | --- | --- |
| Six-C5 bank | Six additional WROOM C5 radios with individual selects | **In testing** |
| RF/NFC board | Optional RF and NFC expansion | **Early testing; pin map not published** |

Both connect to the same base Cerberus board. The six-C5 signal assignments are on the [pinouts page](pinouts.md), with add-on status and file locations on [Expansion add-ons](expansion.md).

## Electrical and mechanical reference

Treat S3/C5 signals as **3.3 V logic**. Do not connect 5 V signal outputs directly or infer supply capability from a GPIO label. Verify a peripheral's logic voltage separately from its supply input.

Keep GPIO19/20 for USB, memory pins for flash/PSRAM, and GPIO0/3/45/46 startup strapping requirements intact. Preserve the quad-PSRAM configuration and the SDMMC pull-up network. Do not treat an unassigned GPIO as physically exposed or safe to repurpose.

## References

- [Base-board pin definitions](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/shared/cerberus_pins.h)
- [Sentinel build and memory profile](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/docs/SENTINEL_BUILD.md)
- [Espressif SDMMC high-speed configuration](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/sdmmc_host.html)
- [Espressif ESP32-C5 capabilities](https://www.espressif.com/en/products/socs/esp32-c5)
- [Espressif C5-WROOM series comparison and memory options](https://documentation.espressif.com/esp32-c5-wroom-1_wroom-1u_datasheet_en.html)
- [Espressif ESP32-S3 GPIO restrictions](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/gpio.html)
- [Analog Devices MAX17048](https://www.analog.com/en/products/max17048.html)
- [TI BQ25895 product and datasheet](https://www.ti.com/product/BQ25895)
