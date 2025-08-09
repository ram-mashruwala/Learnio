from flask import jsonify
from . import api_bp

@api_bp.route("/")
def index():
    return jsonify({"testing": "this is more testing"})
