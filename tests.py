#!usr/bin/env python3

import unittest
from io import StringIO
from unittest.mock import patch

from app import (
    special_sum,
    ERR_NUM_ARGS,
    ERR_NON_NUMERIC,
)


class TestSpecialSum(unittest.TestCase):
    def test_accept_exactly_three_args(self):
        args = [1, 2, 3]
        self.assertEqual(get_terminal_response(args), str(6))

    def test_not_accept_less_than_three_args(self):
        args = [1, 2]
        self.assertEqual(get_terminal_response(args), ERR_NUM_ARGS)

    def test_not_accept_more_than_three_args(self):
        args = [1, 2, 3, 4]
        self.assertEqual(get_terminal_response(args), ERR_NUM_ARGS)

    def test_not_accept_non_numeric_args(self):
        args = [1, 2, 'abc']
        self.assertEqual(
            get_terminal_response(args),
            ERR_NON_NUMERIC
        )

    def test_teens_are_zero(self):
        args = [1, 2, 13]
        self.assertEqual(get_terminal_response(args), str(3))

    def test_teens_are_exclusive_of_fifteen_and_sixteen(self):
        args = [1, 2, 15]
        self.assertIn(str(18), get_terminal_response(args))
        args = [1, 2, 16]
        self.assertIn(str(19), get_terminal_response(args))


def get_terminal_response(args_list):
    with patch('sys.stdout', new=StringIO()) as sudo_stdout:
        special_sum(args_list)
        return sudo_stdout.getvalue().strip()


if __name__ == '__main__':
    unittest.main()
