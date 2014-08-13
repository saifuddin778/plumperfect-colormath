import sys
sys.dont_write_bytecode = True

import json
from flask import Flask, request
from app.app import color_convert, color_distance
from time import time as tm

colormath_app = Flask(__name__)
colormath_app.config['SECRET_KEY'] = '1234567890'

"""
Main method to run the app either in a debug or prod mode.
"""
def main_(debug=False):
    if debug:
        colormath_app.debug=True
        colormath_app.run()
    else:
        colormath_app.debug=False
        colormath_app.run()

@colormath_app.route('/')
def main():
    name = "colormath RGB conversion api"
    version = '1.0'
    object_ = {'name': name, 'version': version}
    return json.dumps(object_)


@colormath_app.route('/convert/')
def convert(**params):
    if params:
        color_conversion_ = color_convert(params)
        return color_conversion_.convert()
    elif request.args:
        start_ = tm()
        color_conversion_ = color_convert(request.args)
        end_ = tm()
        return json.dumps({'time_spent': float(end_-start_), 'output': color_conversion_.convert()})

if __name__ == "__main__" and len(sys.argv) == 4:
    mode = sys.argv[3]
    if mode == 'settings.prod':
        main_()
    elif mode == 'settings.development':
        main_(True)
