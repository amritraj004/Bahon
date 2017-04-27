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

import sqlite3
from datetime import datetime


class Database:
    prepared_statements = {
        "fetch_user": "SELECT redirectTo FROM redirects WHERE userName IS ?",
        "insert_user": "INSERT INTO redirects VALUES(?, ?, ?)",
        "delete_user": "DELETE FROM redirects WHERE userName IS ?;"
    }

    def __init__(self, db_location):
        self.connection = sqlite3.connect(
            db_location,
            check_same_thread=False
        )

    def fetch_user(self, username: str) -> str or None:
        cur = self.connection.cursor()
        cur.execute(self.prepared_statements["fetch_user"], (username,))
        result = cur.fetchall()
        cur.close()

        for item in result:
            return item[0]
        else:
            return None

    def insert_user(self, username: str, redirect_to: str) -> True or False:
        try:
            cur = self.connection.cursor()
            cur.execute(self.prepared_statements["insert_user"], (datetime.utcnow().isoformat(), username, redirect_to))
            cur.close()

            # Commit the changes
            self.connection.commit()

            return True

        # IntegrityError means that this username already exists
        # or one of the NOT NULL marked fields are NULL
        except sqlite3.IntegrityError:
            return False

