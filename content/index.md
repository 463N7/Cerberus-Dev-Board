# Build with Cerberus.

One handheld. Two processors. A practical reference for writing firmware, connecting peripherals, and creating expansion boards.

<div class="hero-actions"><a class="button" href="getting-started.html">Start developing <span aria-hidden="true">↗</span></a><a class="button secondary" href="pinouts.html">Explore the pinouts</a></div>

<div class="stats"><div><strong>ESP32-S3</strong><span>Application + interface</span></div><div><strong>ESP32-C5</strong><span>Dual-band radio coprocessor</span></div><div><strong>320 × 480</strong><span>ST7796 + GT911 touch</span></div><div><strong>16 MB / 2 MB</strong><span>Production S3 flash / PSRAM</span></div></div>

## The device, documented.

Cerberus pairs a touchscreen application processor with an independently programmable radio processor. The S3 handles the display, touch, storage, USB, and user interface. The C5 handles radio work and exchanges structured messages over SPI. Different firmware can make use of the same hardware.

<div class="architecture" aria-label="Cerberus system overview"><div class="arch-peripherals">Display · Touch · microSD · USB · Battery gauge</div><div class="arch-main"><span>APPLICATION PROCESSOR</span><strong>ESP32-S3</strong><small>SPI2 display / SDMMC storage / shared I²C</small></div><div class="arch-link">SPI3 data + READY <span>UART for programming</span></div><div class="arch-radio"><span>RADIO COPROCESSOR</span><strong>ESP32-C5</strong><small>2.4 / 5 GHz Wi-Fi · Bluetooth LE · 802.15.4</small></div></div>

## Find what you need

<div class="guide-grid"><a href="pinouts.html"><span>01 / HARDWARE</span><h3>Every built-in connection</h3><p>GPIO tables, bus ownership, I²C addresses, and the S3-to-C5 link.</p></a><a href="programming.html"><span>02 / FIRMWARE</span><h3>Program both processors</h3><p>Production memory settings, toolchain, protocol, and first-build checks.</p></a><a href="expansion.html"><span>03 / EXPANSION</span><h3>Make room for more</h3><p>Six-radio expansion, peripheral plans, and a dedicated KiCad file area.</p></a><a href="batteries.html"><span>04 / COMPATIBILITY</span><h3>Power it with confidence</h3><p>Tested batteries and dimensional candidates kept in separate lists.</p></a><a href="antennas.html"><span>05 / RF</span><h3>Match the right antenna</h3><p>Band coverage, connectors, cables, and repeatable test records.</p></a><a href="troubleshooting.html"><span>06 / SUPPORT</span><h3>Get back to building</h3><p>USB recovery and checks for C5, display, SD, and battery readings.</p></a></div>

## Know your hardware revision

The baseline here is the production **N16R2** device with one onboard C5 and **1-bit SDMMC**. The six-C5 expansion and Arcade wiring are separate configurations. GPS and RF/NFC add-ons are expansion features, not built-in parts of the base device.

Each guide distinguishes source-confirmed mappings, recorded hardware tests, and plans. Battery model validation, exact antenna connector part numbers, and an as-built expansion-header orientation still need records before they can be presented as confirmed compatibility. See [revisions and evidence](revisions.md).

<div class="callout"><strong>A developer reference without device schematics.</strong><p>Pin assignments, software interfaces, and expansion information are published here. Cerberus main-board design files are excluded.</p></div>
