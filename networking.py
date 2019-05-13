import network

def connect_to_wifi(essid, password, ifconfig=None):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    if ifconfig and len(ifconfig) == 4:
        station.ifconfig(ifconfig)
    station.connect(essid, password)
    print("Connected {} to: {}".format(station.isconnected(), station.ifconfig()))