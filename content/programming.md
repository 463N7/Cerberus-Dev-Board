# Programming reference

The S3 runs application services. The onboard C5 runs a separate radio application. Their shared wire interface and protocol must agree; changing one processor's firmware can require rebuilding both.

## Reference toolchain

The recorded production Sentinel toolchain is PlatformIO Core **6.1.19**, platform **espressif32@7.0.1**, and **ESP-IDF 6.0.1** (`framework-espidf@4.60001.0`). Use the pinned configuration and dependency lock files in the firmware repository.

```powershell
# Run inside a Cerberus-Sentinel checkout.
python tools/build_sentinel.py --target s3
python tools/build_sentinel.py --target c5
python tools/build_sentinel.py --target bridge
python tools/build_sentinel.py --target all --package
```

## Memory and partitions

| Target | Reference memory profile | Application partition |
| --- | --- | --- |
| Production S3 | 16 MB flash, DIO 80 MHz; 2 MB quad PSRAM | `0x10000`, size `0x700000` in Sentinel |
| Onboard C5 | Conservative 2 MB flash budget, PSRAM disabled | `0x10000`, size `0x1F0000` in Sentinel |
| Temporary S3 bridge | Production S3 profile | Uses the S3 application slot temporarily |

These offsets belong to the referenced firmware layout, not every possible Cerberus application. Use each release's manifest and partition images when flashing. A detected 8 MB C5 does not justify changing its partition map without rebuilding and validation.

**Keep production PSRAM in quad mode.** Octal PSRAM can reserve GPIO35–37 used by microSD. DMA buffers and task stacks must follow ESP-IDF memory requirements; large optional UI buffers can explicitly request PSRAM and handle allocation failure.

## Source layout and driver entry points

| Location in Sentinel | Responsibility |
| --- | --- |
| `shared/cerberus_pins.h` | Production board signal assignments |
| `shared/cerberus_protocol.h` | Shared message definitions, framing, capabilities, versions |
| `s3_main/main/display.c` | ST7796 SPI2 display and buffered updates |
| `s3_main/main/touch.c` | GT911 input |
| `s3_main/main/i2c_bus.c` | Shared I²C0 device registration |
| `s3_main/main/battery.c` | MAX17048 sampling and cached status |
| `s3_main/main/storage.c` | SDMMC and file service |
| `s3_main/main/c5_control.c` | Inverted reset/boot control |
| `s3_main/main/c5_spi_link.c` | SPI3 master and READY handling |
| `s3_main/main/c5_flash_bridge.c` | Temporary USB/UART bridge |
| `c5_firmware/` | Onboard C5 application |

Use those driver implementations when integrating into the same firmware. Adding a second independent SPI or I²C owner over existing pins will break the shared services.

## S3/C5 protocol

The current Sentinel header identifies protocol **V2**, with V1 fallback and a capability bitmap. Ordinary framed transfers are **32 bytes** with a **22-byte payload**; event batches have a separate **64-byte** transfer form. V2 framing includes CRC validation and bounded payload handling. Use the exact structures and helpers from the matching firmware commit.

The normal READY line is **C5 GPIO11 → S3 GPIO44**. It reuses the C5 UART TX wire. Before clocking a request, the S3 waits for a queued C5 transfer; request/response timing and fallback handling belong to the link driver. The UART is not the normal runtime message path.

The legacy seven-radio scanner uses different framing and IRQ behavior. Do not treat an identical SPI pinout as protocol compatibility.

## C5 programming through the S3

The bridge temporarily occupies the S3 application slot, sets C5 boot/reset control, and forwards USB to the C5 UART at **115200 baud, 8N1**. The established path uses the esptool stub, uncompressed writes, and **4096-byte blocks**.

| Host-facing interface | USB VID:PID | Role |
| --- | --- | --- |
| Native S3 USB Serial/JTAG | `303A:1001` | Install bridge or final S3 firmware |
| Cerberus C5 flash bridge | `303A:4001` | Reach onboard C5 ROM loader |

The bridge's USB line-coding requests are firmware-specific: 2400 requests C5 ROM reset/retry, 1200 returns to S3 ROM, and 9600 returns carrier identity. They do not change the physical C5 UART rate. Use the [full bridge contract](https://github.com/463N7/Cerberus-Sentinel/blob/580c80d77e0eaa952028e65293b4b097be18c7cf/docs/C5_USB_BRIDGE.md) before writing a custom programmer. Compare device identity across port changes and always reinstall the final S3 application.

## Battery gauge integration

Use the existing shared bus at 400 kHz and MAX17048 address `0x36`. Its voltage register is `0x02`, state-of-charge register `0x04`, and version register `0x08`. Words are read most-significant byte first. The documented conversions are **78.125 µV per VCELL count** and **1/256 percent per SOC count**. See the [Analog Devices datasheet](https://www.analog.com/en/products/max17048.html).

Sentinel samples every 5 seconds, retries unavailable readings after 30 seconds, and exposes a cached read-only `battery` console command. A voltage or SOC reading is not proof of battery presence or charging. BQ25895 charging-state support is a separate charger integration; its actual configuration is not defined by the gauge driver.

## Bring-up sequence for a new application

1. Boot the correct memory profile and preserve native USB recovery.
2. Bring up LCD, shared I²C, touch, and gauge without expansion attached.
3. Initialize the C5 control pins, release reset, and validate protocol/capabilities.
4. Mount and test SD with 1-bit SDMMC; never format an existing card automatically.
5. Add one expansion device at a time with a unique select and correct bus settings.
6. Repeat after cold power-cycling, with battery power, and with all intended peripherals present.

The [examples folder](https://github.com/463N7/Cerberus-Dev-Board/tree/main/examples) contains a standalone pin header and a read-only I²C identification example. It is not a complete BSP or a claim that a new binary was tested on hardware.
