import unittest

class TestBasic(unittest.TestCase):

    def test_one_equals_true(self):
        self.assertEqual(True, 1)

    def test_true_one_is_not_true(self):
        self.assertFalse(1 is True)


if __name__ == "__main__":
    unittest.main()