import network

def connect_to_wifi(essid, password=None, ifconfig=None, verbose=True):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    if not station.isconnected():
        if ifconfig and len(ifconfig) == 4:
            station.ifconfig(ifconfig)
        if password:
            station.connect(essid, password)
        else:
            station.connect(essid)
        while not station.isconnected():
            pass
    if verbose:
        print("Connected {} to: {}".format(station.isconnected(), station.ifconfig()))
