import time
import unittest
import sys


class TestMock1(unittest.TestCase):
    def test_1(self):
        time.sleep(0.1)
        self.assertEqual(1 + 1, 2)
        print('my stdout')
        print('my stderr', file=sys.stderr)

    def test_2(self):
        time.sleep(0.2)
        self.assertEqual(2 + 2, 4)
        print('my stdout')
        print('my stderr', file=sys.stderr)

    def test_3(self):
        time.sleep(0.3)
        self.assertEqual(3 + 3, 6)
        print('my stdout')
        print('my stderr', file=sys.stderr)
