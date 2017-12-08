from telebot import TeleBot as tb
import config
import sqlite3
import re
bot = tb(config.token)

def check_authentification(message):
        ss=(message.from_user.id,)
        conn = sqlite3.connect(config.adminBOTDB)
        c = conn.cursor()
        c.execute("""SELECT login FROM users WHERE user_chat_id = ? and last_login > DateTime('Now', 'LocalTime', '-1 minutes')""",ss)
        if c.fetchone() == None:
            bot.send_message(message.from_user.id, 'Sizi tanımadım, zəhmət olmasa /login %şifrə% daxil edin.')
            return 201
        else:
            return 101
        conn.close()

def check_role(message):
    if check_authentification(message)==101:
        conn = sqlite3.connect(config.adminBOTDB)
        c = conn.cursor()
        commanda = message.text
        match = re.search(r'/(\w+)', commanda)
        if match:
            a=('/' + match.group(1))

        zz=(a,message.from_user.id,)
        c.execute("""SELECT login  FROM USERS U JOIN com_users CU on CU.users_id = U.id JOIN commands C on C.id = CU.roles_id where C.desc = ? and U.user_chat_id = ?""",zz)
        if c.fetchone() == None:
            print(c.fetchone())
            print('Jopka')
            print(message.text)
            bot.send_message(message.from_user.id, 'İcra etmək üçün haqqınız çatmır.')
            return 301
        else:
            return 401
        conn.close()

def check_password(message):
    try:
        a = str.replace(message.text, '/login ', '')
        key_string = a.encode('utf-8')
        hash = hashlib.md5(key_string).hexdigest()
        t = (hash,)
        conn = sqlite3.connect(config.adminBOTDB)
        c = conn.cursor()
        c.execute('SELECT login FROM users WHERE password = ?', t)
        login = c.fetchone()[0]
        t = (message.from_user.id, hash,)
        c.execute("""UPDATE users set last_login = datetime(CURRENT_TIMESTAMP, 'localtime'),user_chat_id = ? where password = ?""",t)
        bot.send_message(message.from_user.id, "Xoş gəldin " + login)
        conn.commit()
        conn.close()
    except:
        bot.send_message(message.from_user.id, "Şifrə səhvdir")