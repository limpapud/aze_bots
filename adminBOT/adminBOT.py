from telebot import TeleBot as tb
from telebot import types
import os
import config
import psutil
import glob
import subprocess
import time
import sqlite3
import hashlib
import audit_functions
bot = tb(config.token)

@bot.message_handler(commands=['login'])
def vb_reply(message):
    try:
        a = str.replace(message.text, '/login ', '')
        MAS = a.encode('utf-8')
        hash = hashlib.md5(MAS).hexdigest()
        t = (hash,)
        conn = sqlite3.connect(config.adminBOTDB)
        c = conn.cursor()
        c.execute('SELECT login FROM users WHERE password = ?', t)
        login = c.fetchone()[0]
        t = (message.from_user.id, hash,)
        c.execute("""UPDATE users set last_login = datetime(CURRENT_TIMESTAMP, 'localtime'),user_chat_id = ? where password = ?""", t)
        bot.send_message(message.from_user.id, "Xoş gəldin " + login)
        conn.commit()
        conn.close()
    except:
        bot.send_message(message.from_user.id, "Şifrə səhvdir")


@bot.message_handler(commands=['runcmd'])
def send_start(message):
    if audit_functions.check_role(message) == 401:
        command = str.replace(message.text,'/runcmd ', '')
        bot.send_message(message.from_user.id,'"' + command + '" komandası icra olunur...')
        try:
            subprocess.run(command)
            bot.send_message(message.from_user.id, 'Uğurla icra olundu')
        except:
            bot.send_message(message.from_user.id, 'Komanda səhvlə başa çatdı')
    else:
        bot.send_message(message.from_user.id, 'Icra etməyə icazə yoxdur...')


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_photo(message.from_user.id, 'https://for24.ru/uploads/posts/vsefoto/telegram-bot1.png',caption='AvtoBot v081217T0016')
    bot.send_message(message.from_user.id,'AvtoBot-a xoş gəldin, zəhmət olsa lazimi komandalar arasında lazım olanı seç  \n  \n Cari komanda siyahısı\n /restart_oo - OpenOffice servisin restartı \n /systeminfo Sistem haqqında məlumat \n  \n Rezerv nüsxələmə və arxivasiya \n /videobackup Videoyazıların nüsxələnmə prosessi \n /mysql_backup MySql məlumat bazalarının nüsxələmə prossesi')


@bot.message_handler(commands=['restart_oo'])
def oo_reply(message):
    if audit_functions.check_role(message)==401:
        bot.send_message(message.from_user.id, "Servis söndürülür...")
        os.startfile(config.script_fd + 'restart_oo.bat')
        bot.send_message(message.from_user.id, "Servis başlanır")
        #ToDo Müvəffəqiyyətli əməliyyat statusun əlavə et
    else:
        bot.send_message(message.from_user.id, 'Icra etməyə icazə yoxdur...')


@bot.message_handler(commands=['systeminfo'])
def si_reply(message):
    if audit_functions.check_role(message) == 401:
        bot.send_message(message.from_user.id, "Məlumat yığılır ...")
        RAM_BUSY = str(psutil.virtual_memory().percent)
        C_DISK_BUSY = str(psutil.disk_usage('C:/').percent)
        D_DISK_BUSY = str(psutil.disk_usage('D:/').percent)
        CPU_BUSY = 0
        for x in range(10):
            CPU_BUSY = CPU_BUSY + psutil.cpu_percent(interval=1)
        CPU_BUSY = str(round(CPU_BUSY / 10, 2))
        bot.send_message(message.from_user.id, 'CPU məşğul: ' + CPU_BUSY + ' % \nC:\ diski məşğul: ' + C_DISK_BUSY + ' % \nD:\ diski məşğul: ' + D_DISK_BUSY + ' % \nRAM məşğul: ' + RAM_BUSY + ' %')
        #ToDo Müvəffəqiyyətli əməliyyat statusun əlavə et
        #ToDo Daha nə əlavə etmək mümkündür? Fikirləş.
    else:
        bot.send_message(message.from_user.id, 'Icra etməyə icazə yoxdur...')

@bot.message_handler(commands = ['videobackup'])
def vb_reply(message):
    if audit_functions.check_role(message) == 401:
        bot.send_message(message.from_user.id, "Nüsxələmə başlanılır...")
        os.startfile(config.script_fd + 'folderbackup.bat')
        time.sleep(75)
        bot.send_message(message.from_user.id, "Nüsxələmə bitdi ...")
        v_logfile = glob.glob(config.vbackup_logfolder + '*.log')
        youngest_log = max(v_logfile, key=os.path.getctime)
        youngest_log = str.replace(youngest_log, '\\', '/')
        file_to_send = open(youngest_log, 'rb')
        bot.send_document(message.chat.id,file_to_send)
        #ToDo Müvəffəqiyyətli əməliyyat statusun əlavə et
    else:
        bot.send_message(message.from_user.id, 'Icra etməyə icazə yoxdur...')

@bot.message_handler(commands=['mysql_backup'])
def vb_reply(message):
    if audit_functions.check_role(message) == 401:
        bot.send_message(message.from_user.id, "Nüsxələmə başlanılır ...")
        os.startfile(config.script_fd + 'mysql_backup.bat')
        time.sleep(75)
        bot.send_message(message.from_user.id, "Nüsxələmə bitdi ...")
        mysql_logfile = glob.glob(config.mysqlbackup_logfolder + '*.log')
        youngest_log = max(mysql_logfile, key=os.path.getctime)
        youngest_log = str.replace(youngest_log, '\\', '/')
        file_to_send = open(youngest_log, 'rb')
        bot.send_document(message.chat.id,file_to_send)
        #ToDo Müvəffəqiyyətli əməliyyat statusun əlavə et
    else:
        bot.send_message(message.from_user.id, 'Icra etməyə icazə yoxdur...')


@bot.message_handler(content_types=['text'])
def unknown_intent(message):
    bot.send_video(message.from_user.id, 'https://media.giphy.com/media/l41lXkx9x8OTM1rwY/giphy.gif', caption='Məni helə yazdığını anlamaq üçün sazlamamısan, zəhmət olmasa /start seçib menyuya keç.')

bot.polling()