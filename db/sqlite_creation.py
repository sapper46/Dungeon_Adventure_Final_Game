import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_monster_table(conn):
    """Create a monster table in the provided database connection."""
    create_table_sql = """ CREATE TABLE IF NOT EXISTS monsters (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            health_points INTEGER,
                            min_damage INTEGER,
                            max_damage INTEGER,
                            attack_speed INTEGER,
                            chance_to_hit REAL,
                            chance_to_heal REAL,
                            min_heal_points INTEGER,
                            max_heal_points INTEGER
                        ); """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"db/monster_db.sqlite"

    # create a database connection
    conn = create_connection(database)

    # create monsters table
    if conn is not None:
        create_monster_table(conn)
    else:
        print("Error! cannot create the database connection.")
