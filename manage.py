import sys
sys.dont_write_bytecode = True

import json
from flask import Flask, request
from flask.ext.script import Manager, Server
from app.app import color_convert, color_distance
from time import time as tm

colormath_app = Flask(__name__)
manager = Manager(colormath_app)



"""
Main method to run the app either in a debug or prod mode.
"""
def main_(debug=False):
    manager.add_command("runserver", Server())
    manager.run()
    
    """
    if debug:
        colormath_app.debug=True
        colormath_app.run()
    else:
        colormath_app.debug=False
        colormath_app.run()
    """

@colormath_app.route('/')
@manager.command
def index():
    name = "colormath RGB conversion api"
    version = '1.0'
    object_ = {'name': name, 'version': version}
    return json.dumps(object_)


@colormath_app.route('/convert/')
@manager.option('--input_type')
@manager.option('--output_type')
@manager.option('--color')
def convert(**params):
    if params:
        color_conversion_ = color_convert(params, True)
        output, status = color_conversion_.convert()
        return {'output': output, 'status': status}
    else:
        start_ = tm()
        color_conversion_ = color_convert(request.args)
        end_ = tm()
        output, status = color_conversion_.convert()
        return json.dumps({'time_spent': float(end_-start_), 'output': output, 'status': status})
    

@colormath_app.route('/distance/')
@manager.option('--type')
@manager.option('--c1')
@manager.option('--c2')
def distance(**params):
    if params:
        color_distance_ = color_distance(params, True)
        output, status = color_distance_.distance()
        return {'output': output, 'status': status}
    else:
        start_ = tm()
        color_distance_ = color_distance(request.args)
        end_ = tm()
        output, status = color_distance_.distance()
        return json.dumps({'time_spent': float(end_-start_), 'output': output, 'status': status})
"""
if __name__ == "__main__" and len(sys.argv) == 4:
    mode = sys.argv[3]
    if mode == 'settings.prod':
        main_()
    elif mode == 'settings.development':
        main_(True)
"""
if __name__ == '__main__':
    main_()
