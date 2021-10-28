# Display HAT mini

Device-tree overlay for ST7789V fbdev.

:warning: This is great fun for making a simple `/dev/fb1` device that all sorts of framebuffer-compatible stuff will work with. But YMMV. It's experimental. And I think this staging driver is destined for the chopping block.

:warning: Note that Display HAT mini uses a genuinely 320x240 ST7789V2, in order to use ST7789 we set the display up as 240x320 and wish upon a star. The result is then rotated 90 degrees to give us a 320x240 landscape display. As such the *default* rotation is 90 and 270 is 180 degrees from that (landscape upside-down).

## Hey why is this in your personal GitHub and not Pimoroni?

It's experimental and bound to break. It's dangerous to go alone... but you're gonna have to learn to... fly... or something.

## Installing

:warning: You may need to update pygame for `demo.py` to work.

Edit `/boot/config.txt` and ensure it has the following line:

```
dtoverlay=spi0-1cs,cs0_pin=7,cs1_spidev=disabled
```

Then build and insert the dtoverlay to test:

```
make
sudo make reload
```

If everything looks good, install it to `/boot/overlays` with:

```
sudo make install
```

And make sure you add the following to `/boot/config.txt`:

```
dtoverlay=displayhatmini
```

(In addition to the line mentioned above!)


## Fun Things To Try

* Try `fbterm` with `FRAMEBUFFER=/dev/fb1 fbterm -r 0` (or try other rotations, hint: 0 and 2 are landscape)
* Marvel at a tiny X desktop by changing `/dev/fb0` to `/dev/fb1` in `/usr/share/X11/xorg.conf.d/99-fbturbo.conf` and running `startx` (tip: AAAAAAAAAAHHHH SO SMOL)

## Notes

Thank you to Paul of piCorePlayer for making me believe this was possible:  https://forums.slimdevices.com/showthread.php?111502-Jivelite-on-a-Pirate-Audio-240x240-screen/page33

Thank you to DRAgon715204 (if that is your real name) for giving me enough of a dtoverlay skeleton that I could tweak the rest: https://forums.raspberrypi.com/viewtopic.php?t=294784
