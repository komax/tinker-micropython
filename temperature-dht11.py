import dht
import machine
import time


class DHTClient:
    def __init__(self, pin_number):
        self.dht = dht.DHT11(machine.Pin(pin_number))
        self.dht.measure()

    def report_th(self, freq_sec=10):
        while True:
            self.dht.measure()
            print("Temp: {0} C and humidity {1}".format(self.dht.temperature(), self.dht.humidity()))
            time.sleep(freq_sec)

dht = DHTClient(pin_number=15)