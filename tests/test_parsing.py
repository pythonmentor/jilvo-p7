from pytest import *
import sys
import os
# sys.path.insert(0, '../flask_app/')
# from parse_question import parsing
sys.path.append(f"{os.getcwd()}/flask_app/")
from parse_question import parsing


def test_parsing():
    results = ['tour', 'Eiffel', '']
    assert parsing("Où est la tour Eiffel ? ") == results
    

