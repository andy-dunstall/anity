import time
import unittest
import sys


class TestMock2(unittest.TestCase):
    def test_1(self):
        time.sleep(0.1)
        self.assertEqual(1 + 1, 4)

    def test_2(self):
        time.sleep(0.2)
        # Syntax error to fail test.
        skdlfj
        self.assertEqual(2 + 2, 4)

    def test_3(self):
        time.sleep(0.3)
        print('my stdout')
        print('my stderr', file=sys.stderr)
        self.assertEqual(3 + 3, 6)
