import sqlite3
from sqlite3 import Error
from datetime import datetime
import config

db = config.db_location

def create_connection():
    # create a database connection to a SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)

    return conn


# checks if user is in db
def check_if_new_user(user_id):
    conn = create_connection()

    sql = """SELECT UserID
                FROM Users
                WHERE UserID=?"""
    cur = conn.cursor()
    cur.execute(sql, (user_id,))

    result = cur.fetchone()

    if result:
        output = False
    else:
        output = True

    conn.close()

    return output


def add_new_user_to_db(user_id):
    conn = create_connection()

    sql1 = """INSERT INTO Users(UserID, DateAdded)
              VALUES(?,?)"""

    sql2 = "CREATE TABLE IF NOT EXISTS User" + user_id + """Spends (
            "ID" INTEGER UNIQUE,
            "Cost" NUMERIC,
            "Description" TEXT,
            "Category" TEXT,
            "Date" TEXT,
            PRIMARY KEY("ID" AUTOINCREMENT)
        );"""

    cur = conn.cursor()
    cur.execute(sql1, (user_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    cur.execute(sql2)
    conn.commit()

    conn.close()
    return "added new user " + user_id + " to db"


def store_spend(conn, user_id, spend):
    sql = "INSERT INTO User" + user_id + """Spends(cost, description, category, date)
              VALUES(?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, spend)
    conn.commit()
    return cur.lastrowid


def create_spend(user_id, cost, category, description=None, custom_datetime_object=None):
    if custom_datetime_object:
        date_now = custom_datetime_object
    else:
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = create_connection()
    with conn:
        new_spend = (cost, description, category, date_now)
        spend_id = store_spend(conn, user_id, new_spend)
    conn.close()

    return spend_id


def get_all_spend_cost_sum(user_id):
    conn = create_connection()

    sql = "SELECT SUM(cost) FROM User" + user_id + "Spends;"
    cur = conn.cursor()
    cur.execute(sql)

    try:
        cost_sum = "{:.2f}".format(cur.fetchone()[0])
    except TypeError:
        raise TypeError

    conn.close()

    return cost_sum


def get_cost_sum_in_cat(user_id, category):
    conn = create_connection()

    print("getting sum: " + category) #delete me

    sql = """ SELECT SUM(cost)
              FROM User""" + user_id + """spends
              WHERE Category==?;"""
    cur = conn.cursor()
    cur.execute(sql, (category,))

    try:
        cost_sum = "{:.2f}".format(cur.fetchone()[0])
    except TypeError:
        raise TypeError

    conn.close()

    return cost_sum


if __name__ == '__main__':
    # create_new_user_spend_table("thisisnotactuallyauser")
    # create_spend(.75, "gf", "small ball of fun")
    # get_all_spend_cost_sum()
    print("hey")
