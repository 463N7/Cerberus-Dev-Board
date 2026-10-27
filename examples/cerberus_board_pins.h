#pragma once

/* Production N16R2 signal assignments. These are MCU GPIOs, not header positions.
 * Source baseline: Cerberus-Sentinel 580c80d (2026-10-27).
 * 3.3 V logic. Production storage is 1-bit SDMMC; PSRAM is quad.
 */
#define CERBERUS_I2C_SDA_GPIO 8
#define CERBERUS_I2C_SCL_GPIO 9
#define CERBERUS_TOUCH_INT_GPIO 7
#define CERBERUS_TOUCH_RST_GPIO (-1)
#define CERBERUS_TOUCH_I2C_ADDR 0x5D
#define CERBERUS_GAUGE_I2C_ADDR 0x36

#define CERBERUS_LCD_DC_GPIO 4
#define CERBERUS_LCD_RST_GPIO 5
#define CERBERUS_LCD_BL_GPIO 6
#define CERBERUS_LCD_CS_GPIO 16
#define CERBERUS_LCD_SCLK_GPIO 17
#define CERBERUS_LCD_MOSI_GPIO 18

#define CERBERUS_SD_D0_GPIO 35
#define CERBERUS_SD_CLK_GPIO 36
#define CERBERUS_SD_CMD_GPIO 37
/* Production DAT3 is held by the board's pull-up network. Do not drive GPIO38. */
#define CERBERUS_SD_DAT3_TEST_GPIO (-1)

#define CERBERUS_ONBOARD_C5_SPI_CS_GPIO 10
#define CERBERUS_ONBOARD_C5_SPI_MOSI_GPIO 11
#define CERBERUS_ONBOARD_C5_SPI_SCLK_GPIO 12
#define CERBERUS_ONBOARD_C5_SPI_MISO_GPIO 13
#define CERBERUS_ONBOARD_C5_READY_GPIO 44
#define CERBERUS_C5_UART_TX_GPIO 43
#define CERBERUS_C5_UART_RX_GPIO 44
#define CERBERUS_C5_UART_BAUD 115200
/* These signals pass through inverting control circuitry. */
#define CERBERUS_C5_EN_GPIO 21
#define CERBERUS_C5_BOOT_GPIO 40

/* Onboard C5-side SPI and READY assignments; do not use as S3 GPIOs. */
#define CERBERUS_C5_SLAVE_SPI_CS_GPIO 8
#define CERBERUS_C5_SLAVE_SPI_MOSI_GPIO 5
#define CERBERUS_C5_SLAVE_SPI_SCLK_GPIO 4
#define CERBERUS_C5_SLAVE_SPI_MISO_GPIO 6
#define CERBERUS_C5_READY_GPIO 11

#define CERBERUS_USB_DM_GPIO 19
#define CERBERUS_USB_DP_GPIO 20

/* No generic expansion header order or "free GPIO" list is implied here. */
