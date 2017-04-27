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

handle_redirect_error = {
    "status": "fail",
    "reason": "This username does not have a associated redirect."
}

add_user_invalid_query = {
    "status": "fail",
    "reason": "Both username and redirect_url are required.",
    "example": "/u/add?username=lapz&redirect_to=https://abc.xyz"
}

add_user_success = {
    "status": "success",
}

add_user_fail = {
    "status": "fail",
    "reason": "This username already exists."
}
