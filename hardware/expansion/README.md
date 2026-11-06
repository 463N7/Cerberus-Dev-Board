# Expansion-board KiCad files

This is the designated home for **Cerberus expansion boards only**. The [expansion starter project](starter/) is available now. The RF/NFC board and six-C5 bank are separate optional add-ons, both in testing.

The starter contains a KiCad 10 project, PCB, and connector-only schematic for four 20-pin connectors and a prototyping area. [Download the starter ZIP](https://463n7.github.io/Cerberus-Dev-Board/assets/cerberus-expansion-starter.zip), extract it, and open `Cerberus_Proto_Board.kicad_pro`.

For each board, create a revision folder such as `rf-nfc/rev-a/` or `c5-bank/rev-a/` and include:

- Expansion `.kicad_pcb` / `.kicad_pro` files and required local footprints.
- A README with purpose, KiCad version, supported Cerberus revision, connector part number, pin-1 orientation, and supply requirements.
- Bill of materials, assembly notes, mechanical outline, and an explicit license.
- A validation record separating untested, assembled, programming-verified, and functionally tested states.

Do not add the Cerberus main device's PCB, schematics, netlists, Gerbers, or fabrication archives. The only schematic currently included is `starter/Cerberus_Proto_Board.kicad_sch`, which contains the expansion connectors and power symbols. Review any image or exported drawing before upload so main-device design details are not accidentally included.

The 25 breakout GPIO signals, labeled-face photo, and six-C5 GPIO signal map are on the shared [`Pinouts` page](../../content/pinouts.md). Each breakout GPIO has its own row with the processor and side identified. The RF/NFC add-on is in early testing and has no published pin map. Connector part number, pitch, and current ratings are not specified.
