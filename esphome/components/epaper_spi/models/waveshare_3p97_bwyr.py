import esphome.config_validation as cv
from esphome.const import CONF_BUSY_PIN, CONF_INIT_SEQUENCE

from . import EpaperModel


class Waveshare3P97InBWYR(EpaperModel):
    def option(self, name, fallback=cv.UNDEFINED) -> cv.Optional | cv.Required:
        if name == CONF_BUSY_PIN:
            return cv.Required(name)
        return super().option(name, fallback)

    def validate_config(self, config: dict) -> dict:
        if CONF_INIT_SEQUENCE in config:
            raise cv.Invalid("init_sequence cannot be overridden for this model")
        return config


# Vendor init derived from the Waveshare 3.97inch e-Paper HAT+ (G) sample.
# The 0x61 payload is deliberately 800x680; it must not be derived from the
# logical 800x480 display dimensions.
Waveshare3P97InBWYR(
    "waveshare-3.97in-bwyr",
    "EPaperWaveshare3P97InBWYR",
    width=800,
    height=480,
    minimum_update_interval="30s",
    data_rate="10MHz",
    initsequence=(
        (0x00, 0x2B, 0x29),
        (0x06, 0x0F, 0x8B, 0x93, 0xC1),
        (0x50, 0x37),
        (0x30, 0x08),
        (0x61, 0x03, 0x20, 0x02, 0xA8),
        (0x62, 0x76, 0x76, 0x76, 0x5A, 0x9D, 0x8A, 0x76, 0x62),
        (0x65, 0x00, 0x00, 0x00, 0x00),
        (0xE0, 0x10),
        (0xE7, 0xA4),
        (0xE9, 0x01),
        (0xEF, 0x01),
        (0xF6, 0x20),
        (0xEF, 0x00),
        (0xE0, 0x12),
        (0xE6, 92),
        (0xA5, 0x00),
    ),
)
