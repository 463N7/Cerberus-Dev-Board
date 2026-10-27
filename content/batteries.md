# Batteries

Battery compatibility has two separate questions: **does it fit**, and **has it been tested electrically in this device**? A capacity label or similar-looking connector does not answer either question completely.

## Tested batteries

**No exact battery model is yet documented in this public reference.** Prior board discussions describe operation with a battery installed, and recorded firmware checks show a working MAX17048 reading. Neither record identifies a cell model, dimensions, connector polarity, charge rating, or runtime test, so neither is listed as a tested battery product.

| Model / product link | Dimensions (T × W × L) | Connector + polarity | Board / enclosure | Charge / runtime result | Status |
| --- | --- | --- | --- | --- | --- |
| Awaiting exact model record | — | — | — | — | No model-level test claim |

## Should fit — untested candidates

This section is reserved for candidates whose dimensions and connector have been compared with the actual enclosure and board. The battery cavity dimensions and connector part/polarity have not been recovered from the available records, so no product is marked “should fit” yet.

| Candidate / product link | Published size (T × W × L) | Available clearance | Connector match | Electrical checks remaining | Status |
| --- | --- | --- | --- | --- | --- |
| Awaiting cavity + connector measurements | — | — | — | Chemistry, charge voltage/current, protection | Not evaluated |

“Should fit” will mean a dimensional candidate only. It must remain in this section until charging, operation, and enclosure fit have been recorded on a named revision.

## What is known about battery support

- The onboard **MAX17048** fuel gauge is at I²C address `0x36`. It provides voltage and an estimated percentage.
- **BQ25895** is the charger identified in the earlier Cerberus board design discussion. TI documents it as a single-cell charger; its configured limits on the assembled board still need a record.
- The gauge's reading does not establish charging status. USB attachment alone does not establish charging status either.
- The charger STAT LED is a charge/fault indicator, not a general device power light. LED-off and blinking states have more than one possible cause; inspect charger status before assigning a cause.

The [MAX17048 documentation](https://www.analog.com/en/products/max17048.html) and [BQ25895 documentation](https://www.ti.com/product/BQ25895) describe the components. They do not certify a particular battery or the assembled Cerberus board's charging limits.

## A useful compatibility record

For each battery, record the manufacturer and exact SKU, product/datasheet link, chemistry/cell count, nominal and maximum charge voltage, rated capacity, allowed charge current, protection board, lead length, connector manufacturer/series/pitch, and a photo identifying positive and negative contacts.

Measure thickness, width, length, cable bend space, and installed clearance. Record board and enclosure revision, charger settings, USB source, firmware, brightness, radio workload, ambient temperature, starting charge, elapsed runtime, and the observed stop condition. Runtime estimates and completed discharge measurements belong in separate fields.

Use the [battery compatibility report](https://github.com/463N7/Cerberus-Dev-Board/issues/new?template=battery.yml). An exact model record can be added without publishing device schematics.
