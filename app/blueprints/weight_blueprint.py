import json
import logging
from datetime import datetime

from flask import Blueprint, request, jsonify, make_response

from app.weight.weight_reader import get_weight

weight_blueprint = Blueprint('weight_blueprint', __name__)


@weight_blueprint.route("/api/weight", methods=['GET'])
def get_weight_endpoint():
    response = get_weight()
    return make_response(response)
