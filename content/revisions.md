# Revisions and evidence

This reference was assembled on **October 27, 2026** from the current public Sentinel source, local production/scanner records, and earlier Cerberus hardware discussions. Source-confirmed pin assignments, hardware observations, and proposed designs are different evidence levels.

## Reference baseline

The public source baseline is [Cerberus Sentinel commit 580c80d](https://github.com/463N7/Cerberus-Sentinel/tree/580c80d77e0eaa952028e65293b4b097be18c7cf). It provides the production pin map, toolchain, memory configuration, driver behavior, and C5 bridge contract. Upstream changes do not automatically change the baseline in these docs.

| Record | What it establishes | What it does not establish |
| --- | --- | --- |
| Production pin definitions | LCD, touch, SDMMC, S3/C5 SPI and READY signals | Physical connector position or every unit's assembly |
| First-board flash record, October 11 | One S3 detected with 16 MB flash / 2 MB PSRAM; one C5 with 8 MB physical flash | A guarantee that every C5 has that capacity |
| Later battery/health verification | MAX17048 available with plausible voltage/SOC; later SD mount success recorded | Exact battery SKU, charging limits, runtime, or cell-presence sensing |
| Six-C5 programming record, September 29 | Six 4 MB WROOM modules passed write verification | Completed cold-cycle seven-radio scan acceptance |
| Earlier Rev A design discussion | BQ25895 charger identification and STAT LED discussion | Full recovered charger settings or exact battery product list |
| Revised SDMMC routing discussion | GPIO38 expansion routing, SD on GPIO35/36/37 | A complete physical header orientation record |
| RF/NFC expansion planning | E01/E07/PN532/GPS and later CC1101/expander proposals | Fabricated board, verified pinout, or working firmware support |

## Revision boundaries

- **Production N16R2:** default device reference. Quad PSRAM, SDMMC 1-bit, ST7796/GT911, and onboard C5.
- **Prototype SD wiring:** GPIO38 may be tied to DAT3/CS. Check the actual routing before reuse.
- **R8 Arcade development:** octal memory and additional controls/audio are application-specific. Arcade audio on GPIO11/12/13 overlaps the C5 SPI bus; buttons also overlap expansion and GPS signals. These are not extra built-in features of the baseline board.
- **WROOM versus XIAO expansion:** different MOSI/MISO/CS mappings, separate firmware targets.

## Next records to add

1. Base-board revision label and clear connector photos with pin 1 and viewing side.
2. A continuity-verified physical expansion-header map, mating connector, and power pin ratings.
3. Exact battery connector and polarity, charger configured limits, enclosure cavity measurements, and known battery SKUs.
4. Antenna module/connector part numbers and a tested antenna table with band-specific results.
5. Expansion KiCad PCB releases, mechanical outline, assembly notes, and validation logs.
6. A small standalone board-support project with a repeatable display/touch/SD/C5 test procedure.

## Documentation changelog

| Date | Change |
| --- | --- |
| 2026-10-27 | Initial Cerberus Dev Board reference; production pinouts, expansion profiles, programming/recovery, battery/antenna record structures, and separate expansion CAD area |

Use the [documentation issue form](https://github.com/463N7/Cerberus-Dev-Board/issues/new?template=documentation.yml) to submit an exact correction and its evidence. Hardware test claims should name the board revision, firmware, date, and test conditions.
