from telebot import TeleBot as tb
import config
import sqlite3
import re
bot = tb(config.token)


#function to check if user has current active session
def check_authentification(message): # defining function
        ss=(message.from_user.id,) # assinging user_id to 'ss' tuple
        conn = sqlite3.connect(config.adminBOTDB) # connecting to adminBOTDB database.
        c = conn.cursor() #defining connection cursor
        c.execute("""SELECT login FROM users WHERE user_chat_id = ? and last_login > DateTime('Now', 'LocalTime', '-30 minutes')""",ss) # querrying database for active session of user with inputted user_id.
        if c.fetchone() == None: # if output from previous step is 'None' (empty) then:
            bot.send_message(message.from_user.id, 'I did not recognized you.Please use /login %password% to authenticate.')
            return 201
        else: # if active session found then
            return 101
        conn.close() #closing connection to database

def check_role(message):
    if check_authentification(message)==101: # if authentification will complete with 101(Succsessfull) code then
        conn = sqlite3.connect(config.adminBOTDB) # connecting to adminBOTDB database.
        c = conn.cursor() #defining connection cursor
        commanda = message.text # assinging user message to variable
        ex_m = re.search(r'/(\w+)', commanda) # here and in next 3 lines steps to figure out requested command name
        if ex_m:
            a=('/' + ex_m.group(1))
        zz=(a,message.from_user.id,)
        c.execute("""SELECT login  FROM USERS U JOIN com_users CU on CU.users_id = U.id JOIN commands C on C.id = CU.roles_id where C.desc = ? and U.user_chat_id = ?""",zz) # querrying if requested command in list of available to user command list.
        if c.fetchone() == None: # if command is not in list of available to user then...
            bot.send_message(message.from_user.id, 'You have no permission to execute this command...')
            return 301
        else: #else return succsessfull result.
            return 401
        conn.close() #closing connection to database
    else:
        return 606


# Function to check password validity
def check_password(message):
    try:
        a = str.replace(message.text, '/login ', '') # replacing '/login ' with empty string in message text.
        key_string = a.encode('utf-8') # encoding to UTF-8
        hash = hashlib.md5(key_string).hexdigest() #hasing password to MD5
        t = (hash,) # hashed password to 't' tuple.
        conn = sqlite3.connect(config.adminBOTDB) # connecting to adminBOTDB database.
        c = conn.cursor() #defining connection cursor
        c.execute('SELECT login FROM users WHERE password = ?', t) # selecting user with password inputted
        login = c.fetchone()[0] # assigning
        t = (message.from_user.id, hash,) # updating 't' tuple with user id and hashed password.
        c.execute("""UPDATE users set last_login = datetime(CURRENT_TIMESTAMP, 'localtime'),user_chat_id = ? where password = ?""",t) # updating user 'last_login' TIMESTAMP with new one.
        bot.send_message(message.from_user.id, "Welcome " + login) # Sending welcome message with user login.
        conn.commit() # comitting changes to database.
        conn.close() #closing connection to database
    except:
        bot.send_message(message.from_user.id, "Wrong password, please enter again again") # if user not found then ask to check password