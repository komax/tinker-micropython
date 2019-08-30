import machine
import utime

from nightshift import Time, Nightshift
import neupixel

def localtime2time():
    current_time = utime.localtime()
    return Time(hour=current_time[3], minute=current_time[4])


if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print("I woke from a deep sleep")


white_noise_color = 255, 147, 41


pixel = neupixel.create_neupixel(pin=16, num_pixels=3)


def light_up(duration):
    pixel.set_color(*white_noise_color)
    utime.sleep(duration)
    pixel.clear()

ns = Nightshift(begin=Time(18, 21), end=Time(22, 15))
print("Nightshift(begin={}, end={})".format(ns.begin, ns.end))


print("Localtime: {}".format(utime.localtime()))
current_time = localtime2time()

if ns.is_at_end(current_time, delta=Time(0, 20)):
    print("I am at the end of the nighttime... clearing neopixel")
    pixel.clear()
elif ns.is_at_begin(current_time) or ns.is_within(current_time):
    print("I set neopixel with {}".format(white_noise_color))
    # Within night shift, light up
    pixel.set_color(*white_noise_color)
else:
    print("Clearing neopixel's color")
    # Otherwise don't show anything.
    pixel.clear()
# Calculate the sleep time.
sleeptime = ns.sleep_time(current_time, min_sleep=Time(0, 45), max_sleep=Time(8, 0))
print("I am going to sleep for {}".format(sleeptime))
#utime.sleep(60 * sleeptime)
machine.deepsleep(1_000 * 60 * sleeptime)

