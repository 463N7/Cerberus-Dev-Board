# Troubleshooting

Identify the board revision and installed firmware before applying a fix. The production device, historical scanner prototype, and Arcade build use different memory and peripheral configurations.

| Symptom | Check first | Useful next step |
| --- | --- | --- |
| No USB port | Data cable, direct USB connection, serial app holding the port | Use S3 BOOT + RESET recovery and select the native S3 endpoint |
| Port disappears during installation | Bridge and native USB have different identities | Follow the installer port prompts; reinstall final S3 firmware after C5 |
| S3 stays in bridge / loader | Final application not installed or normal boot not requested | Recover S3, program the final image, then reset and confirm version |
| C5 offline | Matched S3/C5 images, C5 reset state, READY44 | Inspect protocol/version health; do not attach another output to GPIO44 |
| C5 flash fails partway | Stable supply, 115200 baud, supported bridge settings | Use the documented retry path and 4096-byte write blocks |
| Blank or wrong-color LCD | Correct ST7796 driver, SPI2 pins, backlight, panel orientation | Restore a known production firmware before changing wiring |
| Touch not detected | Shared I²C GPIO8/9, GT911 address 0x5D, INT7 | Check bus access; cold power-cycle because touch reset is not connected |
| SD unavailable | FAT32 card, full power-cycle, correct 1-bit SDMMC mode | Check GPIO35/36/37 and quad PSRAM; production does not drive GPIO38 |
| SD files corrupt or inaccessible over USB | Card ownership during USB mass-storage mode | Eject on the host before returning it to the device's file service |
| Battery shows --% | Gauge detection at 0x36 and last read error | Use the firmware battery console status; do not substitute a fake percentage |
| Charger LED is off or flashes | Actual battery and charger status | STAT is not a power LED; distinguish no charge, completion, and faults from registers |
| Expansion module fails or causes brownout | Correct profile, module side pin map, stable board supply | Add one module at a time; a USB-UART adapter may not power a multi-radio bank |
| Two SPI devices stop responding | CS states, shared bus ownership, per-device mode/clock/bit order | Verify deselection and MISO release before testing concurrent workloads |

## A helpful issue report

Include board and enclosure revision, firmware version/commit, S3 memory type, attached expansion revision, power source, exact peripheral model, steps to reproduce, expected behavior, and diagnostic output with private identifiers removed.

For physical pin questions, include a connector photo with viewing side and pin 1 marked. Do not upload main-device schematics, fabrication files, memory dumps, credentials, or captured network data to this documentation repository.

[Open a documentation or hardware-reference issue](https://github.com/463N7/Cerberus-Dev-Board/issues/new?template=documentation.yml).
