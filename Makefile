dtbo:
	dtc -q -I dts -O dtb -o displayhatmini-overlay.dtbo displayhatmini-overlay.dts

reload:
	dtoverlay -r displayhatmini-overlay
	dtoverlay displayhatmini-overlay.dtbo

install: dtbo
	@cp displayhatmini-overlay.dtbo /boot/overlays/displayhatmini.dtbo
	@echo "Done!"
	@echo "Now add the following to /boot/config.txt:"
	@echo ""
	@echo "dtoverlay=spi0-1cs,cs0_pin=7,cs1_spidev=disabled"
	@echo "dtoverlay=displayhatmini"
	@echo ""
