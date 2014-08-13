import sys
sys.dont_write_bytecode = True
from color_conversion import cc_validation, invalid_queries, validate_type

class color_convert(object):
    def __init__(self, arguments):
        self.arguments = arguments
    
    def convert(self):
        if not self.arguments:
            response = invalid_queries('empty_query')
        if self.arguments.get('type') is None:
            response = invalid_queries('convert_wo_type')
        else:
            if not validate_type(self.arguments['type']):
                response = invalid_queries('invalid_color_type')
            else:
                type_ = self.arguments['type']
                parameters = {}
                if len(self.arguments) == 1:
                    response = invalid_queries('no_params_except_type')
                else:
                    for key,val in self.arguments.iteritems():
                        if key != 'type':
                                parameters[key] = val
                    #validating count, keys and their corresponding values
                    valids = cc_validation(parameters, type_)
                    valids_results = [valids.valid_pc(), valids.valid_pk()]
                    for a in valids_results:
                        if not a['indicator']:
                            response = a['response']
                            break
                        else:
                            response = True
                    if response == True:
                        values_indicator = valids.valid_pv()
                        if not values_indicator['indicator']:
                            response = values_indicator['response']
                        else:
                            response = valids.wrap_method()
        return response



class color_distance(object):
    def __init__(self, arguments):
        self.arguments = arguments
    
    def distance(self):
        if not self.arguments:
            response = invalid_queries('empty_query')
        if self.arguments.get('type') is None:
            response = invalid_queries('convert_wo_type')
