# Start developing

Start with the production N16R2 board profile, a USB data cable, and a known firmware release. Keep the onboard S3 and C5 images from the same release.

## 1. Identify your device

Record the board revision, S3 memory suffix, installed expansion board, and firmware version. The production reference has 16 MB S3 flash and 2 MB quad PSRAM. The C5 memory baseline is WROOM N4: **4 MB flash and no PSRAM**. An S3 R8 development profile is a different target.

The device is independently programmable on both processors. The USB connection reaches the S3. A temporary S3 bridge exposes the onboard C5 for programming through that same connector.

## 2. Install a working baseline

Open the [Cerberus USB Installer](https://463n7.github.io/Cerberus-Flasher/) in a supported desktop browser and follow its S3 bridge → C5 → final S3 sequence. The final S3 application must be installed and verified before the device is ready to use. The [installer repository](https://github.com/463N7/Cerberus-Flasher) contains maintenance information.

Use a data-capable USB cable. Close applications that hold the serial port. The port can change when the bridge appears or the S3 returns to its ROM downloader.

## 3. Get the firmware source

The public [Cerberus Sentinel repository](https://github.com/463N7/Cerberus-Sentinel) provides a working production implementation of display, touch, battery status, SD, USB, and the S3/C5 link. This Dev Board repository contains reference material and small examples; it is not a complete firmware image.

```powershell
git clone https://github.com/463N7/Cerberus-Sentinel.git
cd Cerberus-Sentinel
python -m pip install platformio==6.1.19
python tools/build_sentinel.py --target all --package
```

These build commands do not program your device. Consult the firmware repository's [build and recovery guide](https://github.com/463N7/Cerberus-Sentinel/blob/main/docs/SENTINEL_BUILD.md) for its current release workflow. See [programming](programming.md) for memory and driver constraints.

## 4. Confirm the built-in features

- S3 boots and reports the expected version and memory.
- LCD orientation, colors, and backlight are correct; touch works at each corner.
- Onboard C5 is online with the matched protocol/firmware version.
- A known FAT32 card mounts and passes a controlled file read/write test.
- Battery voltage and percentage are plausible, or the unavailable state is shown clearly.
- USB remains usable after resetting and cold power-cycling.

Begin expansion work only after these baseline checks pass. Keep a recovery image and record the original pin assignments.

## Recover the S3 USB connection

1. Hold the board's **S3 BOOT** control.
2. Tap **RESET** while keeping BOOT held.
3. Release BOOT, select the native S3 USB port, and reinstall the final S3 firmware.
4. Reset or power-cycle into the application and confirm its version.

This recovery path is documented for Cerberus. Physical board controls must be identified on your actual revision; their positions are not inferred from a generic ESP32 development board.

## Next steps

Use the [built-in pinouts](pinouts.md), choose an [expansion profile](expansion.md), and work through the [programming guide](programming.md). Record hardware results using the compatibility-report forms linked from the repository.
