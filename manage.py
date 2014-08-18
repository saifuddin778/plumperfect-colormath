import sys
sys.dont_write_bytecode = True

import json
import subprocess
from flask import Flask, request
from flask.ext.script import Manager, Server, Option
from app.app import color_convert, color_distance
from settings import development
from time import time as tm

colormath_app = Flask(__name__)

for k, v in development.app_settings.iteritems():
    colormath_app.config[k] = v

manager = Manager(colormath_app)

    
"""
Main method to run the app either in a debug or prod mode.
"""
def main_(debug=False):
    manager.add_command("runserver", Server())
    manager.run()


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

if __name__ == '__main__':
    if 'tests' in sys.argv:
        print 'testing the current methods..'
        command_ = 'py.test --cov tests/'
        process = subprocess.Popen(command_, shell=True)
        process.wait()
    else:
        main_()