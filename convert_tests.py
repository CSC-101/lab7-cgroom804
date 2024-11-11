import unittest

from convert import str_to_float


class TestCases(unittest.TestCase):
    pass

    # Part 1
    def test_str_to_float1(self):
        self.assertEqual(str_to_float("5"), 5.0)

    def test_str_to_float2(self):
        self.assertEqual(str_to_float("xyz"), None)

    # Part 2


if __name__ == '__main__':
    unittest.main()