from machine import Pin, PWM
import time

class FadingLED:
    def __init__(self, pin_num, freq=1000):
        self.pin = Pin(pin_num, Pin.OUT)
        self.pin.off()
        self.pwm = PWM(self.pin, freq)
    
    def toggle(self, fading=False):
        if self.pin.value():
            self.pin.off()
        else:
            self.pin.on()

    def fade_on(self, ms=25):
        for i in range(512):
            time.sleep_ms(ms)
            self.pwm.duty(i)

    def fade_off(self, ms=25):
        for i in range(512, -1, -1):
            time.sleep_ms(ms)
            self.pwm.duty(i)


class TogglePins:
    def __init__(self):
        self.pins = [
            FadingLED(12),
            FadingLED(13),
            FadingLED(14)
        ]

    def _toggle_pin(self, pin):
        if pin.value():
            pin.off()
        else:
            pin.on()
        # if pin.duty():
        #     self._fade_off(pin)
        # else:
        #     self._fade_on(pin)
    


    def toggle(self, pin_number):
        if pin_number == 12:
            self.pins[0].toggle()
        elif pin_number == 13:
            self.pins[1].toggle()
        elif pin_number == 14:
            self.pins[2].toggle()

    def row_up(self, mseconds):
        time.sleep_ms(mseconds)
        self.pins[0].fade_on()
        self.pins[1].fade_on()
        time.sleep_ms(mseconds)
        self.pins[0].fade_off()
        self.pins[2].fade_on()
        time.sleep_ms(mseconds)
        self.pins[1].fade_off()
        time.sleep_ms(mseconds)
        self.pins[2].fade_off()

    
    def row_down(self, mseconds):
        time.sleep_ms(mseconds)
        self.pins[2].fade_on()
        self.pins[1].fade_on()
        time.sleep_ms(mseconds)
        self.pins[0].fade_on()
        self.pins[2].fade_off()
        time.sleep_ms(mseconds)
        self.pins[1].fade_off()
        time.sleep_ms(mseconds)
        self.pins[0].fade_off()



def kit(mseconds=300):
    t = TogglePins()
    while True:
        t.row_up(mseconds)
        t.row_down(mseconds)




def pulse(mseconds=500):
    t = TogglePins()
    while True:
        time.sleep_ms(mseconds)
        t.toggle(2)
        time.sleep_ms(mseconds)
        t.toggle(4)
        time.sleep_ms(mseconds)
        t.toggle(19)



