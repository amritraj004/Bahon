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

from os import path
from Bahon.modules.database import sqlite3_database

defaults = {
    "sqlite3_path": path.abspath("Bahon/extras/test.db")
}


class Database:
    """
    This class manages the various databases that can be used with Bahon.
    For now only sqlite3 is supported.
    """
    def __init__(self, db_type: str, **kwargs):
        if db_type == "sqlite3":
            self.database = sqlite3_database.Database(kwargs.get("sqlite3_path") or defaults["sqlite3_path"])
