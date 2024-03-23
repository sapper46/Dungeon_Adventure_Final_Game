import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a database connection to the SQLite database specified by the db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def select_all_monsters(conn):
    """
    Query all rows in the monsters table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM monsters")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def get_db_monster(db_file, name):
    """Fetch a monster's details by its name"""
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM monsters WHERE name=?", (name,))
    monster_data = cur.fetchone()
    conn.close()
    return monster_data
