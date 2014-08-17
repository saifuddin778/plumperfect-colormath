import sys
import os
import json
from itertools import permutations
import random
from numpy.random import rand

from colormath.color_objects import *
from colormath.color_diff import *
from colormath.color_conversions import convert_color as cco


lib_path = os.path.abspath('../plumperfect-colormath/')
sys.path.append(lib_path)
from manage import convert, distance

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
def test_conv_invalid_no_valid():
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

def test_conv_invalid_color_formats():
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
def test_conv_valid_queries():
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


"""
testing the distance calculation methods
"""

"""
invalid distance calculation queries without colors
"""
def test_dist_invalid_no_valid():
    query_1 = {'type': -1} #error 2
    query_2 = {'abcxyz': ''} #error 1
    query_3 = {'type': 'sdds'} # error 2
    query_4 = {'type': 'cie2000'} # error 2
    query_5 = {'ti': ''} #error 1
    query_6 = {'type': ''} #error 2

    result_1 = distance(**query_1)
    result_2 = distance(**query_2)
    result_3 = distance(**query_3)
    result_4 = distance(**query_4)
    result_5 = distance(**query_5)
    result_6 = distance(**query_6)

    assert result_1['output']['error_type'] == 2
    assert result_2['output']['error_type'] == 1
    assert result_3['output']['error_type'] == 2
    assert result_4['output']['error_type'] == 2
    assert result_5['output']['error_type'] == 1
    assert result_6['output']['error_type'] == 2


"""
invalid distance calculation queries with invalid colors
"""
def test_dist_invalid_color():
    query_1 = {'type': 'cie2000', 'c1': '', 'c2': ''} #error 5
    query_2 = {'type': 'cmc', 'c1': (1,2,3), 'c2': ''} #error 5
    query_3 = {'type': 'cie1994', 'c1': (1,2,'a'), 'c2': ''} #error 5
    query_4 = {'type': 'cie2000', 'c1': (1,2), 'c2': (1.2, 2,3)} # 6
    query_5 = {'type': 'cie2000', 'c1': (1,2,3)} #error 3
    query_6 = {'type': 'cie2000', 'c2': (1,2,3)} #error 2
    query_7 = {'c2': (1,2,3)} #error 0
    query_8 = {'c1': (1,2)} #error 0
    query_9 = {'type': 'cie1976', 'c': (2,3,2), 'c2': (1,2,3)} #error 2
    query_10 = {'type': 'cie1976', 'c1': (0,0,0), 'c2': [0,0,]} #error 6
    query_11 = {'type': '', 'c1': '', 'c2': ''} #error 5
    query_12 = {'type': '', 'c1': ''} # error 3
    

    result_1 = distance(**query_1)
    result_2 = distance(**query_2)
    result_3 = distance(**query_3)
    result_4 = distance(**query_4)
    result_5 = distance(**query_5)
    result_6 = distance(**query_6)
    result_7 = distance(**query_7)
    result_8 = distance(**query_8)
    result_9 = distance(**query_9)
    result_10 = distance(**query_10)
    result_11 = distance(**query_11)
    result_12 = distance(**query_12)
    

    assert result_1['output']['error_type'] == 5
    assert result_2['output']['error_type'] == 5
    assert result_3['output']['error_type'] == 5
    assert result_4['output']['error_type'] == 6
    assert result_5['output']['error_type'] == 3
    assert result_6['output']['error_type'] == 2
    assert result_7['output']['error_type'] == 0
    assert result_8['output']['error_type'] == 0
    assert result_9['output']['error_type'] == 2
    assert result_10['output']['error_type'] == 6
    assert result_11['output']['error_type'] == 5
    assert result_12['output']['error_type'] == 3


"""
testing valid queries for color distance
"""
def test_dist_valid_queries():
    distance_types = ['cie1976', 'cie1994', 'cie2000', 'cmc']
    distance_methods = {
        'cie1976': delta_e_cie1976,
        'cie1994': delta_e_cie1994,
        'cie2000': delta_e_cie2000,
        'cmc': delta_e_cmc
    }
    
    colors_a = [[random.randrange(0,255, 1) for i in range(3)] for _ in range(0, 1000)]
    colors_b = [[random.randrange(-100,100, 1) for i in range(3)] for _ in range(0, 1000)]
    
    for a, b in zip(colors_a, colors_b):
        c1 = a
        c2 = b
        distance_type = distance_types[random.randrange(0, 4)]
        query = dict(c1 = c1, c2 = c2, type=distance_type)
        out_api = distance(**query)
        output_real = distance_methods[distance_type](LabColor(*c1), LabColor(*c2))
        assert out_api['output'] == output_real
        
