# Pinouts

**GPIO numbers refer to the ESP32-S3 unless a C5 column says otherwise.** These are signal assignments, not physical connector positions.

Jump to the [base board](#base-cerberus-board), [six-C5 expansion add-on](#six-c5-expansion-add-on-in-testing), or [RF/NFC expansion add-on](#rfnfc-expansion-add-on-in-testing). Both expansion add-ons are **in testing** and have separate pin maps.

<div class="table-filter"><label for="pin-filter">Find a pin or signal</label><input id="pin-filter" type="search" placeholder="Try GPIO44, touch, MOSI, PN532…"><p id="pin-filter-status" aria-live="polite"></p></div>

## Base Cerberus board

The base board uses an ESP32-S3 N16R2, one onboard ESP32-C5, and 1-bit SDMMC with a **40 MHz maximum clock target**.

### ST7796 display

| Signal | S3 GPIO | Purpose |
| --- | --- | --- |
| LCD DC | GPIO4 | Command / data selection |
| LCD RESET | GPIO5 | Panel reset |
| LCD BL | GPIO6 | Backlight PWM |
| LCD CS | GPIO16 | SPI2 chip select |
| LCD SCLK | GPIO17 | SPI2 clock |
| LCD MOSI | GPIO18 | Write data to panel |
| LCD MISO | Not used | Display driver is write-only |

Display setup: 320 × 480 portrait, RGB565, SPI2 at 40 MHz. Pixel orientation and inversion belong to the display driver.

### GT911 touch and shared I²C

| Signal / device | S3 GPIO / address | Notes |
| --- | --- | --- |
| I²C SDA | GPIO8 | Shared I²C0 data |
| I²C SCL | GPIO9 | Shared I²C0 clock; 400 kHz |
| Touch INT | GPIO7 | Interrupt / initialization signal |
| Touch RESET | Not connected | No dedicated reset GPIO |
| GT911 address | `0x5D` | 7-bit I²C address |
| MAX17048 fuel gauge | `0x36` on GPIO8/9 | Battery voltage and estimated percentage |
| BQ25895 charger | `0x6A` | Charger control/status; host-bus routing pending confirmation |

Register added I²C devices on the existing bus. Check address conflicts and combined pull-up strength.

### microSD

| Card signal | S3 GPIO / connection | Notes |
| --- | --- | --- |
| DAT0 | GPIO35 | Single data line |
| CLK | GPIO36 | SDMMC clock; up to 40 MHz |
| CMD | GPIO37 | SDMMC command |
| DAT1 / DAT2 | Board pull-ups | Not used for 1-bit data transfer |
| DAT3 | Board pull-up | Not driven by firmware |

Use **1-bit SDMMC**, with `SDMMC_FREQ_HIGHSPEED` as the 40 MHz maximum configuration. The actual clock is negotiated by the card and firmware. See the [SDMMC configuration example](programming.md#sdmmc-1-bit-40-mhz-configuration).

### S3 ↔ onboard C5

| Signal | S3 GPIO | Onboard C5 connection | Direction / mode |
| --- | --- | --- | --- |
| SPI CS | GPIO10 | GPIO8 | S3 → C5 |
| SPI MOSI | GPIO11 | GPIO5 | S3 → C5 |
| SPI SCLK | GPIO12 | GPIO4 | S3 → C5 |
| SPI MISO | GPIO13 | GPIO6 | C5 → S3 |
| Runtime READY | GPIO44 | GPIO11 | C5 → S3 |
| Programming UART TX | GPIO43 | GPIO12 / UART RX | S3 → C5; 115200 baud |
| Programming UART RX | GPIO44 | GPIO11 / UART TX | C5 → S3; same wire as READY |
| Reset control | GPIO21 | EN through inverting circuitry | S3 high holds reset; low releases it |
| Boot control | GPIO40 | BOOT through inverting circuitry | S3 high requests download mode at reset |

GPIO44 is driven by the onboard C5. Keep other peripheral outputs off that wire. GPIO43 is the C5 programming TX signal; isolate add-on circuitry using it before C5 flashing.

### Native USB and startup

| Signal / restriction | S3 GPIO | Notes |
| --- | --- | --- |
| USB D− | GPIO19 | Native USB |
| USB D+ | GPIO20 | Native USB |
| S3 BOOT | GPIO0 | ROM recovery control |
| Other startup straps | GPIO3, GPIO45, GPIO46 | Preserve required reset states |
| Flash / PSRAM | Module memory connections | Preserve the N16R2 quad-PSRAM configuration |

## Six-C5 expansion add-on — in testing

**Optional expansion add-on · In testing.** This board adds six WROOM C5 radios to the base board's onboard C5. Matching add-on firmware is required.

### S3 bus and radio selects

| Signal | S3 GPIO | Notes |
| --- | --- | --- |
| Shared MOSI | GPIO11 | S3 → all C5 radios |
| Shared SCLK | GPIO12 | S3 → all C5 radios |
| Shared MISO | GPIO13 | Selected C5 → S3 |
| R0 onboard C5 CS | GPIO10 | Base-board radio |
| R1 add-on C5 CS | GPIO14 | Expansion radio 1 |
| R2 add-on C5 CS | GPIO15 | Expansion radio 2 |
| R3 add-on C5 CS | GPIO41 | Expansion radio 3 |
| R4 add-on C5 CS | GPIO42 | Expansion radio 4 |
| R5 add-on C5 CS | GPIO45 | Expansion radio 5 |
| R6 add-on C5 CS | GPIO48 | Expansion radio 6 |

### WROOM C5 module side

| Signal | Expansion C5 GPIO | S3 connection |
| --- | --- | --- |
| MOSI input | GPIO10 | S3 GPIO11 |
| SCLK | GPIO8 | S3 GPIO12 |
| MISO output | GPIO9 | S3 GPIO13 |
| CS | GPIO23 | Assigned S3 radio-select slot above |

Each expansion C5 uses the `c5-expansion-wroom` image; its radio identity follows the S3 chip-select slot. The memory baseline is **4 MB flash / no PSRAM**. Programming checks have passed on six modules; assembled multi-radio operation remains in testing.

Download the [six-C5 expansion pinout CSV](assets/c5-expansion-pinout.csv).

## RF/NFC expansion add-on — in testing

**Optional expansion add-on · In testing.** This board adds E07, two E01 radios, PN532, GPS, an additional CC1101, and a TCA9534A control expander. The assignments below are the current wiring reference under test.

### Shared buses

| Bus signal | S3 GPIO | Connected devices |
| --- | --- | --- |
| SPI MOSI | GPIO11 | Onboard C5 and RF/NFC SPI devices |
| SPI SCLK | GPIO12 | Onboard C5 and RF/NFC SPI devices |
| SPI MISO | GPIO13 | Onboard C5 and RF/NFC SPI devices |
| I²C SDA | GPIO8 | Onboard I²C devices and TCA9534A |
| I²C SCL | GPIO9 | Onboard I²C devices and TCA9534A |

### Device control and data signals

| Device | Signal | Connection | Notes |
| --- | --- | --- | --- |
| E07 | CSN | GPIO14 | Dedicated chip select |
| E07 | GDO0 | GPIO2 | Direct S3 input |
| E07 | GDO2 | GPIO47 | Direct S3 input |
| E07 | TX_EN | GPIO45 | Startup strap; keep required reset state |
| E07 | RX_EN | GPIO46 | Startup strap; keep required reset state |
| E01 #1 | CSN | GPIO15 | Dedicated chip select |
| E01 #1 | CE | GPIO3 | Startup strap; keep required reset state |
| E01 #2 | CSN | TCA9534A P0 | Expander output |
| E01 #2 | CE | TCA9534A P1 | Expander output |
| PN532 | SS | GPIO42 | SPI mode |
| GPS | TX → S3 RX | GPIO1 | GPS serial output |
| GPS | RX ← S3 TX | GPIO48 | GPS serial input |
| Additional CC1101 | CSN | GPIO43 | Shares C5 programming TX; isolate for flashing |
| Additional CC1101 | GDO0 | GPIO38 | Expansion signal |
| Additional CC1101 | GDO2 | GPIO41 | Expansion signal |
| TCA9534A | I²C address | `0x38` | A0/A1/A2 low |

### Module setup and power

| Device / connection | Requirement |
| --- | --- |
| E07, both E01 modules, additional CC1101 | Regulated add-on 3.3 V rail and common GND; size the supply for the exact module suffixes |
| PN532 | SPI interface; Elechouse V3 selector CH1 OFF / CH2 ON; verify the fitted module's supply rating |
| GPS | Supply and logic levels must match the fitted receiver or breakout |
| TCA9534A | 3.3 V and common GND; establish CSN high / CE low before enabling its output directions |
| E01 IRQ / PN532 IRQ and reset | Not assigned in this wiring reference |

E07 TX_EN and RX_EN must not be asserted together. The add-on requires compatible drivers and per-device SPI clock/mode settings. Its GPIO assignments overlap the six-C5 add-on, so use each add-on's own map and firmware configuration.

Download the [RF/NFC expansion pinout CSV](assets/rf-nfc-expansion-pinout.csv).

## Connector orientation and developer files

These tables provide GPIO-to-signal mappings. Physical connector pin order and power ratings are not listed.

Download the [base-board pin header](https://github.com/463N7/Cerberus-Dev-Board/blob/main/examples/cerberus_board_pins.h). The [expansion add-ons page](expansion.md) has testing status, bus integration notes, and the expansion KiCad file area.

Base-board source: [Cerberus pin definitions](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/shared/cerberus_pins.h). Add-on mappings are documented separately above and remain in testing.
