#!/usr/bin/python3
"""
Still don't know the exact thing yet
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify, request

@app_views.route('/status', methods=['GET'])
def status():
    """
    function for status route that returns the status
    """
    if request.method == 'GET':
        whatever = {"status": "OK"}
        return jsonify(whatever)
@app_views.route('/stats', methods=['GET'])
def stats():
    """
    function to return the count of all class objects
    """
    if request.method == 'GET':
        response = {}
        PLURALS = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)
