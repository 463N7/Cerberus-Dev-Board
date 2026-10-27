# Developer examples

- `cerberus_board_pins.h`: Cerberus signal reference; MCU GPIOs only.
- `i2c-identify/`: standalone ESP-IDF application that probes only GT911 and MAX17048 addresses and logs acknowledgment results. It does not alter charger configuration, gauge registers, or storage.

The standalone I²C example is awaiting compilation and hardware testing.

When extending Sentinel, use its existing shared I²C bus and Cerberus pin header. Do not run the standalone bus-initialization example inside an application that already owns GPIO8/9.
