#include "cerberus_board_pins.h"
#include "driver/i2c_master.h"
#include "esp_check.h"
#include "esp_log.h"

/* Standalone application only. Existing Cerberus firmware must reuse its bus. */
void app_main(void)
{
    i2c_master_bus_handle_t bus = NULL;
    const i2c_master_bus_config_t config = {
        .i2c_port = I2C_NUM_0,
        .sda_io_num = CERBERUS_I2C_SDA_GPIO,
        .scl_io_num = CERBERUS_I2C_SCL_GPIO,
        .clk_source = I2C_CLK_SRC_DEFAULT,
        .glitch_ignore_cnt = 7,
        .flags.enable_internal_pullup = true,
    };
    ESP_ERROR_CHECK(i2c_new_master_bus(&config, &bus));
    const uint16_t addresses[] = {CERBERUS_TOUCH_I2C_ADDR, CERBERUS_GAUGE_I2C_ADDR};
    const char *names[] = {"GT911 touch", "MAX17048 gauge"};
    for (unsigned i = 0; i < sizeof(addresses) / sizeof(addresses[0]); ++i) {
        esp_err_t result = i2c_master_probe(bus, addresses[i], 50);
        ESP_LOGI("cerberus", "%s at 0x%02x: %s", names[i],
                 (unsigned)addresses[i], esp_err_to_name(result));
    }
    ESP_ERROR_CHECK(i2c_del_master_bus(bus));
}
