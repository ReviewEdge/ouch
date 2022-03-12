import database_connector as dbc


# WRITE CODE HERE THAT WILL EXECUTE TERMINAL COMMANDS TO CREATE DB


def create_users_table():
    conn = dbc.create_connection()

    sql = """CREATE TABLE IF NOT EXISTS Users (
        "UserID" INTEGER UNIQUE,
        "DateAdded" TEXT,
        PRIMARY KEY("UserID")
    );"""

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

    conn.close()

    return "created Users table in db"


if __name__ == '__main__':
    print(create_users_table())
