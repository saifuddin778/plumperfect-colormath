import sys
sys.dont_write_bytecode = True

validate_cc_parameters = {
                           
                            'lab': {'min_count': 3,
                                    'params': {'lab_l': float,
                                               'lab_a': float,
                                               'lab_b': float}
                                    },
                            'hsl': {
                                'min_count': 3,
                                'params': {'hsl_h': float,
                                           'hsl_s': float,
                                           'hsl_l': float}
                            },
                            'rgb': {
                                      'min_count': 3,
                                      'params': {'rgb_r': float,
                                                 'rgb_g': float,
                                                 'rgb_b': float}
                            }
}


validate_cd_parameters = {
                            'min_count': 3,
                            'params_type': float
}

