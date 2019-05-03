import unittest
import numpy as np
from plotxel import smart_ticks, smart_limits

class TestSmartTicks(unittest.TestCase):

    def test_simple(self):
        a = smart_ticks([1, 2, 3, 4], [2, 3])
        a = [round(i, 1) for i in a]
        self.assertEqual([1.8, 2.0, 2.2, 2.4, 2.6, 2.8], a)

    def test_100(self):
        data = np.random.rand()



class TestSmartLimits(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(4, 4)

if __name__ == '__main__':
    unittest.main()