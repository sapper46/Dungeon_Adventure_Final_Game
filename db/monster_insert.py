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


def create_monster(conn, monster):
    """
    Create a new monster in the monsters table
    :param conn: Connection object
    :param monster: A tuple containing the monster data
    :return: monster id
    """
    sql = ''' INSERT INTO monsters(name, health_points, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal, min_heal_points, max_heal_points)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, monster)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"db/monster_db.sqlite"

    # create a database connection
    conn = create_connection(database)
    if conn:

        monsters = [
            ('Ogre', 200, 30, 60, 2, 0.6, 0.1, 30, 60),
            ('Gremlin', 70, 15, 30, 5, 0.8, 0.4, 20, 40),
            ('Skeleton', 100, 30, 50, 3, 0.8, 0.3, 30, 50)
        ]

        for monster in monsters:
            create_monster(conn, monster)
            print(f"monster type {monster[0]} added")

    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
