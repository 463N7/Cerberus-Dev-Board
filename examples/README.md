# Developer examples

- `cerberus_board_pins.h`: production signal reference; MCU GPIOs only.
- `i2c-identify/`: standalone ESP-IDF application that probes only GT911 and MAX17048 addresses and logs acknowledgment results. It does not alter charger configuration, gauge registers, or storage.

The examples are source-reviewed reference material. They have not been compiled or physically tested as part of the documentation website build. No complete board-support package is claimed.

When extending Sentinel, use its existing shared I²C bus and production pin header. Do not run the standalone bus-initialization example inside an application that already owns GPIO8/9.
