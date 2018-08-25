# adminBOT user management

import sqlite3
from config import adminBOTDB
import hashlib

conn = sqlite3.connect(adminBOTDB)  # connecting to SQLlite DB
c = conn.cursor()  # creating cursor from connection.

def new_user(username, password):
    pass_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    sql_query = 'INSERT INTO users(login, password) values("%s","%s")' % (username, pass_hash)
    try:
        c.execute(sql_query)
        conn.commit()
        return "Success"
    except:
        conn.close()
        return "Error"


def show_users():
    sql_query = 'SELECT id, login FROM users'
    c.execute(sql_query)
    data = c.fetchall()
    return data


def password_reset(username, password):
    sql_query = 'UPDATE users SET password="%s" where login="%s"' % (username, password)
    c.execute(sql_query)
    conn.commit()


def delete_user(uid):
    delete_user = 'DELETE FROM users WHERE id = %s' % uid
    delete_roles = 'DELETE FROM com_users WHERE users_id = %s' % uid
    c.execute(delete_user)
    c.execute(delete_roles)
    conn.commit()


def delete_role(user_id, role):
    sql_query = 'DELETE FROM com_users WHERE users_id = %s AND roles_id = %s' % (user_id, role)
    c.execute(sql_query)
    conn.commit()


def show_roles(uid):
    sql_query = '''
    SELECT login, desc from Users
        U JOIN com_users
        CU on CU.users_id = U.id
        JOIN commands C on C.id = CU.roles_id
        where u.id = %s
    ''' % uid
    c.execute(sql_query)
    data = c.fetchall()
    for i in data:
        print(i)


def assign_role(user_id, role):
    sql_query = 'INSERT INTO com_users (users_id, roles_id) VALUES (%s,%s)' % (user_id, role)
    c.execute(sql_query)
    conn.commit()


help = ("""
adminBOT User Management"
Please type a command from list:"

1. Show users
2. Show user rights
3. Add new user
4. Add user right
5. Revoke user right
6. Delete user
7. Show this message again
8. Exit
""")
print(help)

while True:
    option = input("# ")
    if option == "1":
        users = show_users()
        print("| ID | User name")
        print("----------------")
        for i in users:
            print("| %s  | %s" % (i[0],i[1]))

    if option == "2":
        user_id = input("Please type user id: ")
        show_roles(user_id)

    if option == "3":
        username = input("Please type new username: ")
        password = input("Please type password for new user: ")
        print(new_user(username, password))

    if option == "6":
        user_id = input("Please type user id: ")
        delete_user(user_id)

    if option == "7":
        print(help)
        conn.close()

    if option == "8":
        exit()
    else:
        print("Not yet implemented or you entered the wrong command")