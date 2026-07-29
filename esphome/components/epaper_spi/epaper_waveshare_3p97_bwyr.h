#pragma once

#include "epaper_spi.h"

namespace esphome::epaper_spi {

class EPaperWaveshare3P97InBWYR final : public EPaperBase {
 public:
  EPaperWaveshare3P97InBWYR(const char *name, uint16_t width, uint16_t height, const uint8_t *init_sequence,
                            size_t init_sequence_length)
      : EPaperBase(name, width, height, init_sequence, init_sequence_length, DISPLAY_TYPE_COLOR) {
    this->row_width_ = (width + 3) / 4;
    this->buffer_length_ = this->row_width_ * height;
  }

  void fill(Color color) override;

 protected:
  void draw_pixel_at(int x, int y, Color color) override;
  bool reset() override;
  bool initialise(bool partial) override;
  bool should_wait_for_state_(EPaperState state) const override {
    return state != EPaperState::INITIALISE && EPaperBase::should_wait_for_state_(state);
  }
  bool transfer_data() override;
  void power_on() override {}
  void refresh_screen(bool partial) override;
  void power_off() override;
  void deep_sleep() override;

  enum class Step : uint8_t {
    NONE,
    RESET_HIGH,
    RESET_LOW,
    RESET_SETTLE,
    INIT_SEQUENCE,
    INIT_SETTLE,
    POWER_ON,
    POWER_ON_WAIT,
    POWER_ON_SETTLE,
    INIT_DONE,
  };

  Step step_{Step::NONE};
};

}  // namespace esphome::epaper_spi
