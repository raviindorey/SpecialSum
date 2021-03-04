import unittest
import json

from app import app
from resources.special_sum import (ERR_NON_NUMERIC, ERR_NUM_ARGS)


class TestsSpecialSum(unittest.TestCase):
    def test_accept_exactly_three_args(self):
        response = put_to_special_sum([1, 2, 3])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['result'], 6)

    def test_not_accept_less_than_three_args(self):
        response = put_to_special_sum([1, 2])
        self.assertEqual(response.get_json()['error'], ERR_NUM_ARGS)

    def test_not_accept_more_than_three_args(self):
        response = put_to_special_sum([1, 2, 3, 4])
        self.assertEqual(response.get_json()['error'], ERR_NUM_ARGS)

    def test_not_accept_non_numeric_args(self):
        response = put_to_special_sum([1, 2, 'abc'])
        self.assertEqual(
            response.get_json()['error'],
            ERR_NON_NUMERIC
        )

    def test_teens_are_zero(self):
        response = put_to_special_sum([1, 2, 13])
        self.assertEqual(response.get_json()['result'], 3)

    def test_teens_are_exclusive_of_fifteen_and_sixteen(self):
        response = put_to_special_sum([1, 2, 15])
        self.assertEqual(18, response.get_json()['result'])
        response = put_to_special_sum([1, 2, 16])
        self.assertEqual(19, response.get_json()['result'])


def put_to_special_sum(num_list):
    num_list = str(num_list)
    num_list = num_list.replace(' ', '')
    payload = json.dumps({'input': num_list})

    client = app.test_client()

    return client.put(
        '/sum',
        headers={'Content-Type': 'application/json'},
        data=payload
    )
