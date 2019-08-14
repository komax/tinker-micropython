# See https://randomnerdtutorials.com/micropython-ws2812b-addressable-rgb-leds-neopixel-esp32-esp8266/

import machine, neopixel

import time

def create_neu_pixel(pin, num_pixels):
    return NeuPixel(pin, num_pixels)

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


def warm_color_neu_pixel():
    num_pixels = 3
    pin = 2
    neupixel = create_neu_pixel(pin, num_pixels)
    # Warm color. white noise.
    neupixel.set_color(255, 147, 41)
    return neupixel


def blue_bounce_pixel():
    num_pixels = 3
    pin = 2
    neupixel = create_neu_pixel(pin, num_pixels)
    neupixel.bounce(0, 0, 255, 50)
    return neupixel


