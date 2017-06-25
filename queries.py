import psycopg2
import random


def user_datas():
    """Read the nessecery information from the user_file to
    connect to the database, such as dbname, username, password
    """
    with open('user.txt') as file:
        data = file.read()
        data = data.split(',')
        return data


def fetch_database(query, tuple_parameters=None, fetch='all'):
    """Connects to the database to retrieve data, then
    returns it.
    First parameter: query
    Second parameter: parameters which you want to insert into your query, use tupple type
    Third parameter: fetch type, one or all, use string type
    """
    try:
        data = user_datas()
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(data[0], data[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query, tuple_parameters)
        if fetch == 'all':
            rows = cursor.fetchall()
        elif fetch == 'one':
            rows = cursor.fetchone()
        return rows

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if conn:
            conn.close()


def modify_database(query, tuple_parameters=None):
    """Connects to the database then modifies the data
    without fetching anything.
    """
    try:
        data = user_datas()
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(data[0], data[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query, tuple_parameters)

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if conn:
            conn.close()


def register_new_user(user_name, password):
    modify_database("""INSERT INTO swuser(username, password)
                    SELECT '{}', '{}';""".format(user_name, password))


def check_user(username, password):
    """Selects user and password from the database"""
    data = []
    return fetch_database("""SELECT username FROM swuser
                          WHERE username='{}' AND password='{}';""".format(username,password))
    rows = cursor.fetchall()
    data = rows
    return data








            