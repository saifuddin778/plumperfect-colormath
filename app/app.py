import sys
sys.dont_write_bytecode = True

import ast
from color_conversion import cc_object, invalid_queries, validate_conversion_items
from color_distance import cd_object, invalid_distance_queries, validate_distance_items
from types import FloatType, IntType, TupleType, ListType, StringType
from numpy import float64
from notifications import docs

"""
color conversion
"""
class color_convert(object):
    def __init__(self, arguments, module_query=False):
        self.status = False
        self.module_query = module_query
        self.arguments = arguments
        self.allowed_params = ['input_type', 'output_type', 'color']
    
    def convert(self):
        response = invalid_distance_queries('empty_query')
        if not self.arguments or len(self.arguments) == 0:
            return invalid_distance_queries('empty_query'), self.status
        
        if self.arguments.has_key('docs'):
            return docs['convert'], True
        
        parameters = {}
        
        for k,v in self.arguments.iteritems():
            if k in self.allowed_params:
                parameters[k] = str(v).strip()
        
        if len(parameters) == 0:
            return invalid_queries('no_input_type'), self.status
        
        if len(parameters) != 3:
            if parameters.get('input_type') is None:
                response = invalid_queries('no_input_type')
            elif parameters.get('output_type') is None:
                response = invalid_queries('no_output_type')
            elif parameters.get('color') is None:
                response = invalid_queries('no_color')
        else:
            for k, v in parameters.iteritems():   
                if k not in ['input_type', 'output_type']:
                    desired_type = [TupleType, ListType]
                    desired_length = 3
                    desired_unit_types = [FloatType, IntType, float64]
                else:
                    desired_type = [StringType]
                    desired_length = None
                    desired_unit_types = [StringType]
                
                validation = validate_conversion_items(v, desired_length, desired_type, desired_unit_types, self.module_query)

                if not validation['valid']:
                    response = validation['response']
                    break
                else:
                    parameters[k] = validation['result_item']
            if validation['valid']:
                conversion_object = cc_object(parameters)
                response = conversion_object.convert()
                self.status = True
        
        return response, self.status

"""
color distance
"""
class color_distance(object):
    def __init__(self, arguments, module_query=False):
        self.module_query = module_query
        self.status = False
        self.arguments = arguments
        self.allowed_params = ['c1', 'c2', 'type']
        
    def distance(self):
        response = invalid_queries('empty_query')
        if not self.arguments or len(self.arguments) == 0:
            return invalid_distance_queries('empty_query'), self.status
        
        if self.arguments.has_key('docs'):
            return docs['convert'], True
        
        parameters = {}
        
        for k,v in self.arguments.iteritems():
            if k in self.allowed_params:
                parameters[k] = str(v).strip()
        
        if len(parameters) == 0:
            return invalid_distance_queries('no_distance_type'), self.status
        
        if len(parameters) != 3:
            if parameters.get('type') is None:
                repsonse = invalid_distance_queries('no_distance_type')
            elif parameters.get('c1') is None:
                response = invalid_distance_queries('no_color_1')
            elif parameters.get('c2') is None:
                response = invalid_distance_queries('no_color_2')
            
        else:
            for k, v in parameters.iteritems():
                if k == 'type':
                    desired_length = None
                    desired_type = [StringType]
                    desired_unit_types = None
                else:
                    desired_length = 3
                    desired_type = [TupleType, ListType]
                    desired_unit_types = [FloatType, IntType]
                    
                validation = validate_distance_items(v, desired_length, desired_type, desired_unit_types, self.module_query)
                if not validation['valid']:
                    response = validation['response']
                    break
                else:
                    parameters[k] = validation['result_item']
                    
            if validation['valid']:
                distance_object = cd_object(parameters)
                response = distance_object.calculate_distance()
                self.status = True
                
        return response, self.status