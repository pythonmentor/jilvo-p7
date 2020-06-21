import sys
import os
sys.path.append(f"{os.getcwd()}/flask_app/")
from parse_question import parsing

def test_parsing():
    results = ['tour', 'Eiffel', '']
    assert parsing("Où est la tour Eiffel ? ") == results
    


