import sys
sys.dont_write_bytecode = True

conv_notif = {}
dist_notif = {}

"""
Color Conversion Notifications
"""
conv_notif['empty_query'] = {
        'error_type': 0,
        'success': False,
        'notice': 'empty query'
}

conv_notif['convert_wo_type'] = {
        'error_type': 1,
        'success': False,
        'notice': 'please pass in the type of color to be converted to RGB'
}

conv_notif['invalid_color_type'] = {
        'error_type': 2,
        'success': False,
        'notice': 'please pass in the valid type of color to be converted to RGB'
}

conv_notif['no_params_except_type'] = {
        'error_type': 3,
        'success': False,
        'notice': 'no parameters provided for the input color type to be converted to RGB'
}

conv_notif['wrong_number_params'] = {
        'error_type': 4,
        'success': False,
        'notice': 'invalid number of arguments provided'
}

conv_notif['misspelled_param'] = {
        'error_type': 5,
        'success': False,
        'notice': 'one or more misspelled color parameters are passed'
}

conv_notif['invalid_param_value'] = {
        'error_type': 6,
        'success': False,
        'notice': 'one or more parameter values are of wrong types'
}