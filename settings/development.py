import sys
sys.dont_write_bytecode = True


"""
dev settings for plumperfect-colormath
"""
app_settings = dict(
    DEBUG = True,
    
    TESTING = True,

    PROPAGATE_EXCEPTIONS = True,
    
    PRESERVE_CONTEXT_ON_EXCEPTION= True,
    
    SECRET_KEY = None,
    
    SESSION_COOKIE_NAME = None,
    
    SESSION_COOKIE_DOMAIN = None,
    
    SESSION_COOKIE_PATH = None,
    
    SESSION_COOKIE_HTTPONLY = True,
    
    SESSION_COOKIE_SECURE = False,
    
    TRAP_HTTP_EXCEPTIONS = True,
    
    TRAP_BAD_REQUEST_ERRORS = False,
    
    JSON_AS_ASCII = True,
    
    JSON_SORT_KEYS = True,
    
    JSONIFY_PRETTYPRINT_REGULAR = True
)
