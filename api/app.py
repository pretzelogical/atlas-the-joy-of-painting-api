#!/usr/bin/env python3
""" API server for the database """
from flask import Flask, request, jsonify
from check_query import check_query
from os import environ
# from db import get_from_db


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/episodes", methods=["POST"])
def episode_query():
    query = request.get_json()
    query_error = check_query(query)
    if query_error:
        return jsonify({"error": query_error}), 400
    # tlop_data = get_from_db(query)
    return jsonify({})


if __name__ == '__main__':
    host = environ.get('tjop_host', 'localhost')
    port = int(environ.get('tjop_port', '5000'))
    app.run(host, port)
