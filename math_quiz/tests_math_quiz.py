import unittest
from math_quiz import randfunc_randint, randfunc_randoperator, func_eval_jumble


class TestMathGame(unittest.TestCase):

    def test_randfunc_randint(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randfunc_randint(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_randfunc_randoperator(self):
        # Test if the random operator is one of the expected operators
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = randfunc_randoperator()
            self.assertIn(operator, valid_operators)

    def test_func_eval_jumble(self):
        # Test if the function returns the correct problem and answer
            test_cases = [
                (5, 2, '+', '5 + 2', 3),
                (5, 2, '-', '5 - 2', 7),
                (5, 2, '*', '5 * 2', 10),
                (10, 5, '+', '10 + 5', 5),
                (10, 5, '-', '10 - 5', 15),
                (10, 5, '*', '10 * 5', 50)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = func_eval_jumble(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
