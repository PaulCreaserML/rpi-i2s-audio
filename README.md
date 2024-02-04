# rpi-i2s-audio

## my_loader

This is an old school kernel module for I2S, specifically for a mono MEMs microphone. However overlays are now used.

## rpi-i2s-mic.dts

This is the overlay for a MEMs microphone, specifically the SPH0645 I2C MIC.

dtc  -I dts -O dtb -o rpi-i2s-mic.dtbo  rpi-i2s-mic.dts
sudo cp rpi-i2s-mic.dtbo  /boot/overlays/.

Remember to add the overlay to the config.txt file.


