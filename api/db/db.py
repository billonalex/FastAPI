#!/usr/bin/python
import sqlite3
import os
from datetime import datetime

now = datetime.now()

db_name = "fastapi.db"
db_dump = "dump/dump-" + now.strftime("%Y-%m-%d") + ".sql"


def connect():
    abs_path = os.path.dirname(os.path.abspath(__file__)) + "/" + db_name
    conn = sqlite3.connect(abs_path)
    conn.row_factory = dict_factory
    return conn


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def dump_db():
    abs_path_db = os.path.dirname(os.path.abspath(__file__)) + "/" + db_name
    conn = sqlite3.connect(abs_path_db)
    abs_path = os.path.dirname(os.path.abspath(__file__)) + "/" + db_dump

    file = open(abs_path, 'w')

    for line in conn.iterdump():
        file.write('%s\n' % line)

    file.close()
