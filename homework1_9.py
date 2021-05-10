#Задание 1

import unittest

def calculate_average_velocity(*args):
	velocity_sum = 0
	for i in args:
		try:
			velocity_sum += i
		except TypeError:
			continue
	return velocity_sum / len(args)

a = calculate_average_velocity(1,2,3,4)
print(a)


class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(calculate_average_velocity(4,7), 5.5)
unittest.main()


#Задание 3

import unittest


def ordinary_case(input_data):
    time_data = {}
    try:
        if input_data == dict(input_data):
            for i, b in input_data.items():
                add_list = []
                add = 0
                count = 0
                for f in b:
                    try:
                        add += f
                    except TypeError:
                        raise ValueError
                    count += 1
                try:
                    add /= count
                except ZeroDivisionError:
                    add = 0
                i = f"{i}'s rating"
                time_data.update({i : add})
                input_data = time_data
            return time_data
    except TypeError:
        raise ValueError







class TestMyFunction(unittest.TestCase):
    def test_ordinary_case(self):
        input_data = {'JD': [13, 89, 32, 55],
                'Turk': [5, 32, 57, 39],
                'Janitor':[100, 100, 100, 100]}
        result = {"JD's rating": 47.25,
            "Turk's rating": 33.25,
            "Janitor's rating": 100.0}
        self.assertEqual(ordinary_case(input_data), result)

    def test_other_data_type(self):
        input_data = [3, 'JD', True, (33, 77), ['slay', 'invoke', ], ]
        for i in input_data:
            self.assertRaises(ValueError, ordinary_case, i)

    def test_empty_list(self):
        input_data = {'Jon Snow': []}
        result = {"Jon Snow's rating": 0}
        self.assertEqual(ordinary_case(input_data), result)

unittest.main()