# Expansion add-ons

Cerberus has one base board. The **six-C5 bank** and **RF/NFC board** are optional expansion add-ons. **Both are in testing.**

## Base-board expansion connections

The [expansion breakout table](pinouts.md#expansion-breakout-connections) lists both labeled rows, including the separate S3 and C5 GPIO groups and the ground, 3.3 V, and 5 V contacts. The photo shows the viewing orientation. [Download the breakout CSV](assets/expansion-breakout-pinout.csv).

## Six-C5 expansion add-on — in testing

Adds six WROOM C5 radios to the onboard C5 using a shared SPI bus and individual chip selects. Each expansion module uses the same `c5-expansion-wroom` image; the S3 identifies it by chip-select slot. The memory baseline is 4 MB flash with no PSRAM per expansion C5.

Six modules have passed programming verification. Assembled multi-radio operation and compatibility remain in testing.

[View the complete six-C5 add-on pinout](pinouts.md#six-c5-expansion-add-on-in-testing) · [Download CSV](assets/c5-expansion-pinout.csv)

## RF/NFC expansion add-on — early testing

Optional RF/NFC expansion board in early testing. Pin assignments and wiring details are not published at this stage.

## Shared-bus integration

- Register each SPI device with its own CS, clock rate, mode, and bit order. The onboard C5's 40 MHz setting does not apply to every peripheral.
- Serialize complete request/response sequences where required by the device protocol, and preserve the C5 READY handshake when using its base-board link.
- Make unused selects inactive before starting the bus. Preserve S3 startup-strapping states when adding control circuitry.
- Use a supply sized for the exact radio modules. GPIOs provide logic signals, not module power.
- Power off before attaching or removing an add-on. Isolate circuitry using GPIO43 before programming the onboard C5.

## Expansion KiCad files

Use [`hardware/expansion/`](https://github.com/463N7/Cerberus-Dev-Board/tree/main/hardware/expansion) for expansion PCB/project files, footprints, and release notes. Keep the RF/NFC and six-C5 designs in separate folders with their own test records.

No CAD files have been uploaded yet. Each design should identify the compatible Cerberus connector, KiCad version, power budget, assembly notes, license, and testing status. Cerberus main-device design files and all schematic files are excluded.
