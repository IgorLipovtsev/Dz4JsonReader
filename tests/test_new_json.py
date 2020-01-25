import pytest
import json
import random


def test_json_writer(csv_reader):
    """записываем данные в новый json файл"""
    with open('users.json', 'r') as users_file:
        data = json.load(users_file)

    with open('igor_example.json', 'w') as users_file2:
        final = []
        for all_text in data:
            name_dict = {}

            name_dict['name'] = all_text['name']

            name_dict['gender'] = all_text['gender']

            name_dict['address'] = all_text['address']

            name_dict['books'] = [csv_reader]

            final.append(name_dict)

        json.dump(random.choice(final), users_file2, indent=2)
