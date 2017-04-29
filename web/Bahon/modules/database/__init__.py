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
from Bahon.modules.database.sqlite3_database import SQLite3Database

defaults = {
    "sqlite3_path": path.abspath("./Bahon/extras/test.db")
}


class Database(SQLite3Database):
    """
    This class manages the various databases that can be used with Bahon.
    For now only sqlite3 is supported.
    """

    # TODO: add a way to test if database is initialized with records and stuff
    # TODO: the path from kwargs should also be absolute
    def __init__(self, db_type: str, **kwargs):

        # since we are going to do multiple inheritance
        # using super to initialize the base classes is
        # not a very good idea.
        if db_type == "sqlite3":
            SQLite3Database.__init__(self, kwargs.get("sqlite3_path") or defaults["sqlite3_path"])
