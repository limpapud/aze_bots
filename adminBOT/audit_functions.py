from telebot import TeleBot as Tb
import sqlite3
import re
import hashlib
import config

bot = Tb(config.token)


# function to check if user has current active session
def check_auth(message):  # defining function
    ss = [message.from_user.id]  # assigning user_id to 'ss' tuple
    conn = sqlite3.connect(config.adminBOTDB)  # connecting to adminBOTDB database.
    c = conn.cursor()  # defining connection cursor
    c.execute("""SELECT login 
        FROM users WHERE user_chat_id = ? 
        and last_login > 
        DateTime('Now', 'LocalTime', '-30 minutes')
        """, ss)  # querying database for active session of user with inputted user_id.
    if c.fetchone() is None:  # if output from previous step is 'None' (empty) then:
        bot.send_message(message.from_user.id,
                         'I did not recognized you.Please use /login %password% to authenticate.')
        return 201
    else:  # if active session found then
        return 101


def check_role(message):
    if check_auth(message) == 101:  # if authentication will complete with 101(Successful) code then
        conn = sqlite3.connect(config.adminBOTDB)  # connecting to adminBOTDB database.
        c = conn.cursor()  # defining connection cursor
        command = message.text  # assigning user message to variable

        # here and in next 3 lines steps to figure out requested command name
        ex_m = re.search(r'/(\w+)', command)
        if ex_m:
            a = ('/' + ex_m.group(1))
        zz = (a, message.from_user.id,)

        c.execute(
            """SELECT login  
            FROM USERS 
            U JOIN com_users 
            CU on CU.users_id = U.id 
            JOIN commands C on C.id = CU.roles_id 
            where C.desc = ? and U.user_chat_id = ?""",
            zz)  # querying if requested command in list of available to user command list.

        if c.fetchone() is None:  # if command is not in list of available to user then...
            # bot.send_message(message.from_user.id, 'You have no permission to execute this command...')
            conn.close()  # close db connection
            return 301
        else:  # else return successful result.
            conn.close()  # close db connection
            return 401
    else:
        return 606


# Function to check password validity
def check_password(message):
    try:
        # replacing '/login ' with empty string in message text.
        replace_login = str.replace(message.text, '/login ', '')
        key_string = replace_login.encode('utf-8')  # encoding to UTF-8
        pass_hash = hashlib.md5(key_string).hexdigest()  # hashing password to MD5
        t = (pass_hash,)  # hashed password to 't' tuple.
        conn = sqlite3.connect(config.adminBOTDB)  # connecting to adminBOTDB database.
        c = conn.cursor()  # defining connection cursor
        c.execute('SELECT login FROM users WHERE password = ?', t)  # selecting user with password inputted
        login = c.fetchone()[0]  # assigning
        t = (message.from_user.id, pass_hash,)  # updating 't' tuple with user id and hashed password.
        c.execute(
            """UPDATE users 
            set last_login = datetime(CURRENT_TIMESTAMP, 'localtime'),
            user_chat_id = ? where password = ?""",
            t)  # updating user 'last_login' TIMESTAMP with new one.
        bot.send_message(message.from_user.id, "Welcome " + login)  # Sending welcome message with user login.
        conn.commit()  # committing changes to database.
        conn.close()  # closing connection to database

    except:
        bot.send_message(message.from_user.id,
                         "Wrong password, please enter again again")  # if user not found then ask to check password
