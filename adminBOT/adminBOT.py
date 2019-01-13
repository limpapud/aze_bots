from telebot import TeleBot as tb  # Telegram API
from telebot import types
import os  # native os library for Operating system functions
import config  # configuration file
import psutil  # process and system monitoring library
import glob  # dealing with paths
import subprocess  # running commands (Windows  / UNIX)
import time  # library for time operations.
import sqlite3  # SQLite for database operations
import hashlib  # hashing into MD5
import audit_functions  # security functions
bot = tb(config.token)  # API token

@bot.message_handler(commands=['login'])  # handler for cases with '/login" command where user authenticates into adminBOT
def vb_reply(message):
    try:
        a = str.replace(message.text, '/login ', '')  # replacing '/login' in input string by empty string
        MAS = a.encode('utf-8')  # encoding with UTF-8
        hash = hashlib.md5(MAS).hexdigest()  # hashing into MD5
        t = (hash,)  # assinging hashed password to tuple
        conn = sqlite3.connect(config.adminBOTDB)  # connecting to SQLlite BD
        c = conn.cursor()  # creating cursor from connection.
        c.execute('SELECT login FROM users WHERE password = ?', t)  # executing qurerry to find out users with this password
        login = c.fetchone()[0]  # getting login of authenticated user
        t = (message.from_user.id, hash,)  # updating tuple with new values for next querry
        c.execute("""UPDATE users set last_login = datetime(CURRENT_TIMESTAMP, 'localtime'),user_chat_id = ? where password = ?""", t)  # updating "last_login" timestamp with CURRENT_TIMESTAMP
        bot.send_message(message.from_user.id, "Welcome " + login)  # Greeting user with his Login
        conn.commit()  # Committing changes to DB
        conn.close()  # Closing connection to DB
    except:  # If error occurs then..
        bot.send_message(message.from_user.id, "Wrong password, please enter again again")  # ..then send this message to user


@bot.message_handler(commands=['runcmd'])  # handler for cases with '/runcmd" command where user enters cmd/bash string.
def send_runcmd(message):
    if audit_functions.check_role(message) == 401:  # if user is authorised to use this command then move to the lines
        command = str.replace(message.text,'/runcmd ', '')  # replacing '/runcmd' in input string by empty string
        bot.send_message(message.from_user.id,'"' + command + '" command execution started...')  # Notification about start of execution with name of command
        try:
            subprocess.run(command)  # try to start command
            bot.send_message(message.from_user.id, 'Successfully executed ')  # execution completed
        except:
            bot.send_message(message.from_user.id, 'Error happened while execution of requested command. Please check for permissiond or typos in command')  # execution failed due to some typo or other problem
    else:
        bot.send_message(message.from_user.id, 'You have no permission to execute this command...')  # if not authorised then return ' No permission to execute' message


@bot.message_handler(commands=['start'])  # handler for cases with '/start" command where user gets to know about bot.
def send_start(message):
    bot.send_photo(message.from_user.id, 'https://for24.ru/uploads/posts/vsefoto/telegram-bot1.png',caption='adminBOT v091217T1553')
    bot.send_message(message.from_user.id,' Welcome to adminBOT, please select command among other  \n  \n List of all commands:\n /restart_oo - Restart OpenOffice service \n /systeminfo System information \n /runcmd %command% to run CMD or Bash command \n  \n Backup and archiving: \n /videobackup Videorecording backup \n /mysql_backup MySQL Database backup')


@bot.message_handler(commands=['restart_oo'])  # handler for cases with '/restart_oo" command that restarts OpenOffice service.
def oo_reply(message):
    if audit_functions.check_role(message) == 401:  # if user is authorised to use this command then move to the lines
        bot.send_message(message.from_user.id, "Stopping service...")
        os.startfile(config.script_fd + 'restart_oo.bat')  # executing 'restart_oo.bat' batch file from 'BATs' folder.
        bot.send_message(message.from_user.id, "Starting service")
        # ToDo Add Successfully operation check
    else:
        bot.send_message(message.from_user.id, 'You have no permission to execute this command...')  # if not authorised then return ' No permission to execute' message


@bot.message_handler(commands=['systeminfo'])  # handler for cases with '/systeminfo" command that outputs information about server.
def si_reply(message):
    if audit_functions.check_role(message) == 401:  # if user is authorised to use this command then move to the lines
        bot.send_message(message.from_user.id, "Gathering information ...")  # sending 'Gathering information ...' message
        RAM_BUSY = str(psutil.virtual_memory().percent)  # assigning RAM busy % to RAM BUSY variable
        C_DISK_BUSY = str(psutil.disk_usage('C:/').percent)  # assigning C drive busy % to C_DISK_BUSY variable
        D_DISK_BUSY = str(psutil.disk_usage('D:/').percent)  # assigning D drive busy % to D_DISK_BUSY variable
        CPU_BUSY = 0
        for x in range(10):  # iterating to...
            CPU_BUSY = CPU_BUSY + psutil.cpu_percent(interval=1)  # to get information about 10 second period CPU busy %
        CPU_BUSY = str(round(CPU_BUSY / 10, 2))  # dividing output from previous step to number of seconds to get average
        bot.send_message(message.from_user.id, 'CPU busy: ' + CPU_BUSY + ' % \nC:\ drive busy: ' + C_DISK_BUSY + ' % \nD:\ drive busy: ' + D_DISK_BUSY + ' % \nRAM busy: ' + RAM_BUSY + ' %')  # outputing and sending information gathered to user.
        # ToDo Add Successfully operation check
        # ToDo What to add? Think about this.
    else:
        bot.send_message(message.from_user.id, 'You have no permission to execute this command...')  # if not authorised then return ' No permission to execute' message

@bot.message_handler(commands = ['videobackup']) # handler for cases with '/systeminfo" command that outputs information about server.
def vb_reply(message):
    if audit_functions.check_role(message) == 401:  # if user is authorised to use this command then move to the lines
        bot.send_message(message.from_user.id, "Starting backup process...")
        os.startfile(config.script_fd + 'folderbackup.bat') #   executing 'folderbackup.bat' batch file from 'BATs' folder.
        time.sleep(4)  # wait for 75 seconds (look at ToDo below
        bot.send_message(message.from_user.id, "Backup process has ended. Please check logs...")
        v_logfile = glob.glob(config.vbackup_logfolder + '*.log')  # looking for files with '.log' extention in config.vbackup_logfolder folder.
        youngest_log = max(v_logfile, key=os.path.getctime)  # checking and choosing the file with maximum TIMESTAMP (i.e youungest one)
        youngest_log = str.replace(youngest_log, '\\', '/')  # fixing full path to log file by replacing '\' by '/'
        file_to_send = open(youngest_log, 'rb')  # opening file and assigning filestream to file_to_send variable
        bot.send_document(message.chat.id,file_to_send)  # sending logfile to user
        # ToDo Add Successfully operation check
    else:
        bot.send_message(message.from_user.id, 'You have no permission to execute this command...')  # if not authorised then return ' No permission to execute' message

@bot.message_handler(commands=['mysql_backup'])  # handler for cases with '/systeminfo" command that outputs information about server.
def vb_reply(message):
    if audit_functions.check_role(message) == 401:  # if user is authorised to use this command then move to the lines
        bot.send_message(message.from_user.id, "Starting backup process...")
        os.startfile(config.script_fd + 'mysql_backup.bat')  # executing 'mysql_backup.bat' batch file from 'BATs' folder.
        time.sleep(75)  # wait for 75 seconds (look at ToDo)
        bot.send_message(message.from_user.id, "Backup process has ended. Please check logs...")
        mysql_logfile = glob.glob(config.mysqlbackup_logfolder + '*.log')  # looking for files with '.log' extention in config.mysqlbackup_logfolder folder.
        youngest_log = max(mysql_logfile, key=os.path.getctime)  # checking and choosing the file with maximum TIMESTAMP (i.e youngest one)
        youngest_log = str.replace(youngest_log, '\\', '/')  # fixing full path to log file by replacing '\' by '/'
        file_to_send = open(youngest_log, 'rb')  # opening file and assigning filestream to file_to_send variable
        bot.send_document(message.chat.id,file_to_send)  # sending logfile to user
        # ToDo Add Successfully operation check
    else:
        bot.send_message(message.from_user.id, 'You have no permission to execute this command...')  # if not authorised then return ' No permission to execute' message


@bot.message_handler(content_types=['text'])  # handler for with unknown 'text' type intent.
def unknown_intent(message):
    bot.send_video(message.from_user.id, 'https://media.giphy.com/media/l41lXkx9x8OTM1rwY/giphy.gif', caption='I have no clue how to speak with people. Please use /start command to get list of possible commands.')  # send user to /start menu

bot.polling(none_stop=True)  # start pooling for messages none-stop