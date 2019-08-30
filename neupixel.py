# See https://randomnerdtutorials.com/micropython-ws2812b-addressable-rgb-leds-neopixel-esp32-esp8266/

import machine, neopixel

import time

def create_neupixel(pin, num_pixels, color=(255, 255, 255)):
    np  = NeuPixel(pin, num_pixels)
    np.set_color(*color)
    return np

class NeuPixel:
    def __init__(self, pin, num_pixels):
        pin = machine.Pin(pin)
        self.np = neopixel.NeoPixel(pin, num_pixels)
        self.num_pixels = num_pixels

    def clear(self):
        for i in range(self.num_pixels):
            self.np[i] = (0, 0, 0)
        self.np.write()

    def set_color(self, r, g, b):
        for i in range(self.num_pixels):
            self.np[i] = (r, g, b)
        self.np.write()

    def bounce(self, r, g, b, wait):
        for i in range(4 *  self.num_pixels):
            for j in range(self.num_pixels):
                self.np[j] = r, g, b
            if (i // self.num_pixels) % 2 == 0:
                self.np[i % self.num_pixels] = 0, 0, 0
            else:
                self.np[self.num_pixels - 1 - (i % self.num_pixels)] = 0, 0, 0
            self.np.write()
            time.sleep_ms(wait)


def warm_color_neupixel(num_pixels, pin):
    # Warm color. white noise.
    color = (255, 147, 41)
    return create_neupixel(num_pixels, pin, color)


def blue_bounce_pixel(num_pixels, pin, color=(0, 0, 255), bounce_time=50):
    np = create_neupixel(num_pixels, pin)
    np.bounce(*color, bounce_time)
    return np


