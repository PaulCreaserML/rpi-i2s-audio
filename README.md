# rpi-i2s-audio

## my_loader

This is an old school kernel module for I2S, specifically for a mono MEMs microphone. However overlays are now used.

## rpi-i2s-mic.dts

This is the overlay for a MEMs microphone, specifically the SPH0645 I2C MIC.

### Compile

dtc  -I dts -O dtb -o rpi-i2s-mic.dtbo  rpi-i2s-mic.dts

sudo cp rpi-i2s-mic.dtbo  /boot/overlays/.

Remember to add the overlay to the config.txt file.

dtoverlay=rpi-i2s-mic

### ADAFRUIT SPH0645

  - 3.3V Connector Pin 1
  - GND   Connector Pin 39
  - LRCL  Connector Pin 35 GPIO 19
  - DOUT  Connector Pin 37 GPIO 20
  - BCLK  Connector Pin 12 GPIO 18
  - SEL   Connector Pin 17 3.3V

## i2s_audio_read_test.py

Simple demo application for recording audio from I2S mems mic

# Warning

After looking at the raw data via python using the sounddevice module, it seems there is a dc offset in the output data. Subtracting the mean or high pass filtering can be used to remove thia offset. During playback you will hearma pop or click when audio playback starts or finishes.
