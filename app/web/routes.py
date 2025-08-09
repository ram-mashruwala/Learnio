from . import web_bp

@web_bp.route('/')
def list_users():
    return "<h1>Hello World</h1>"
