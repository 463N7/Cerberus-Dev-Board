# Expansion add-ons

Cerberus has one base board. The **six-C5 bank** and **RF/NFC board** are optional expansion add-ons. **Both are in testing.** Their GPIO assignments overlap, so each uses its own pin map and compatible firmware.

## Six-C5 expansion add-on — in testing

Adds six WROOM C5 radios to the onboard C5 using a shared SPI bus and individual chip selects. Each expansion module uses the same `c5-expansion-wroom` image; the S3 identifies it by chip-select slot. The memory baseline is 4 MB flash with no PSRAM per expansion C5.

Six modules have passed programming verification. Assembled multi-radio operation and compatibility remain in testing.

[View the complete six-C5 add-on pinout](pinouts.md#six-c5-expansion-add-on-in-testing) · [Download CSV](assets/c5-expansion-pinout.csv)

## RF/NFC expansion add-on — in testing

Adds an E07, two E01 radios, PN532, GPS, an additional CC1101, and a TCA9534A control expander. The current wiring reference uses shared SPI, PN532 in SPI mode, and the expander for the second E01's controls.

Wiring, firmware integration, power, and assembled operation remain in testing. Confirm module suffixes and connector orientation against the board under test.

[View the complete RF/NFC add-on pinout](pinouts.md#rfnfc-expansion-add-on-in-testing) · [Download CSV](assets/rf-nfc-expansion-pinout.csv)

## Shared-bus integration

- Register each SPI device with its own CS, clock rate, mode, and bit order. The onboard C5's 40 MHz setting does not apply to every peripheral.
- Serialize complete request/response sequences where required by the device protocol, and preserve the C5 READY handshake when using its base-board link.
- Make unused selects inactive before starting the bus. Preserve S3 startup-strapping states when adding control circuitry.
- Set the TCA9534A output latch before enabling output directions. I²C expander outputs are for control signals, not SPI clocks or precise pulse capture.
- Use a supply sized for the exact radio modules. GPIOs provide control signals; the base-board expansion-rail current rating still needs verification.
- Power off before attaching or removing an add-on. Isolate circuitry using GPIO43 before programming the onboard C5.

## Connector reference

The [pinouts page](pinouts.md) provides base-board and add-on signal mappings together. Physical header positions, pin-1 orientation, viewing side, mating part, and supply contacts need an as-built connector record before they can be listed as verified.

## Expansion KiCad files

Use [`hardware/expansion/`](https://github.com/463N7/Cerberus-Dev-Board/tree/main/hardware/expansion) for expansion PCB/project files, footprints, and release notes. Keep the RF/NFC and six-C5 designs in separate folders with their own test records.

No CAD files have been uploaded yet. Each design should identify the compatible Cerberus connector, KiCad version, power budget, assembly notes, license, and testing status. Cerberus main-device design files and all schematic files are excluded.
