#!/usr/bin/env python3
import os
import sys
import signal
import pygame
import time
import colorsys
import math


print("""HyperPixel 2 Lots of Circles Demo

Run with: sudo SDL_FBDEV=/dev/fb1 python3 demo.py

""")


hue_to_rgb = []


for i in range(0, 255):
    hue_to_rgb.append(colorsys.hsv_to_rgb(i / 255.0, 1, 1))


# zoom tunnel
def tunnel(x, y, step):
    u_width = 32
    u_height = 32
    speed = step / 100.0
    x -= (u_width / 2)
    y -= (u_height / 2)
    xo = math.sin(step / 27.0) * 2
    yo = math.cos(step / 18.0) * 2
    x += xo
    y += yo
    if y == 0:
        if x < 0:
            angle = -(math.pi / 2)
        else:
            angle = (math.pi / 2)
    else:
        angle = math.atan(x / y)
    if y > 0:
        angle += math.pi
    angle /= 2 * math.pi  # convert angle to 0...1 range
    hyp = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    shade = hyp / 2.1
    shade = 1 if shade > 1 else shade
    angle += speed
    depth = speed + (hyp / 10)
    col1 = hue_to_rgb[step % 255]
    col1 = (col1[0] * 0.8, col1[1] * 0.8, col1[2] * 0.8)
    col2 = hue_to_rgb[step % 255]
    col2 = (col2[0] * 0.3, col2[1] * 0.3, col2[2] * 0.3)
    col = col1 if int(abs(angle * 6.0)) % 2 == 0 else col2
    td = .3 if int(abs(depth * 3.0)) % 2 == 0 else 0
    col = (col[0] + td, col[1] + td, col[2] + td)
    col = (col[0] * shade, col[1] * shade, col[2] * shade)
    return (col[0] * 255, col[1] * 255, col[2] * 255)


class DisplayHATmini:
    """Framebuffer Display HAT mini"""
    screen = None

    def __init__(self):
        self._init_display()

        self.screen.fill((0, 0, 0))
        self._updatefb()

        self._running = False

    def _exit(self, sig, frame):
        self._running = False
        print("\nExiting!...\n")

    def _init_display(self):
        os.putenv('SDL_VIDEODRIVER', 'dummy')
        pygame.display.init()  # Need to init for .convert() to work
        self.screen = pygame.Surface((320, 240))

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

    def _updatefb(self):
        fbdev = os.getenv('SDL_FBDEV', '/dev/fb1')
        with open(fbdev, 'wb') as fb:
            fb.write(self.screen.convert(16, 0).get_buffer())

    def run(self):
        self._running = True
        signal.signal(signal.SIGINT, self._exit)
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._running = False
                        break

            t = int(time.time() * 40)
            for x in range(21):
                for y in range(16):
                    r, g, b = tunnel(x, y, t)
                    r = min(255, int(r))
                    g = min(255, int(g))
                    b = min(255, int(b))
                    pygame.draw.circle(self.screen, (r, g, b), ((x * 15) + 6, (y * 15) + 6 + 7), 7)

            box_w = 320 // 6
            box_h = 240 // 4

            pygame.draw.rect(self.screen, (255, 0, 0), (0, 0, box_w, box_h))
            pygame.draw.rect(self.screen, (0, 255, 0), (box_w, 0, box_w, box_h))
            pygame.draw.rect(self.screen, (0, 0, 255), (box_w * 2, 0, box_w, box_h))

            pygame.draw.rect(self.screen, (255, 255, 0), (0, box_h, box_w, box_h))
            pygame.draw.rect(self.screen, (255, 0, 255), (box_w, box_h, box_w, box_h))
            pygame.draw.rect(self.screen, (0, 255, 255), (box_w * 2, box_h, box_w, box_h))



            self._updatefb()

        pygame.quit()
        sys.exit(0)


display = DisplayHATmini()


display.run()
