import sqlite3
from sqlite3 import Error
from datetime import datetime

db = r"C:\Users\RICHARDSONLG20\IdeaProjects\ouch\db\pythonsqlite.db"

def create_connection(db_file):
    # create a database connection to a SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def store_spend(conn, spend):
    sql = ''' INSERT INTO spends(cost, description, category, date)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, spend)
    conn.commit()
    return cur.lastrowid


def create_spend(cost, category, description=None, custom_datetime_object=None):
    if custom_datetime_object:
        date_now = custom_datetime_object
    else:
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = create_connection(db)
    with conn:
        new_spend = (cost, description, category, date_now)
        spend_id = store_spend(conn, new_spend)
    conn.close()

    return spend_id


def get_all_spend_cost_sum():
    conn = create_connection(db)

    sql = ''' SELECT SUM(cost)
              FROM spends; '''
    cur = conn.cursor()
    cur.execute(sql)

    cost_sum = "{:.2f}".format(cur.fetchone()[0])

    conn.close()

    return cost_sum


def get_cost_sum_in_cat(category):
    conn = create_connection(db)

    print("getting sum: " + category) #delete me

    sql = ''' SELECT SUM(cost)
              FROM spends
              WHERE Category==?; '''
    cur = conn.cursor()
    cur.execute(sql, (category,))

    cost_sum = "{:.2f}".format(cur.fetchone()[0])

    conn.close()

    return cost_sum


if __name__ == '__main__':
    create_spend(.75, "gf", "small ball of fun")
    get_all_spend_cost_sum()


