import pytest


from code import main

def test_read_data():
    expected = {
        'Ukraine': {'2000': 48000000, '2001': 48100000, '2002': 48200000},
        'Poland': {'2000': 38000000, '2001': 38100000, '2002': 38200000},
        'Germany': {'2000': 82000000, '2001': 82100000, '2002': 82200000}
    }
    actual = read_data('population.txt')
    assert actual == expected
# тести були спеціально в ведені не правильні данні щоб вони були FAILD