import sys
sys.dont_write_bytecode = True
from colormath.color_objects import *
from colormath.color_conversions import convert_color as cco
from notifications import conv_notif
from validate_parameters import validate_cc_parameters as pcv
from misc import test_type_function, wrap_type_function


color_sets = {
                'spectral': SpectralColor,
                'lab': LabColor,
                'lchab': LCHabColor,
                'lchuv': LCHuvColor,
                'luv': LuvColor,
                'xyz': XYZColor,
                'xyy': xyYColor,
                'hsl': HSLColor,
                'hsv': HSVColor,
                'cmy': CMYColor,
                'cmyk': CMYKColor
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
validates the input type of color to be converted
"""
def validate_type(type_):
    types_ = {
                'spectral': None,
                'lab': None,
                'lchab': None,
                'lchuv': None,
                'luv': None,
                'xyz': None,
                'xyy': None,
                'hsl': None,
                'hsv': None,
                'cmy': None,
                'cmyk': None,
                }

    if types_.has_key(type_):
        return True
    else:
        return False




class cc_validation(object):
    def __init__(self, params, type_):
        self.params = params
        self.type_ = type_
    
    """
    validates the the number of parameters for the given input color type
    """
    def valid_pc(self):
        validation = {'indicator': True}
        if pcv[self.type_].has_key('min_count'):
            if len(self.params) != pcv[self.type_]['min_count']:
                validation['indicator'] = False
                validation['response'] = invalid_queries('wrong_number_params',
                                                                {'input_params': len(self.params),
                                                                 'required_params':pcv[self.type_]['min_count']}
                                                         )
        return validation


    """
    validates all the parameters for a given color type individually and checks if the
    params are correctly spelled
    """
    def valid_pk(self):
        validation = {'indicator': True}
        if sorted(pcv[self.type_]['params'].keys()) != sorted(self.params.keys()):
            validation['indicator'] = False
            validation['response'] = invalid_queries('misspelled_param')    
        return validation

    """
    validates all the parameters passed have correct values i.e. can be converted into through their
    valid formats.
    """
    def valid_pv(self):
        validation = {'indicator': True}
        for k,v in self.params.iteritems():
            if not test_type_function(pcv[self.type_]['params'][k], self.params[k]):
                validation['indicator'] = False
                validation['response'] = invalid_queries('invalid_param_value')
                break
        return validation

    """
    maps to the right type
    """
    def map_to_types(self):
        for a in sorted(pcv[self.type_]['params'].keys()):
            self.params[a] = wrap_type_function(pcv[self.type_]['params'][a], self.params[a])
        return self.params
    
    def convert_(self):
        result = cco(self.color_obj, sRGBColor)
        return dict([(k,v) for k, v in zip(result.VALUES, result.get_value_tuple())])

    #wraps the function passed in to parameters as dicts
    def wrap_method(self):
        self.map_to_types()
        self.color_obj = color_sets[self.type_](**self.params)
        return self.convert_()
    