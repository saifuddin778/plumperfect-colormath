import sys
sys.dont_write_bytecode = True

#returns the value converted to desired type
def wrap_type_function(func, arg):
    return func(arg)

#tests if the value is a valid pass for the function
def test_type_function(func, arg):
    try:
        func(arg)
        valid = True
    except:
        valid = False
    return valid
