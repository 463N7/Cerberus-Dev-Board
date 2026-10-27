# Built-in pinouts

**All GPIO numbers below refer to the ESP32-S3 unless the C5 column says otherwise.** These are signal assignments, not physical connector pin numbers. The baseline is production N16R2 with 1-bit SDMMC and the Sentinel READY handshake.

<div class="table-filter"><label for="pin-filter">Find a pin or signal</label><input id="pin-filter" type="search" placeholder="Try GPIO44, touch, MOSI, battery…"><p id="pin-filter-status" aria-live="polite"></p></div>

## ST7796 display

| Signal | S3 GPIO | Purpose |
| --- | --- | --- |
| LCD DC | GPIO4 | Command / data selection |
| LCD RESET | GPIO5 | Panel reset |
| LCD BL | GPIO6 | Backlight PWM |
| LCD CS | GPIO16 | SPI2 chip select |
| LCD SCLK | GPIO17 | SPI2 clock |
| LCD MOSI | GPIO18 | Write data to panel |
| LCD MISO | Not used | Reference display driver is write-only |

Reference display setup: 320 × 480 portrait, RGB565, SPI2 at 40 MHz. Pixel orientation and inversion belong to the display driver, not the pin map.

## GT911 touch and shared I²C

| Signal / device | S3 GPIO / address | Notes |
| --- | --- | --- |
| I²C SDA | GPIO8 | Shared I²C0 data |
| I²C SCL | GPIO9 | Shared I²C0 clock; 400 kHz reference |
| Touch INT | GPIO7 | Interrupt / initialization signal |
| Touch RESET | Not connected | Pin value `-1` in the firmware profile |
| GT911 address | `0x5D` | 7-bit I²C address |
| MAX17048 fuel gauge | `0x36` on GPIO8/9 | 7-bit address; battery voltage and estimated percentage |
| BQ25895 charger | Datasheet address `0x6A` | Bus exposure/routing not established by the public pin header; verify before using |

Register added I²C devices on the existing bus; do not initialize another driver over GPIO8/9. Confirm address conflicts and combined pull-up strength.

## microSD — production

| Card signal | S3 GPIO / connection | Notes |
| --- | --- | --- |
| DAT0 | GPIO35 | Single data line |
| CLK | GPIO36 | SDMMC clock |
| CMD | GPIO37 | SDMMC command |
| DAT1 / DAT2 | Board pull-ups | Not used for 1-bit data transfer |
| DAT3 | Board pull-up | Not driven by production firmware |
| GPIO38 | Expansion on revised routing | Historical prototype used this for SD CS / DAT3 test |

Use SDMMC 1-bit mode, not the historical SPI storage map. Octal PSRAM configurations can consume GPIO35–37 and are incompatible with this routing.

## S3 ↔ onboard C5

| Signal | S3 GPIO | Onboard C5 connection | Direction / mode |
| --- | --- | --- | --- |
| SPI CS | GPIO10 | GPIO8 | S3 → C5 |
| SPI MOSI | GPIO11 | GPIO5 | S3 → C5 |
| SPI SCLK | GPIO12 | GPIO4 | S3 → C5 |
| SPI MISO | GPIO13 | GPIO6 | C5 → S3 |
| Runtime READY | GPIO44 | GPIO11 | C5 → S3; Sentinel/Base handshake |
| Programming UART TX | GPIO43 | GPIO12 / UART RX | S3 → C5; 115200 baud |
| Programming UART RX | GPIO44 | GPIO11 / UART TX | C5 → S3; same wire as READY |
| Reset control | GPIO21 | EN through inverting control circuitry | S3 high holds C5 reset; S3 low releases it |
| Boot control | GPIO40 | BOOT through inverting control circuitry | S3 high requests C5 download mode at reset |
| Legacy wardriving IRQ | GPIO39 | GPIO9 | Older scanner profile only; not Sentinel READY |

GPIO44 is actively driven by the C5. Do not connect GPS TX or another peripheral output to it. GPIO43 is a programming signal; optional sharing requires a deliberate design and removal/isolation of the expansion board during C5 flashing.

## Native USB and startup

| Signal / restriction | S3 GPIO | Notes |
| --- | --- | --- |
| USB D− | GPIO19 | Preserve native USB routing |
| USB D+ | GPIO20 | Preserve native USB routing |
| S3 BOOT | GPIO0 startup strap | Board BOOT control for ROM recovery |
| Other startup straps | GPIO3, GPIO45, GPIO46 | External circuitry must preserve required reset states |
| Flash / PSRAM | Module dependent | GPIO26–37 include memory-related signals; never repurpose from a generic pin list |

## Optional historical GPS map

| External GPS signal | Wardriving S3 GPIO | Status |
| --- | --- | --- |
| GPS TX → S3 RX | GPIO1 | 9600 baud in wardriving reference |
| GPS RX ← S3 TX | GPIO2 | Older wardriving profile |
| GPS PPS | GPIO46 | Older profile; do not assume it is used by Sentinel |

The RF/NFC expansion planning chat later considered GPS RX on GPIO48 or shared GPIO43 instead. Those are separate plans, not interchangeable connector definitions. GPS is not built into the production baseline.

## Reusable definitions

Download the [production pin header](https://github.com/463N7/Cerberus-Dev-Board/blob/main/examples/cerberus_board_pins.h). Physical expansion connector numbering is withheld until a labeled as-built pin-1/orientation record is available. See [expansion pinouts](expansion.md).

Source baseline: [Sentinel production pin header](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/shared/cerberus_pins.h), plus the earlier board pinout discussion for C5 UART12/11 and the historical scanner configuration for IRQ39/GPS.
