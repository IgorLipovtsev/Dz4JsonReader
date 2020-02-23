import pytest
import json
import random


def test_json_writer(csv_reader):
    """записываем данные в новый json файл"""

    with open('users.json', 'r') as users_file:
        users = json.load(users_file)

    with open('igor_example.json', 'w') as users_file2:
        final_book = []
        for user in users:

            name_dict = {}

            name_dict['name'] = user['name']

            name_dict['gender'] = user['gender']

            name_dict['address'] = user['address']

            name_dict['books'] = [random.choice(csv_reader)]

            final_book.append(name_dict)

        json.dump(final_book, users_file2, indent=2)
