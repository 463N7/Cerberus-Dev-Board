# Expansion add-ons

Cerberus has one base board. The **six-C5 bank** and **RF/NFC board** are optional expansion add-ons. **Both are in testing.**

## Base-board expansion connections

The [expansion breakout table](pinouts.md#expansion-breakout-connections) lists all 25 GPIO signals individually: 18 S3 and 7 C5. Each entry identifies the processor, printed label, and side. The photo shows the viewing orientation. [Download the breakout CSV](assets/expansion-breakout-pinout.csv).

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

### Expansion starter project

[Download the expansion starter ZIP](assets/cerberus-expansion-starter.zip) · [Browse the KiCad source files](https://github.com/463N7/Cerberus-Dev-Board/tree/main/hardware/expansion/starter)

An editable **KiCad 10** project with an expansion PCB, four 20-pin connector footprints, a prototyping area, and the matching expansion connector schematic. Extract the ZIP and open **`Cerberus_Proto_Board.kicad_pro`**. Keep the `.kicad_pro`, `.kicad_pcb`, and `.kicad_sch` files together.

The custom prototyping footprint is embedded in the PCB. Standard KiCad libraries provide the connectors and header 3D models. The [project README](https://github.com/463N7/Cerberus-Dev-Board/blob/main/hardware/expansion/starter/README.md) describes dependencies and validation status. These are starter files; a fabrication-validation report is not included.

Use [`hardware/expansion/`](https://github.com/463N7/Cerberus-Dev-Board/tree/main/hardware/expansion) for expansion PCB/project files, footprints, and release notes. Keep the RF/NFC and six-C5 designs in separate folders with their own test records.

Cerberus main-device design files remain excluded. The supplied starter's connector-only schematic is included with its expansion project.
