import sys
sys.dont_write_bytecode = True

import ast
from types import FloatType, IntType, TupleType, ListType
from notifications import dist_notif
from colormath.color_diff import *
from colormath.color_objects import LabColor

distance_types = {
    'cie1976': delta_e_cie1976,
    'cie1994': delta_e_cie1994,
    'cie2000': delta_e_cie2000,
    'cmc': delta_e_cmc
}

"""
invalid notifications generator
"""
def invalid_distance_queries(query_type, param_count_related=False):
    if param_count_related:
        notice = dist_notif[query_type]
        notice['requirements'] = param_count_related
    else:        
        notice = dist_notif[query_type]
    return notice

"""
validates the parameters passed in - step by step
"""
def validate_distance_items(input_item, desired_length, desired_types, desired_unit_types, is_module):
    indicator = {'result_item': input_item, 'valid': True, 'response': ''}
    distance_types = {
        'cie1976': True,
        'cie2000': True,
        'cie2000': True,
        'cmc': True
    }
    
    if not desired_length:
        if distance_types.get(input_item) is None:
                indicator['valid'] = False
                indicator['response'] = invalid_distance_queries('invalid_distance_type')
    else:
        try:
            """
            if not is_module:
                input_item = ast.literal_eval(input_item)
            """
            if not len(input_item):
                indicator['valid'] = False
                indicator['response'] = invalid_queries('wrong_color_format')
            else:
                input_item = ast.literal_eval(input_item)
                indicator['result_item'] = input_item
                if type(input_item) not in desired_types:
                    indicator['valid'] = False
                    indicator['response'] = invalid_distance_queries('wrong_color_format')
                else:
                    unit_types = list(set(map(type, input_item)))
                    if len(input_item) != desired_length:
                        indicator['valid'] = False
                        indicator['response'] = invalid_distance_queries('invalid_color_length')
                    else:
                        for a in unit_types:
                            if a not in desired_unit_types:
                                indicator['valid'] = False
                                indicator['response'] = invalid_distance_queries('invalid_color_features')
                                break
        except:
                indicator['valid'] = False
                indicator['response'] = invalid_distance_queries('wrong_color_format')
    return indicator



class cd_object(object):
    def __init__(self, params):
        self.params = params
        self.c1 = self.params['c1']
        self.c2 = self.params['c2']
        self.type_ = self.params['type']
        self.element_types = [FloatType, IntType]
    
    def wrap_color_object(self):
        self.c1 = LabColor(*self.c1)
        self.c2 = LabColor(*self.c2)
    
    def calculate_distance(self):
        self.wrap_color_object()
        return distance_types[self.type_](self.c1, self.c2)