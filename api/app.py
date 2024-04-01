#!/usr/bin/env python3
""" API server for the database """
from flask import Flask, request, jsonify
# from db import get_from_db


def check_query(query):
    """ Check that query is valid and not malformed """
    pass

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/episodes", methods=["POST"])
def episode_query():
    query = request.get_json()
    # tlop_data = get_from_db(query)

