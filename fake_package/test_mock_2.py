import time
import unittest


class TestMock2(unittest.TestCase):
    def test_1(self):
        time.sleep(0.1)
        self.assertEqual(1 + 1, 4)

    def test_2(self):
        time.sleep(0.2)
        skdlfj
        self.assertEqual(2 + 2, 4)

    def test_3(self):
        time.sleep(0.3)
        self.assertEqual(3 + 3, 6)
