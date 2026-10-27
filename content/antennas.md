# Antennas

Match an antenna to the **specific radio and connector**, then record how it performs in the intended enclosure. The C5, nRF24/E01, CC1101/E07, and GNSS are different antenna applications.

## Choose by radio

| Radio / configuration | Frequency coverage to check | Connector / integration status |
| --- | --- | --- |
| Onboard ESP32-C5 | 2.4 GHz and 5 GHz for dual-band Wi-Fi; 2.4 GHz for BLE/802.15.4 | Exact installed module/antenna connector part requires confirmation |
| S3 native radio, if used | 2.4 GHz | Depends on fitted S3 module and its antenna arrangement |
| nRF24 / E01 expansion | 2.4 GHz; match the exact module's RF specifications | Optional expansion; exact connector and module suffix must be recorded |
| E07 / CC1101 expansion | Match populated module and selected band, such as 433 or 915 MHz | A 433 MHz module and 915 MHz module are separate compatibility records |
| Quectel LC29HAAMD GNSS plan | Dual-band L1/L5 | Planning only; active/passive antenna power and connector remain board-specific |

The C5's dual-band Wi-Fi capability is documented by [Espressif](https://www.espressif.com/en/products/socs/esp32-c5). It does not make a single-band antenna dual-band. Do not infer connector mating from the seller's “IPEX” wording; confirm the exact RF connector family and the SMA/RP-SMA contact arrangement where applicable.

## Tested antennas

| Exact antenna model | Radio + band | Connector / cable | Board / enclosure | Test result | Status |
| --- | --- | --- | --- | --- | --- |
| Awaiting model-level test record | — | — | — | — | No tested product claim |

## Previously discussed candidates

| Candidate | Intended application | Evidence status |
| --- | --- | --- |
| Ebyte TX2400-JZ-3 | Compact 2.4 GHz nRF24/E01 antenna | Discussed candidate; exact version, connector, enclosure fit, and performance not verified here |
| Taoglas compact antenna | Compact nRF24/E01 form factor | Brand preference recorded; exact model not identified |
| Bolton DART | Compact nRF24/E01 form factor | Candidate preference recorded; exact model/connector not identified |

These are recovered planning candidates, not purchasing recommendations or tested substitutes. No current price, stock, or delivery claim is made.

## Installation and comparison records

Record antenna part number, manufacturer datasheet, band, nominal impedance, connector, cable type/length, mounting location, keep-out/ground-plane requirements, and enclosure revision. For an active GNSS antenna, additionally record its permitted supply voltage/current and whether the expansion board supplies antenna bias.

Compare with the same Cerberus board, firmware, radio settings, antenna orientation, location, reference source, and test duration. Save observations separately for each band. RSSI alone is not an antenna-gain measurement, and a single reception result does not establish range or full-band performance.

Use the [antenna compatibility report](https://github.com/463N7/Cerberus-Dev-Board/issues/new?template=antenna.yml). A simple installed photo and exact part number are useful first additions.
