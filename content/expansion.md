# Expansion boards

There are two different expansion efforts: the **six-C5 scanner bank**, with module programming records, and a **planned RF/NFC board** discussed for E01/E07/CC1101/PN532/GPS. Their GPIO assignments overlap. Select one board profile before writing drivers.

## Six-C5 bank — firmware signal map

All radios share the S3 SPI3 data signals. Radio identity follows the S3 chip-select slot; the six expansion modules use the same expansion firmware image.

| Signal | S3 GPIO |
| --- | --- |
| Shared MOSI | GPIO11 |
| Shared SCLK | GPIO12 |
| Shared MISO | GPIO13 |
| R0 onboard C5 CS | GPIO10 |
| R1 expansion C5 CS | GPIO14 |
| R2 expansion C5 CS | GPIO15 |
| R3 expansion C5 CS | GPIO41 |
| R4 expansion C5 CS | GPIO42 |
| R5 expansion C5 CS | GPIO45 |
| R6 expansion C5 CS | GPIO48 |
| R0 legacy IRQ | GPIO39; onboard C5 GPIO9 |

GPIO11/12/13 are bus signals, not spare chip-select pins. The older scanner bank uses its own SPI protocol. It is not supported simply by attaching it to unmodified Sentinel.

## C5 module side — choose the matching board

| Signal | Onboard C5 | WROOM expansion | Historical XIAO prototype |
| --- | --- | --- | --- |
| SCLK | GPIO4 | GPIO8 | GPIO8 |
| MOSI input | GPIO5 | GPIO10 | GPIO9 |
| MISO output | GPIO6 | GPIO9 | GPIO10 |
| CS | GPIO8 | GPIO23 | GPIO7 |
| Legacy IRQ | GPIO9 | Unused | Unused |
| Scanner build environment | `c5-onboard` | `c5-expansion-wroom` | `c5-expansion-xiao` |

The XIAO prototype routes MOSI/MISO differently from the dedicated WROOM board. Their binaries and wiring must not be substituted. Six WROOM modules reported 4 MB flash and passed programming verification on September 29, 2026. That verifies image writing, not simultaneous seven-radio operation; the assembled scan test remained pending in that record.

## Physical connector reference

GPIO38/41/42 were explicitly identified as expansion signals in the revised SDMMC routing discussion. The exact **as-built connector position, pin-1 mark, viewing side, row direction, pitch, mating part, supply pins, and current rating** are not yet supported by a recovered connector record.

A 2×13 connector table appeared in the RF planning discussion, but it was a proposed redesign. It is not presented here as the physical header on existing devices. Before wiring, obtain the board revision's labeled connector photo or continuity-verified map.

## RF/NFC expansion — latest planning variant

**Planning reference only.** The most recent discussed variant kept PN532 on SPI, moved the second E01's controls onto a TCA9534A, and added an Elechouse 915 MHz CC1101 with direct GDO inputs. No as-built KiCad release or assembled validation is included.

| Device | Signal | Proposed connection |
| --- | --- | --- |
| All SPI peripherals | MOSI / SCLK / MISO | GPIO11 / GPIO12 / GPIO13 |
| E07 | CSN | GPIO14 |
| E07 | GDO0 / GDO2 | GPIO2 / GPIO47 |
| E07 | TX_EN / RX_EN | GPIO45 / GPIO46; startup-strapping review required |
| E01 #1 | CSN / CE | GPIO15 / GPIO3; startup-strapping review required |
| E01 #2 | CSN / CE | TCA9534A P0 / P1 |
| PN532 | SS | GPIO42 |
| GPS | TX → S3 RX | GPIO1 |
| GPS | RX ← S3 TX | GPIO48 |
| Added Elechouse CC1101 | CSN | GPIO43; conflicts with C5 programming traffic |
| Added Elechouse CC1101 | GDO0 / GDO2 | GPIO38 / GPIO41 |
| TCA9534A | SDA / SCL | GPIO8 / GPIO9 |
| TCA9534A | Address | `0x38` when A0/A1/A2 are low |

This is the final proposal recovered from that planning chat, not a verified board definition. Earlier alternatives used other PN532, GPS, E01 CE, and GDO pins. Confirm GPIO output capability, startup straps, physical exposure, power, firmware support, and module suffixes against the actual expansion design before implementation.

## Shared-bus development rules

- Register each SPI device with its own CS, clock rate, mode, and bit order. Do not apply the C5's 40 MHz setting to every peripheral.
- Serialize complete request/response sequences when the protocol requires it; preserve the C5 READY handshake when using Sentinel's link.
- Make every unused CS inactive before starting the bus. Use board-appropriate reset bias on selects and enables while preserving S3 startup straps.
- For a proposed expander, set its output latch to the desired state before enabling output directions. Slow I²C control signals are not substitutes for precise pulse capture or SPI clocks.
- Keep radio power separate from GPIO control. The E01 suffix changes peak current and footprint; the prior 2 A and 3 A supply proposals were design budgets, not measured Cerberus expansion-rail ratings.
- Power off before attaching/removing a board. Isolate or remove add-ons using GPIO43 before C5 programming.

## KiCad files have a home

Use [`hardware/expansion/`](https://github.com/463N7/Cerberus-Dev-Board/tree/main/hardware/expansion) for expansion **PCB/project files, footprints, and release notes**. Add each design in a revision-named folder and include connector orientation, supported Cerberus revision, power budget, assembly notes, and validation status.

No CAD files have been added yet. Main-device CAD and all schematic files are excluded. A folder is not a manufacturing release; only label a revision “tested” when there is a matching validation record.
