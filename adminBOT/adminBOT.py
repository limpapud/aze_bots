from telebot import TeleBot as Tb  # Telegram API
import os  # native os library for Operating system functions
import psutil  # process and system monitoring library
import glob  # dealing with paths
import subprocess  # running commands (Windows  / UNIX)
import time  # library for time operations.
import sqlite3  # SQLite for database operations
import hashlib  # hashing into MD5

import audit_functions  # security functions
import config  # configuration file


bot = Tb(config.token)  # API token


# handler for cases with '/login"
# command where user authenticates into adminBOT
@bot.message_handler(commands=['login'])
def vb_reply(message):
    try:
        a = str.replace(message.text, '/login ', '')  # replacing '/login' in input string by empty string
        MAS = a.encode('utf-8')  # encoding with UTF-8
        hash = hashlib.md5(MAS).hexdigest()  # hashing into MD5

        conn = sqlite3.connect(config.adminBOTDB)  # connecting to SQLlite BD
        c = conn.cursor()  # creating cursor from connection.

        # executing qurerry to find out users with this password
        sql_query = 'SELECT login FROM users WHERE password = "%s"' % hash
        print(sql_query)
        c.execute(sql_query)

        login = c.fetchone()[0]  # getting login of authenticated user
        t = (message.from_user.id, hash,)  # updating tuple with new values for next query

        # updating "last_login" timestamp with CURRENT_TIMESTAMP
        c.execute("""UPDATE users set 
        last_login = datetime(CURRENT_TIMESTAMP, 'localtime'),
        user_chat_id = ? where password = ?""", t)

        bot.send_message(message.from_user.id, "Welcome " + login)  # Greeting user with his Login
        conn.commit()  # Committing changes to DB
        conn.close()  # Closing connection to DB
    except Exception as e:  # If error occurs then..
        # ..then send this message to user
        bot.send_message(message.from_user.id, "Wrong password, please enter again again")
        print(e)


# handler for cases with '/runcmd" command where user enters cmd/bash string.
@bot.message_handler(commands=['runcmd'])
def send_runcmd(message):
    # if user is authorised to use this command then move to the lines
    if audit_functions.check_role(message) == 401:
        # replacing '/runcmd' in input string by empty string
        command = str.replace(message.text, '/runcmd ', '')
        # Notification about start of execution with name of command
        bot.send_message(message.from_user.id, '"' + command + '" command execution started...')
        try:
            subprocess.run(command)  # try to start command
            bot.send_message(message.from_user.id, 'Successfully executed ')  # execution completed
        except:
            # execution failed due to some typo or other problem
            bot.send_message(message.from_user.id, 'Error happened while execution '
                                                   'of requested command. '
                                                   'Please check for permissions or typos in command')
    else:
        # if not authorised then return 'No permission to execute' message
        bot.send_message(message.from_user.id, 'You have no permission to execute this command...')


@bot.message_handler(commands=['start'])  # handler for cases with '/start" command where user gets to know about bot.
def send_start(message):
    bot.send_photo(message.from_user.id,
                   'https://for24.ru/uploads/posts/vsefoto/telegram-bot1.png',
                   caption='adminBOT v091217T1553')
    bot.send_message(message.from_user.id,
                     'Welcome to adminBOT, please select '
                     'command among other  \n  \n '
                     'List of all commands:\n /restart_oo - Restart OpenOffice service \n'
                     ' /systeminfo System information \n'
                     ' /runcmd %command% to run CMD or Bash command \n'
                     '  \n Backup and archiving: \n'
                     ' /videobackup Video recording backup \n'
                     ' /mysql_backup MySQL Database backup')


# Handler for cases with '/restart_oo" command that restarts OpenOffice service.
@bot.message_handler(commands=['restart_oo'])
def oo_reply(message):
    if audit_functions.check_role(message) == 401:  # if user is authorised to use this command then move to the lines
        bot.send_message(message.from_user.id, "Stopping service...")
        os.startfile(config.script_fd + 'restart_oo.bat')  # executing 'restart_oo.bat' batch file from 'BATs' folder.
        bot.send_message(message.from_user.id, "Starting service")
        # ToDo Add Successfully operation check
    else:
        # if not authorised then return ' No permission to execute' message
        bot.send_message(message.from_user.id, 'You have no permission to execute this command...')


# Handler for cases with '/systeminfo" command that outputs information about server.
@bot.message_handler(commands=['systeminfo'])
def si_reply(message):
    # if user is authorised to use this command then move to the lines
    if audit_functions.check_role(message) == 401:
        # sending 'Gathering information ...' message
        bot.send_message(message.from_user.id, "Gathering information ...")

        RAM_BUSY = str(psutil.virtual_memory().percent)  # assigning RAM busy % to RAM BUSY variable
        C_DISK_BUSY = str(psutil.disk_usage('C:/').percent)  # assigning C drive busy % to C_DISK_BUSY variable
        D_DISK_BUSY = str(psutil.disk_usage('D:/').percent)  # assigning D drive busy % to D_DISK_BUSY variable
        CPU_BUSY = 0
        for x in range(10):  # iterating to...
            CPU_BUSY = CPU_BUSY + psutil.cpu_percent(interval=1)  # to get information about 10 second period CPU busy %
        CPU_BUSY = str(
            round(CPU_BUSY / 10, 2))  # dividing output from previous step to number of seconds to get average

        # outputting and sending information gathered to user.
        bot.send_message(message.from_user.id,
                         'CPU busy: ' + CPU_BUSY + ' % \n'
                             'C:\ drive busy: ' + C_DISK_BUSY + ' % \n'
                              'D:\ drive busy: ' + D_DISK_BUSY + ' % \n'
                              'RAM busy: ' + RAM_BUSY + ' %')
        # ToDo Add Successfully operation check
        # ToDo What to add? Think about this.
    else:
        # if not authorised then return ' No permission to execute' message
        bot.send_message(message.from_user.id,
                         'You have no permission to execute this command...')


@bot.message_handler(
    # handler for cases with '/systeminfo" command that outputs information about server.
    commands=['videobackup'])
def vb_reply(message):
    # if user is authorised to use this command then move to the lines
    if audit_functions.check_role(message) == 401:
        bot.send_message(message.from_user.id, "Starting backup process...")
        os.startfile(
            # executing 'folderbackup.bat' batch file from 'BATs' folder.
            config.script_fd + 'folderbackup.bat')
        time.sleep(4)  # wait for 75 seconds (look at ToDo below
        bot.send_message(message.from_user.id, "Backup process has ended. Please check logs...")

        # looking for files with '.log' extension in config.vbackup_logfolder folder.
        v_logfile = glob.glob(
            config.vbackup_logfolder + '*.log')
        # checking and choosing the file with maximum TIMESTAMP (i.e youngest one)
        youngest_log = max(v_logfile,
                           key=os.path.getctime)

        # fixing full path to log file by replacing '\' by '/'
        youngest_log = str.replace(youngest_log, '\\', '/')

        # opening file and assigning FileStream to file_to_send variable
        file_to_send = open(youngest_log, 'rb')
        # sending logfile to user
        bot.send_document(message.chat.id, file_to_send)
        # ToDo Add Successfully operation check
    else:
        # if not authorised then return ' No permission to execute' message
        bot.send_message(message.from_user.id,
                         'You have no permission to execute this command...')


@bot.message_handler(
    # handler for cases with '/systeminfo" command that outputs information about server.
    commands=['mysql_backup'])
def vb_reply(message):
    if audit_functions.check_role(message) == 401:  # if user is authorised to use this command then move to the lines
        bot.send_message(message.from_user.id, "Starting backup process...")
        os.startfile(
            config.script_fd + 'mysql_backup.bat')  # executing 'mysql_backup.bat' batch file from 'BATs' folder.
        time.sleep(75)  # wait for 75 seconds (look at ToDo)
        bot.send_message(message.from_user.id, "Backup process has ended. Please check logs...")
        mysql_logfile = glob.glob(
            # looking for files with '.log' extension in config.mysqlbackup_logfolder folder.
            config.mysqlbackup_logfolder + '*.log')

        # checking and choosing the file with maximum TIMESTAMP (i.e youngest one)
        youngest_log = max(mysql_logfile,
                           key=os.path.getctime)
        youngest_log = str.replace(youngest_log, '\\', '/')  # fixing full path to log file by replacing '\' by '/'
        file_to_send = open(youngest_log, 'rb')  # opening file and assigning FileStream to file_to_send variable
        bot.send_document(message.chat.id, file_to_send)  # sending logfile to user
        # ToDo Add Successfully operation check
    else:
        # if not authorised then return ' No permission to execute' message
        bot.send_message(message.from_user.id,
                         'You have no permission to execute this command...')


# handler for with unknown 'text' type intent.
@bot.message_handler(content_types=['text'])
def unknown_intent(message):
    # send user to /start menu
    bot.send_video(message.from_user.id, 'https://media.giphy.com/media/l41lXkx9x8OTM1rwY/giphy.gif',
                   caption='I have no clue how to speak with people. '
                           'Please use /start command to get list of possible commands.')


# start pooling for messages none-stop
bot.polling(none_stop=True)
