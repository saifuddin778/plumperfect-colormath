import sys
sys.dont_write_bytecode = True

import ast
from colormath.color_objects import *
from colormath.color_conversions import convert_color as cco
from notifications import conv_notif

color_sets = {
                'lab': LabColor,
                'hsl': HSLColor,
                'rgb': sRGBColor
             }

"""
returns the right notification based on the type of invalid query
"""
def invalid_queries(query_type, param_count_related=False):
    if param_count_related:
        notice = conv_notif[query_type]
        notice['requirements'] = param_count_related
    else:        
        notice = conv_notif[query_type]
    return notice


"""
validates the parameters passed in - step by step
"""
def validate_conversion_items(input_item, desired_length, desired_types, desired_unit_types, is_module):
    indicator = {'result_item': input_item, 'valid': True, 'response': ''}
    color_types = {
                'lab': True,
                'hsl': True,
                'rgb': True
                }
    
    if not desired_length:
        if color_types.get(input_item) is None:
                indicator['valid'] = False
                indicator['response'] = invalid_queries('invalid_color_type')
    else:
        try:
            if not len(input_item):
                indicator['valid'] = False
                indicator['response'] = invalid_queries('wrong_color_type')
            else:    
                input_item = ast.literal_eval(input_item)
                indicator['result_item'] = input_item
            
                if type(input_item) not in desired_types:
                    indicator['valid'] = False
                    indicator['response'] = invalid_queries('wrong_color_type')
                else:
                    unit_types = list(set(map(type, input_item)))
                    if len(input_item) != desired_length:
                        indicator['valid'] = False
                        indicator['response'] = invalid_queries('invalid_color_length')
                    else:
                        for a in unit_types:
                            if a not in desired_unit_types:
                                indicator['valid'] = False
                                indicator['response'] = invalid_queries('invalid_color_features')
                                break
        except:
                indicator['valid'] = False
                indicator['response'] = invalid_queries('wrong_color_type')
    return indicator

"""
The main conversion object
"""
class cc_object(object):
    def __init__(self, params):
        self.color = params['color']
        self.input_type = params['input_type']
        self.output_type = params['output_type']
        
    def create_color_object(self):
        self.color_object = color_sets[self.input_type](*self.color)
    
    def convert(self):
        self.create_color_object()
        result = cco(self.color_object, color_sets[self.output_type])
        result = dict([(k,v) for k, v in zip(result.VALUES, result.get_value_tuple())])
        return result