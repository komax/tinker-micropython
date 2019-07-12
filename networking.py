import network

def connect_to_wifi(essid, password=None, ifconfig=None):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    if ifconfig and len(ifconfig) == 4:
        station.ifconfig(ifconfig)
    if password:
        station.connect(essid, password)
    else:
        station.connect(essid)
    print("Connected {} to: {}".format(station.isconnected(), station.ifconfig()))