import unittest
from nightshift import Nightshift, Time

class NightshiftTest(unittest.TestCase):

    def setUp(self):
        self.ns = Nightshift(begin=Time(13,30), end=Time(15,45))

    def test_duration_equals_135_minutes(self):
        self.assertEqual(135 * 60, self.ns.duration_s())

    def test_within_yields_true(self):
        self.assertTrue(self.ns.is_within(Time(14,5)))

    def test_within_before_yields_false(self):
        self.assertFalse(self.ns.is_within(Time(13, 14)))

    def test_within_yields_true_for_start_time(self):
        self.assertTrue(self.ns.is_within(Time(13,30)))

    def test_within_yields_true_for_end_time(self):
        self.assertTrue(self.ns.is_within(Time(15,45)))

    def test_within_yields_false(self):
        self.assertFalse(self.ns.is_within(Time(15,55)))


class SleeptimeTest(unittest.TestCase):

    def setUp(self):
        self.ns = Nightshift(begin=Time(13,30), end=Time(15,45))

    def test_sleep_time_before_20m(self):
        self.assertEqual(20, self.ns.sleep_time(Time(13, 10), max_sleep=Time(10, 0)))

    def test_sleep_time_for_start_time(self):
        self.assertEqual(135, self.ns.sleep_time(self.ns.begin, max_sleep=Time(10, 0)))

    def test_sleep_time_for_time_during_nightshift(self):
        self.assertEqual(90, self.ns.sleep_time(Time(14, 15), max_sleep=Time(10, 0)))

    def test_sleep_time_for_end_time(self):
        self.assertEqual(45 + 21 * 60 - 1, self.ns.sleep_time(Time(15, 45), max_sleep=Time(100, 0)))


if __name__ == '__main__':
    unittest.main()