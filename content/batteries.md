# Batteries

Four battery packs have been tested with Cerberus. The list below identifies the tested packs by their printed labels and the reference photo.

## Tested batteries

**All four packs below are confirmed tested with Cerberus.** Voltage and capacity figures are the ratings printed on each pack.

| Battery / printed label | Nominal voltage | Labeled capacity | Identification in photo |
| --- | --- | --- | --- |
| PL 606090 pouch | 3.7 V | 4000 mAh | Top; shown installed in the Cerberus enclosure |
| PL 505573 pouch | 3.7 V | 2500 mAh | Lower left |
| PL 695084 pouch | 3.7 V | 3200 mAh | Lower right; additional marking `2803` |
| BATMAX BT-PS3 — PS3 DualShock 3 replacement battery | 3.7 V | 1800 mAh / 6.66 Wh | Small black pack |

The BATMAX label lists replacement references **LIP1359, LIP1859, and LIP1427**, with controller compatibility **CECHZC2E / CECHZC2U**. The pouch packs are identified by their printed PL codes; their manufacturer is not listed.

<details class="connector-photo"><summary>View the tested battery photo</summary><figure><a href="assets/tested-batteries.jpg"><img src="assets/tested-batteries.jpg" alt="Four tested Cerberus batteries: PL 606090 4000 mAh installed at the top, PL 505573 2500 mAh at lower left, PL 695084 3200 mAh at lower right, and a black BATMAX BT-PS3 1800 mAh PS3 DualShock 3 replacement pack." width="4590" height="8160" loading="lazy"></a><figcaption>Tested packs and their printed labels. Select the photo to view it at full size.</figcaption></figure></details>

Measured dimensions, connector series and pin order, charger settings, measured capacity, and runtime are not yet recorded here. The pouch codes are identifiers, not measured dimensions. Only the 4000 mAh pack is shown installed in this photo.

## Should fit — untested candidates

No untested candidates are listed yet. Add a pack here once its dimensions and connector have been compared with the actual enclosure and board.

| Candidate / product link | Published size (T × W × L) | Available clearance | Connector match | Electrical checks remaining | Status |
| --- | --- | --- | --- | --- | --- |
| Awaiting cavity + connector measurements | — | — | — | Chemistry, charge voltage/current, protection | Not evaluated |

“Should fit” will mean a dimensional candidate only. It must remain in this section until charging, operation, and enclosure fit have been recorded on a named revision.

## What is known about battery support

- The onboard **MAX17048** fuel gauge is at I²C address `0x36`. It provides voltage and an estimated percentage.
- The **BQ25895** charger shares I²C0: SDA GPIO8, SCL GPIO9, address `0x6A`. Its configured charge limits are not yet listed here.
- The gauge's reading does not establish charging status. USB attachment alone does not establish charging status either.
- The charger STAT LED is a charge/fault indicator, not a general device power light. LED-off and blinking states have more than one possible cause; inspect charger status before assigning a cause.

The [MAX17048 documentation](https://www.analog.com/en/products/max17048.html) and [BQ25895 documentation](https://www.ti.com/product/BQ25895) describe the components. They do not certify a particular battery or the assembled Cerberus board's charging limits.

## A useful compatibility record

For each battery, record the manufacturer and exact SKU, product/datasheet link, chemistry/cell count, nominal and maximum charge voltage, rated capacity, allowed charge current, protection board, lead length, connector manufacturer/series/pitch, and a photo identifying positive and negative contacts.

Measure thickness, width, length, cable bend space, and installed clearance. Record board and enclosure revision, charger settings, USB source, firmware, brightness, radio workload, ambient temperature, starting charge, elapsed runtime, and the observed stop condition. Runtime estimates and completed discharge measurements belong in separate fields.

Use the [battery compatibility report](https://github.com/463N7/Cerberus-Dev-Board/issues/new?template=battery.yml). An exact model record can be added without publishing device schematics.
