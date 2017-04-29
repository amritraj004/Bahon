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
    "reason": "This username does not have a associated redirect."
}

# -- Add user block
add_user_invalid_query = {
    "reason": "Parameters username and redirect_url are both required.",
    "example": "GET /u/add?username=lapz&redirect_url=https://abc.xyz"
}

add_user_success = {
    "info": "To test if the redirect is working properly, visit: {0}"
}

add_user_fail = {
    "reason": "This username already exists."
}

# -- Delete user block
delete_user_invalid_query = {
    "reason": "Parameter username is required.",
    "example": "GET /u/delete?username=lapz"
}

delete_user_success = {
    "info": "This username and its associated data are now deleted."
}

delete_user_fail = {
    "reason": "This username does not exist."
}
