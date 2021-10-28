dtbo:
	dtc -I dts -O dtb -o displayhatmini-overlay.dtbo displayhatmini-overlay.dts

reload:
	dtoverlay -r displayhatmini-overlay
	dtoverlay displayhatmini-overlay.dtbo
