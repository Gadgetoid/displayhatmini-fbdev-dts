# Display HAT mini

Device-tree overlay for ST7789V fbdev.

:warning: Note that Display HAT mini uses a genuinely 320x240 ST7789V2, in order to use ST7789 we set the display up as 240x320 and wish upon a star. As such, demo.py renders into a 320x240 canvas and manually rotates it using `pygame.transform.rotate`.

## Installing

:warning: You may need to update pygame

Edit `/boot/config.txt` and ensure it has the following line:

```
dtoverlay=spi0-1cs,cs0_pin=7,cs1_spidev=disabled
```

Then build and insert the dtoverlay:

```
make
sudo make reload
```

## Notes

Thank you to Paul of piCorePlayer for making me believe this was possible:  https://forums.slimdevices.com/showthread.php?111502-Jivelite-on-a-Pirate-Audio-240x240-screen/page33

Thank you to DRAgon715204 (if that is your real name) for giving me enough of a dtoverlay skeleton that I could tweak the rest: https://forums.raspberrypi.com/viewtopic.php?t=294784
