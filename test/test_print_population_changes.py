import io
import sys
import pytest

from code import main

def test_print_population_changes():
    populations = {
        'Ukraine': {'2000': 48000000, '2001': 48100000, '2002': 48200000},
        'Poland': {'2000': 38000000, '2001': 38100000, '2002': 38200000},
        'Germany': {'2000': 82000000, '2001': 82100000, '2002': 82200000},
    }
    expected_output = "Ukraine:\n\t2001: 100,000\n\t2002: 100,000\nPoland:\n\t2001: 100,000\n\t2002: 100,000\nGermany:\n\t2001: 100,000\n\t2002: 100,000\n"
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_population_changes(populations)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == expected_output