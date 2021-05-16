from quicksort import quicksort
import unittest
import random


class quicksortTest(unittest.TestCase):
    def test_integers_sort(self):
        for i, input in enumerate(range(100)):
            input = random.sample(range(0, 1000), 16)
            size = len(input) - 1
            expected = sorted(input)
            quicksort(input, 0, size)
            print("\n----------Test#:{}----------\nInput: {}\nExpected: {}\nResult: {}\n".format(
                (i + 1), input, expected, input == expected))
            self.assertEqual(input, expected)


if __name__ == "__main__":
    unittest.main()
