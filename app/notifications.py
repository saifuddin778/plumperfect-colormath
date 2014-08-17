import sys
sys.dont_write_bytecode = True

conv_notif = {}
dist_notif = {}

"""
Color Conversion Notifications
"""
conv_notif['empty_query'] = {
        'error_type': 0,
        'notice': 'empty query'
}

conv_notif['convert_wo_type'] = {
        'error_type': 1,
        'notice': 'please pass in the type of color to be converted to RGB'
}

conv_notif['no_input_type'] = {
        'error_type': 2,
        'notice': 'please pass in the type of your input color'
}

conv_notif['no_output_type'] = {
        'error_type': 3,
        'notice': 'please pass in the type you want your color to be converted to'
}

conv_notif['no_color'] = {
        'error_type': 4,
        'notice': 'no input color provided for conversion'
}


conv_notif['invalid_color_type'] = {
        'error_type': 4,
        'notice': 'please pass in the valid type(s) of colors to be converted'
}

conv_notif['no_params_except_type'] = {
        'error_type': 5,
        'notice': 'no parameters provided for the input color type to be converted'
}

conv_notif['wrong_number_params'] = {
        'error_type': 6,
        'notice': 'invalid number of arguments provided'
}

conv_notif['misspelled_param'] = {
        'error_type': 7,
        'notice': 'one or more misspelled color parameters are passed'
}

conv_notif['invalid_param_value'] = {
        'error_type': 8,
        'notice': 'one or more parameter values are of wrong types'
}

conv_notif['wrong_color_type'] = {
        'error_type': 9,
        'notice': 'please pass the color parameter as either a list or tuple of floats/ints: like (f, f, f).'
}

conv_notif['invalid_color_length'] = {
        'error_type': 10,
        'notice': 'please pass the color parameter as a either a list or tuple of 3 floats/ints.'
}

conv_notif['invalid_color_features'] = {
        'error_type': 11,
        'notice': 'please pass the color vector as a set of floats or ints.'
}


"""
Distance Calculation Notifications
"""
dist_notif['empty_query'] = {
        'error_type': 0,
        'notice': 'empty query'
}

dist_notif['no_distance_type'] = {
        'error_type': 1,
        'notice': 'please pass in the type of distance to be measured'
}

dist_notif['no_color_1'] = {
        'error_type': 2,
        'notice': 'please provide the color (c1) as c1=(float,float,float)'
}

dist_notif['no_color_2'] = {
        'error_type': 3,
        'notice': 'please provide the color (c1) as c1=(float,float,float)'
}

dist_notif['invalid_distance_type'] = {
        'error_type': 4,
        'notice': "invalid distance type specified. Distance can be one of the following: 'cie1976', 'cie2000','cie2000' and 'cmc'."
}

dist_notif['wrong_color_format'] = {
        'error_type': 5,
        'notice': 'one or more colors are provided in the wrong format - both colors should be strictly provided as tuples of floats or ints.'
}

dist_notif['invalid_color_length'] = {
        'error_type': 6,
        'notice': 'both of the colors c1 and c2 should be provided as length 3 tuples of floats or ints.'
}


dist_notif['invalid_color_features'] = {
        'error_type': 7,
        'notice': 'colors should be strictly provided as tuples of floats or ints.'
}


"""
Docs
"""
docs = {
        
        'convert': {
                'function': 'Returns the input color type converted to the desired type',
                'parameters': {'input_type': "input type of the color provided for conversion. This can either be 'lab', 'rgb' or 'hsl'",
                               'output_type': "output type of color you want as a result. This can either be 'lab', 'rgb' or 'hsl'",
                               'color': "the color to be converted - can be provided as a tuple of floats or ints",
                        },
                'example_queries': ['http://localhost:5000/convert/?input_type=rgb&output_type=hsl&color=(20,10,10)', 'http://localhost:5000/convert/?input_type=lab&output_type=rgb&color=(-2,-1,1)']
        },
        'distance': {
               'function': 'Returns the distance between two provided lab colors',
               'parameters': {'type': "the type of distance to be calculated between provided colors. This can either be 'cie1976', 'cie2000','cie2000' or 'cmc'",
                               'c1': 'first color (float,float,float)',
                               'c2': "second color (float,float,float)",
                        },
                'example_queries': ['http://localhost:5000/distance/?type=cmc&c1=(1,2,3)&c2=(-1,2,3)', 'http://localhost:5000/distance/?type=cie2000&c1=(1,20,3)&c2=(-1,21,3)']
 
        }      
}



