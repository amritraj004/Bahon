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
import os
import socket
import json
from flask import Flask, request, make_response, Response, redirect
from Bahon.modules.database import Database
import Bahon.modules.utils.prepared_responses as p_resp

app = Flask("__name__")

# Initialize the database and get the connection object
db = Database(
    db_type="sqlite3"
)

"""
HTTP Status Codes Reference (from Wikipedia):
- 200:  OK
        Standard response for successful HTTP requests. The actual response will depend
        on the request method used. In a GET request, the response will contain an entity
        corresponding to the requested resource. In a POST request, the response will
        contain an entity describing or containing the result of the action.
- 400:  Bad Request
        The server cannot or will not process the request due to an apparent client error
        (e.g., malformed request syntax, too large size, invalid request message framing,
        or deceptive request routing)
- 404:  Not Found
        The requested resource could not be found but may be available in the future.
        Subsequent requests by the client are permissible.
"""


def generate_json_response(body: dict, code: int) -> Response:
    """
    Generate a JSON response.

    :param body: The body of the response. This will be converted
                 to JSON.
    :param code: The HTTP status code to send in the response.
    :returns Response
    """
    if code == 200:
        body.update({"status": "success"})
    else:
        body.update({"status": "fail"})

    resp = make_response(json.dumps(body), code)
    resp.headers["Content-Type"] = "application/json"

    return resp


@app.route("/")
def index():
    return "Environment var 'Name': {0}\nHostname: {1}".format(os.getenv("NAME"), socket.gethostname())


@app.route("/<username>", methods=["GET"])
def handle_redirect(username):
    result = db.fetch_user(username)
    if result:
        return redirect(result)

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


# TODO: Maybe delete should not be a public method or a token should be used?
@app.route("/u/delete", methods=["GET"])
def remove_user():
    username = request.args.get("username")

    # Validation for the query strings
    if username is None:
        return generate_json_response(p_resp.delete_user_invalid_query, 400)

    if db.delete_user(username):
        return generate_json_response(p_resp.delete_user_success, 200)

    else:
        return generate_json_response(p_resp.delete_user_fail, 400)

