from Clock import Clock  # The code to test
import unittest   # The test framework

class Test_Clock(unittest.TestCase):

    def setUp(self):
        self.__clock = Clock()

    def test_inc_sec_from_default_values(self):
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:00:00:01")

    def test_inc_min_from_default_values(self):
        self.__clock.inc_minute()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:00:01:00")

    def test_inc_sec_from_midnight_jan(self):
        self.__clock = Clock(31, 1, 2021, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "01:02:2021:00:00:00")
    
    def test_inc_sec_from_midnight_feb_atleapyear(self):
        self.__clock = Clock(29, 2, 2024, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:2024:00:00:00")

    def test_inc_min_from_midnight_feb_atleapyear(self):
        self.__clock = Clock(29, 2, 2024, 23, 59, 59)
        self.__clock.inc_minute()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:2024:00:00:00")

    def test_inc_hour_from_midnight_feb_atleapyear(self):
        self.__clock = Clock(29, 2, 2024, 23, 59, 59)
        self.__clock.inc_hour()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:2024:00:00:00")

    def test_inc_sec_from_midnight_feb_notatleapyear(self):
        self.__clock = Clock(28, 2, 2025, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:2025:00:00:00")

    def test_inc_hour_from_midnight_feb_notatleapyear(self):
        self.__clock = Clock(28, 2, 2025, 23, 59, 59)
        self.__clock.inc_hour()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:2025:00:00:00")

    def test_inc_min_from_midnight_feb_notatleapyear(self):
        self.__clock = Clock(28, 2, 2025, 23, 59, 59)
        self.__clock.inc_minute()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:2025:00:00:00")
    
    def test_inc_min_from_midnight_mar(self):
        self.__clock = Clock(20, 3, 2021, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "21:03:2021:00:00:00")
    
    def test_inc_hour_from_midnight_nov(self):
        self.__clock = Clock(10, 11, 2021, 23, 59, 59)
        self.__clock.inc_hour()
        self.assertEqual(self.__clock.clock_as_string(), "11:11:2021:00:00:00")

    def test_inc_day_from_jun(self):
        self.__clock = Clock(21, 6, 2021, 00, 00, 00)
        self.__clock.inc_day()
        self.assertEqual(self.__clock.clock_as_string(), "22:06:2021:00:00:00")
    
    def test_inc_month_from_jun(self):
        self.__clock = Clock(21, 6, 2021, 00, 00, 00)
        self.__clock.inc_month()
        self.assertEqual(self.__clock.clock_as_string(), "21:07:2021:00:00:00")
    
    def test_inc_month_from_des(self):
        self.__clock = Clock(1, 12, 2021, 00, 00, 00)
        self.__clock.inc_month()
        self.assertEqual(self.__clock.clock_as_string(), "01:01:2022:00:00:00")
    
    def test_inc_year_from_2024(self):
        self.__clock = Clock(10, 6, 2024, 00, 00, 00)
        self.__clock.inc_year()
        self.assertEqual(self.__clock.clock_as_string(), "10:06:2025:00:00:00")
        
    
    
    

if __name__ == '__main__':
    unittest.main()
#end of code