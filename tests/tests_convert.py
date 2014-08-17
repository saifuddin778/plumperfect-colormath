import sys
import os
import json
from itertools import permutations, cycle
import random
from numpy.random import rand

from colormath.color_objects import *
from colormath.color_conversions import convert_color as cco


lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from manage import convert

"""
testing the conversion methods
"""

"""
testing docs
"""
#def test_docs():
#    pass

"""
testing invalid queries - case # no valid parameters at all
"""
def test_invalid_no_valid():
    query_1 = {'input_type': 1} #error 3
    query_2 = {'sjhld': 1} #error 2
    query_3 = {'input_type': 'sdds'} # error 3
    query_4 = {'input_type': 'rgb'} # error 3
    query_5 = {'input_type': 'rgb', 'output_type': 2} #error 4
    query_6 = {'input_type': '', 'output_type': ''} #error 4

    result_1 = convert(**query_1)
    result_2 = convert(**query_2)
    result_3 = convert(**query_3)
    result_4 = convert(**query_4)
    result_5 = convert(**query_5)
    result_6 = convert(**query_6)

    assert result_1['output']['error_type'] == 3
    assert result_2['output']['error_type'] == 2
    assert result_3['output']['error_type'] == 3
    assert result_4['output']['error_type'] == 3
    assert result_5['output']['error_type'] == 4
    assert result_6['output']['error_type'] == 4


"""
testing with different invalid color formats
"""

def test_invalid_color_formats():
    query_1 = {'input_type': 'rgb', 'output_type': 'hsl', 'color': ''} #error 9
    query_3 = {'input_type': '', 'output_type': 'lab', 'color': [1,2,'a']} #error 11
    query_4 = {'color': (1,2,3)} #error 2
    query_5 = {'color': (1,2,3), 'input_type': 'rgb', 'output_type': 'abc'} # error 4
    query_6 = {'color': [1,2,3], 'input_type': 'abc', 'output_type': 'lab'} # error 4
    query_7 = {'color': (1,2,3,4,5,6,7), 'input_type': 'hsl', 'output_type': 'lab'} # error 10
    query_8 = {'color': (), 'input_type': 'hsl', 'output_type': 'lab'} # error 10
    query_9 = {'color': '', 'input_type': 'hsl', 'output_type': 'lab'} # error 9

    result_1 = convert(**query_1)
    result_3 = convert(**query_3)
    result_4 = convert(**query_4)
    result_5 = convert(**query_5)
    result_6 = convert(**query_6)
    result_7 = convert(**query_7)
    result_8 = convert(**query_8)
    result_9 = convert(**query_9)

    assert result_1['output']['error_type'] == 9
    assert result_3['output']['error_type'] == 11
    assert result_4['output']['error_type'] == 2
    assert result_5['output']['error_type'] == 4
    assert result_6['output']['error_type'] == 4
    assert result_7['output']['error_type'] == 10
    assert result_8['output']['error_type'] == 10
    assert result_9['output']['error_type'] == 9   

"""
testing valid queries - testing with different valid combinations to make sure nothing
goes functionaly wrong in the production
"""
def test_valid_queries():
    color_codes = ['rgb', 'hsl', 'lab']
    
    color_sets = {
                'lab': LabColor,
                'hsl': HSLColor,
                'rgb': sRGBColor
    }
    
    n_iters = 1000
    #testing N times for validty. You can increase or decrease this n_iters based on your requirements.
    for i in range(0, n_iters):
        for j in permutations(rand(3)):
            color_ = j
            input_type = color_codes[random.randrange(0, 3)]
            output_type = color_codes[random.randrange(0, 3)]
            query = {'input_type': input_type, 'output_type': output_type, 'color': color_}
            input_color_real = dict([(input_type+'_'+a, b) for a, b in zip(input_type, color_)])
            input_color_real = color_sets[input_type](**input_color_real)

            real_output = sorted(cco(input_color_real, color_sets[output_type]).get_value_tuple())
            query_result = sorted(convert(**query)['output'].values())
            assert real_output == query_result
