# Cerberus expansion starter

An editable starting point for Cerberus expansion boards: four 20-pin header footprints, their connector schematic, and a prototyping area. This is the expansion board project.

## Open the project

Use **KiCad 10.0 or a compatible newer version**. Extract the complete [starter ZIP](https://463n7.github.io/Cerberus-Dev-Board/assets/cerberus-expansion-starter.zip), then open **`Cerberus_Proto_Board.kicad_pro`**. Keep the project, PCB, and schematic together with their matching filenames.

| File | Contents |
| --- | --- |
| `Cerberus_Proto_Board.kicad_pro` | Project and board settings |
| `Cerberus_Proto_Board.kicad_pcb` | Four-layer, 1.6 mm expansion PCB with J1–J4 and an embedded prototyping footprint |
| `Cerberus_Proto_Board.kicad_sch` | Four 20-pin connectors and their signal/power connections |

## Libraries and models

The connectors use standard **2.54 mm, 1 × 20 pin-header footprints**. Symbols are embedded in the schematic. The custom `protoboard` footprint geometry is embedded in the PCB; a separate custom footprint library was not supplied. Save that embedded footprint into your own library before using library-based footprint updates.

Header 3D models reference KiCad 10's standard `${KICAD10_3DMODEL_DIR}` library. Install the standard 3D-model library for those previews. The custom prototyping footprint retains a generic header model, so the 3D view is not a verified mechanical model.

## Using the starter

Check connector references and pin-1 markers against the [Cerberus pinout](https://463n7.github.io/Cerberus-Dev-Board/pinouts.html) when positioning an add-on. Preserve the shared-bus and startup-pin requirements in that reference. Verify net assignments, board clearance, and your changes before fabrication.

These are starter design files. No electrical, mechanical, ERC, or DRC validation report is included. License: not specified in the supplied files.
