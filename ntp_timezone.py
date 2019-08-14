import utime

import ntptime


def localtime(hours_delta_utc=2):
    t = ntptime.time()
    ut = list(utime.localtime(t))
    ut[3] = ut[3] + hours_delta_utc
    return tuple(ut)

def set_time():
    tm = localtime()
    import machine
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    machine.RTC().datetime(tm)