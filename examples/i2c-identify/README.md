# Identify the shared I²C devices

Standalone **ESP-IDF 6.0.1** example for Cerberus N16R2. Build it in an ESP-IDF environment with the S3 target:

```powershell
idf.py set-target esp32s3
idf.py build
```

Flashing this replaces the installed S3 application. Preserve your recovery image and use the correct device port if you choose to flash it. It does not program the C5 or demonstrate display/touch operation.

Expected log outcomes are an acknowledgment or an unavailable-address report for GT911 at `0x5D` and MAX17048 at `0x36`. An ACK identifies a responding address, not the device's model or health. GT911 power-on behavior may depend on the previously initialized state because its hardware reset is not connected.

This example has not been physically tested. For a complete verified application, use the linked Cerberus firmware and its built-in diagnostics.
