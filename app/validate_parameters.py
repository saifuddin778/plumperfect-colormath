import sys
sys.dont_write_bytecode = True

validate_cc_parameters = {
                           
                            'lab': {'min_count': 3,
                                      'params': {'lab_l': float,
                                                     'lab_a': float,
                                                     'lab_b': float}
                                    },
                            
                            'lchab': {'min_count': 3,
                                        'params': {'lch_l': float,
                                                         'lch_c': float,
                                                         'lch_h': float}
                                      },
                            'lchuv': {'min_count': 3,
                                        'params': {'lch_l': float,
                                                         'lch_c': float,
                                                         'lch_h': float}
                                    },
                            'luv': {'min_count': 3,
                                    'params': {'luv_l': float,
                                                    'luv_u': float,
                                                    'luv_v': float}
                                    },
                            'xyz': {'min_count': 3,                                    
                                      'params': {'xyz_x': float,
                                                        'xyz_y': float,
                                                      'xyz_z': float}
                                },
                            'xyy': {'min_count': 3,
                                       'params': {'xyy_x': float,
                                                  'xyy_y': float,
                                                  'xyy_Y': float}
                            },
                            'hsl': {
                                'min_count': 3,
                                'params': {'hsl_h': float,
                                                'hsl_s': float,
                                                'hsl_l': float}
                            },
                            'hsv': {
                                'min_count': 3,
                                'params': {'hsv_h': float,
                                                'hsv_s': float,
                                                'hsv_v': float}
                            },
                            'cmy': {
                                'min_count': 3,
                                'params': {'cmy_c': float,
                                                'cmy_m': float,
                                                'cmy_y': float}
                            },
                            'cmyk': {
                                'min_count': 4,
                                'params': {'cmyk_c': float,
                                                'cmyk_m': float,
                                                'cmyk_y': float,
                                                'cmyk_k': float}
                            },
                             'spectral': {'params': { 'spec_340': float,
                                                              'spec_350': float,
                                                              'spec_360': float,
                                                              'spec_370': float,
                                                              'spec_380': float,
                                                              'spec_390': float,
                                                              'spec_400': float,
                                                              'spec_410': float,
                                                              'spec_420': float,
                                                              'spec_430': float,
                                                              'spec_440': float,
                                                              'spec_450': float,
                                                              'spec_460': float,
                                                              'spec_470': float,
                                                              'spec_480': float,
                                                              'spec_490': float,
                                                              'spec_500': float,
                                                              'spec_510': float,
                                                              'spec_520': float,
                                                              'spec_530': float,
                                                              'spec_540': float,
                                                              'spec_550': float,
                                                              'spec_560': float,
                                                              'spec_570': float,
                                                              'spec_580': float,
                                                              'spec_590': float,
                                                              'spec_600': float,
                                                              'spec_610': float,
                                                              'spec_620': float,
                                                              'spec_630': float,
                                                              'spec_640': float,
                                                              'spec_650': float,
                                                              'spec_660': float,
                                                              'spec_670': float,
                                                              'spec_680': float,
                                                              'spec_690': float,
                                                              'spec_700': float,
                                                              'spec_710': float,
                                                              'spec_720': float,
                                                              'spec_730': float,
                                                              'spec_740': float,
                                                              'spec_750': float,
                                                              'spec_760': float,
                                                              'spec_770': float,
                                                              'spec_780': float,
                                                              'spec_790': float,
                                                              'spec_800': float,
                                                              'spec_810': float,
                                                              'spec_820': float,
                                                              'spec_830': float}
                                          },
                            
                            
                }




