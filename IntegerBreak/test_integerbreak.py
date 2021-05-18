from main import integerBreak
import unittest


class integerBreakTest(unittest.TestCase):
    def test_integer_break(self):
        expected = [1, 1, 2, 4, 6, 9, 12, 18, 27, 36, 54, 81, 108,
                    162, 243, 324, 486, 729, 972, 1458, 2187, 2916, 4374, 6561]

        for i in range(1, 25):
            index = i - 1
            input = integerBreak(i)
            result = input == expected[index]
            print("----------Test#:{}----------\nInput: {},\tExpected: {}\nResult: {}\n".format(
                index, input, expected[index], result))
            self.assertEqual(input, expected[index])


if __name__ == "__main__":
    unittest.main()
