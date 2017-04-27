"""
Bahon - a simple url redirector
Copyright (C) 2017 Jewel Mahanta <jewelmahanta@gmail.com>

This file is part of Bahon.

Bahon is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Bahon is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Bahon.  If not, see <http://www.gnu.org/licenses/>.
"""

from flask import Flask, request, make_response, Response
from Bahon.modules.database import Database
import Bahon.modules.utils.prepared_responses as p_resp
import json

app = Flask("__name__")

# Initialize the database and get the connection object
db = Database(
    db_type="sqlite3",
).database


def generate_json_response(body: dict, code: int) -> Response:
    """
    Generate a JSON response.

    :param body: The body of the response. This will be converted
                 to JSON.
    :param code: The HTTP status code to send in the response.
    :returns Response
    """
    resp = make_response(json.dumps(body), code)
    resp.headers["Content-Type"] = "application/json"
    return resp


@app.route("/")
def index():
    return "Bahon"


@app.route("/<username>", methods=["GET"])
def handle_redirect(username):
    result = db.fetch_user(username)
    if result:
        # return redirect(result[4])
        return "redirect to: " + result

    else:
        return generate_json_response(p_resp.handle_redirect_error, 404)


@app.route("/u/add", methods=["GET"])
def add_user():
    username = request.args.get("username")
    redirect_url = request.args.get("redirect_url")

    # Validation for the query strings
    if username is None or redirect_url is None:
        return generate_json_response(p_resp.add_user_invalid_query, 400)

    # Success
    if db.insert_user(username, redirect_url):
        return generate_json_response(p_resp.add_user_success, 200)

    # Error
    else:
        return generate_json_response(p_resp.add_user_fail, 400)
