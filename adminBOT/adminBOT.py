from telebot import TeleBot as tb
import os
import config
import psutil
bot = tb(config.token)

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, 'AvtoBot v061217T2028 \n  \n AvtoBot-a xoş gəldin, zəhmət olsa lazimi komandalar arasında lazım olanı seç  \n  \n Cari komanda siyahısı\n /restart_oo - OpenOffice servisin restartı \n /systeminfo Sistem haqqında məlumat \n  \n Rezerv nüsxələmə və arxivasiya \n /videobackup Videoyazıların nüsxələnmə prosessi \n /mysql_backup MySql məlumat bazalarının nüsxələmə proseesis ')

@bot.message_handler(commands=['restart_oo'])
def oo_reply(message):
    bot.reply_to(message, "Servis söndürülür...")
    os.startfile(config.script_fd + 'restart_oo.bat')
    bot.reply_to(message, "Servis başlanır")
    #ToDo Müvəffəqiyyətli əməliyyat statusun əlavə et


@bot.message_handler(commands=['systeminfo'])
def si_reply(message):
    bot.reply_to(message, "Məlumat yığılır ...")
    RAM_BUSY = str(psutil.virtual_memory().percent)
    C_DISK_BUSY = str(psutil.disk_usage('C:/').percent)
    D_DISK_BUSY = str(psutil.disk_usage('D:/').percent)
    CPU_BUSY = 0
    for x in range(10):
        CPU_BUSY = CPU_BUSY + psutil.cpu_percent(interval=1)
    CPU_BUSY = str(round(CPU_BUSY / 10, 2))
    bot.reply_to(message, 'CPU məşğul: ' + CPU_BUSY + ' % \nC:\ diski məşğul: ' + C_DISK_BUSY + ' % \nD:\ diski məşğul: ' + D_DISK_BUSY + ' % \nRAM məşğul: ' + RAM_BUSY + ' %')
    #ToDo Müvəffəqiyyətli əməliyyat statusun əlavə et
    #ToDo Daha nə əlavə etmək mümkündür? Fikirləş.

@bot.message_handler(commands = ['videobackup'])
def vb_reply(message):
    bot.reply_to(message, "Nüsxələmə başlanılır...")
    os.startfile(config.script_fd + 'folderbackup.bat')
    bot.reply_to(message, "Nüsxələmə bitdi...")
    #ToDo Müvəffəqiyyətli əməliyyat statusun əlavə et
    #ToDo Logları Mail və/və ya Telegram vasitəsi ilə al


@bot.message_handler(commands=['mysql_backup'])
def vb_reply(message):
    bot.reply_to(message, "Nüsxələmə başlanılır ...")
    os.startfile(config.script_fd + 'mysql_backup.bat')
    bot.reply_to(message, "Nüsxələmə bitdi...")
    #ToDo Müvəffəqiyyətli əməliyyat statusun əlavə et
    #ToDo Logları Mail və/və ya Telegram vasitəsi ilə al


@bot.message_handler(content_types=['text'])
def unknown_intent(message):
    bot.send_video("384567868", 'https://media.giphy.com/media/l41lXkx9x8OTM1rwY/giphy.gif', caption='Məni helə yazdığını anlamaq üçün sazlamamısan, zəhmət olmasa /start seçib menyuya keç.')

bot.polling()
