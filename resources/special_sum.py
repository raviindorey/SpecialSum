from flask import request
from flask_restful import Resource

ERR_NUM_ARGS = 'Exactly 3 numbers are required'
ERR_NON_NUMERIC = 'All inputs must be numeric'
TEEN_RANGE = range(13, 20)
UNACCEPTABLE_TEENS = (15, 16)


class SpecialSum(Resource):
    @classmethod
    def put(cls):
        args = request.get_json()

        # drop square brackets
        input_list = args['input'][1:-1]

        # create list of input values
        input_list = input_list.split(',')

        """
        return error message if arguments passed are
        not equal to 3
        """
        if len(input_list) != 3:
            return {'error': ERR_NUM_ARGS}, 400

        num_list = []

        """
        coerce the numeric type of string and add to
        num_list
        return error message if wrong type is provided
        """
        for val in input_list:
            if type(val) == int or val.isnumeric():
                num_list.append(int(val))
            else:
                return {'error': ERR_NON_NUMERIC}, 400

        sum = 0

        """
        sum of all numbers in num list
        where numbers from 13 to 19 should be treated as 0
        except numbers 15 and 16
        """
        for num in num_list:
            if num in TEEN_RANGE and num not in UNACCEPTABLE_TEENS:
                num = 0
            sum += num

        return {'result': sum}
