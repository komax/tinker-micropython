
import collections

Time = collections.namedtuple('Time', 'hour minute')


def duration_m(time_a, time_b):
    hours_delta = time_b.hour - time_a.hour
    minutes_delta = time_b.minute - time_a.minute
    if hours_delta:
        duration_minutes = hours_delta * 60 + minutes_delta
    else:
        duration_minutes = abs(minutes_delta)
    return duration_minutes


class Nightshift:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def duration_s(self):
        duration_minutes = duration_m(self.begin, self.end)
        print("duration in minutes {}".format(duration_minutes))
        return duration_minutes * 60

    def is_before(self, time):
        return time.hour < self.begin.hour or \
            (time.hour == self.begin.hour and time.minute < self.begin.minute)

    def is_within(self, time):
        if self.begin.hour < time.hour < self.end.hour:
            return True
        elif time.hour == self.begin.hour \
            and self.begin.minute <= time.minute:
            return True
        elif time.hour == self.end.hour \
            and time.minute <= self.end.minute:
            return True
        else:
            return False
    
    def is_after(self, time):
        return time.hour > self.end.hour or \
            (time.hour == self.end.hour and time.minute > self.end.minute)

    def is_at_begin(self, time, delta=Time(0,5)):
        return abs(self.begin.hour - time.hour) <= delta.hour and \
            abs(self.begin.minute - time.minute) <= delta.minute
           

    def is_at_end(self, time, delta=Time(0,5)):
        return abs(self.end.hour - time.hour) <= delta.hour and \
            abs(self.end.minute - time.minute) <= delta.minute


    def sleep_time(self, time, max_sleep=Time(0,3), min_sleep=Time(0, 1)):
        st = None
        if self.is_at_end(time) or self.is_after(time):
            duration_today = duration_m(time, Time(23, 59))
            duration_tomorrow = duration_m(Time(0, 0), self.begin)
            st = duration_today + duration_tomorrow
        elif self.is_at_begin(time) or self.is_within(time):
            # Calculate sleep time from time to end.
            st = duration_m(time, self.end)
        elif self.is_before(time):
            # Calculate sleep time between time and begin
            st = duration_m(time, self.begin)
        else:
            raise RuntimeError("{} needs to be either before, within or after the duration".format(time))

        if not st:
            st = min_sleep.hour * 60 + min_sleep.minute
            
        print("I calculated a sleeping time of {} minutes".format(st))
            
        max_sleep_minutes = max_sleep.hour * 60 + max_sleep.minute
        
        if st > max_sleep_minutes:
            st = max_sleep_minutes

    
        print("I am sleeping for {} minutes".format(st))
        return st

    def __repr__(self):
        return "Nightshift(begin={}, end={})".format(self.begin, self.end)


#ns = Nightshift(begin=Time(13,30), end=Time(15,45))
#print(ns.duration_s())
#print(ns._is_before(Time(12, 50)))
#print(ns._is_before(Time(13, 45)))