#!/usr/bin/env python3
""" API server for the database """
from flask import Flask, request, jsonify
from check_query import check_query
from os import environ
from db import TJOPDatabase
import atexit


db = TJOPDatabase()
db.connect(
    host=environ.get('tjop_sql_host', 'localhost'),
    port=int(environ.get('tjop_sql_port', '3306'))
)

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/episodes", methods=["POST"])
def episode_query():
    """ Execute episode query """
    query = request.get_json()
    query_error = check_query(query)
    if query_error:
        return jsonify({"error": query_error}), 400
    db_data = db.get(query)
    return jsonify(db_data)


def shutdown():
    db.close()
    print('Shutting down')


if __name__ == '__main__':
    host = environ.get('tjop_host', 'localhost')
    port = int(environ.get('tjop_port', '5000'))
    atexit.register(shutdown)
    app.run(host, port)
