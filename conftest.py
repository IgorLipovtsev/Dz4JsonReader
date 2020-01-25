import pytest
import random
import csv


@pytest.fixture()
def csv_reader():
    """читаем csv файл"""
    with open('books.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        list_of_rows = []
        for row in reader:
            data = {}
            data['title'] = row['Title']

            data['author'] = row['Author']

            data['height'] = row['Height']

            list_of_rows.append(data)

    return random.choice(list_of_rows)
