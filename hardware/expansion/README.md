# Expansion-board KiCad files

This is the designated home for **Cerberus expansion add-ons only**: the RF/NFC board and six-C5 bank. **Both are in testing.** No CAD files have been uploaded yet.

For each board, create a revision folder such as `rf-nfc/rev-a/` or `c5-bank/rev-a/` and include:

- Expansion `.kicad_pcb` / `.kicad_pro` files and required local footprints.
- A README with purpose, KiCad version, supported Cerberus revision, connector part number, pin-1 orientation, and supply requirements.
- Bill of materials, assembly notes, mechanical outline, and an explicit license.
- A validation record separating untested, assembled, programming-verified, and functionally tested states.

Do not add the Cerberus main device's PCB, schematics, netlists, Gerbers, or fabrication archives. Schematic files are excluded throughout this repository. Review any image or exported drawing before upload so main-device design details are not accidentally included.

The expansion GPIO signal maps are on the shared [`Pinouts` page](../../content/pinouts.md). Physical connector pin order and power ratings are not listed.
