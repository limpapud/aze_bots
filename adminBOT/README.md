# adminBOT [![GitHub issues](https://img.shields.io/github/issues/limpapud/aze_bots.svg)](https://github.com/limpapud/aze_bots/issues) [![GitHub stars](https://img.shields.io/github/stars/limpapud/aze_bots.svg)](https://github.com/limpapud/aze_bots/stargazers) [![GitHub forks](https://img.shields.io/github/forks/limpapud/aze_bots.svg)](https://github.com/limpapud/aze_bots/network) [![GitHub license](https://img.shields.io/github/license/limpapud/aze_bots.svg)](https://github.com/limpapud/aze_bots/blob/master/LICENSE)
![alt text](https://github.com/limpapud/aze_bots/blob/master/adminBOT/assets/logo.png)
###  [Məqaləni Azərbaycanca oxumaq]( https://github.com/limpapud/aze_bots/blob/master/adminBOT/README_az.md)

### Brief information:

**adminBOT** is system administrator day-to-day small and medium size automation bot tool based on [pyTelegramBotAPI]( https://github.com/eternnoir/pyTelegramBotAPI). It can accomplish various tasks from launching simple backup process to switching off antivirus on domain computer.

### Languages and libraries used:

- [Python 3.6]( https://www.python.org/downloads/release/python-360/) - high-level programming language for general-purpose programming... but I do not think that this language needs any introduction.
- [pyTelegramBotAPI]( https://github.com/eternnoir/pyTelegramBotAPI) - a simple, but extensible Python implementation for the Telegram Bot API.
- [psutil]( https://github.com/giampaolo/psutil) - cross-platform lib for process and system monitoring in Python.
- Batch.
- [os]( https://docs.python.org/2/library/os.html) - module provides a portable way of using operating system dependent functionality.
-  [glob]( https://docs.python.org/3/library/glob.html) - unix style pathname pattern expansion.
- [SQLite]( https://www.sqlite.org/)-SQL database engine.
- [hashlib]( https://docs.python.org/2/library/hashlib.html) -module implements a common interface to many different secure hash and message digest algorithms.


### Tasks accomplished by bot:

- *archiving*
- *folder backup*
- *database backup*
- *system information gathering*
- *services restart*
- *geting logs about tasks  accomplised* 
- *special 'command line' mode for immediate Windows/Unix terminal*

### Bot features
- ***increased security*** - *passwords are stored in database as "salted" md5.*
- ***attached database***- possibility to save files and other information in lightweight database.
- ***command-based security functions and advanced authentication & authorization algorithms*** - every task is checked for authorization. 30-minute user-session applied for each command session. 

### Planned functionality:

- *SQL tasks execution*
- *SQL Server Reporting Services integration (report execution and report obtaining as chat attachment)*
- *SQL Server Integration Services integration (task execution)*
- "Webhook" usage

### Demo
----------

![alt text](https://github.com/limpapud/aze_bots/blob/master/adminBOT/assets/demo.png)

Files
-------------------
There is description of files in repository:

Main folder:

> - *adminBOT.py* - main bot file.
> - *adminBOT.db* - SQLite database for bot.
> - *config.py* - configuration file.
> - *audit_functions.py* -  password based authentication & authorization functions.

**BATs** folder
> - *folderbackup.bat* - file backup based on file age in folder.
> - *mysql_backup.bat* - MySQL Database backup.
> - *restart_oo.bat* - Windows service restart.

Contributions
----------------------
Want to contribute? That is great! Please **Fork** and **Pull** to main branch.

> **Notes:**
> - Author appreciates any size of contribution.
> - Have some **Issues** or thoughts to share? You can share it via opening *Issue* or sending an  email that is mentioned in the end of page to author.

Usage and Licencing
-------------
Project is distributed with **MIT** licence.
> **That mean that:**
> - This software and derivatives **may be used for commercial purposes**
> - This software **may be modified**
> - This software **may be distributed**
> - This software **may be used and modified in private**
> - This licence includes a **limitation of liability**
> - This licence explicitly states that it **DOES NOT provide any warranty**
> - A copy of the licence and copyright notice must be included with the software.


### Contact

You can contact with author through [![](https://www.shareicon.net/data/16x16/2015/11/02/665918_email_512x512.png)](mailto:omarbayramov@hotmail.com) **omarbayramov@hotmail.com** mail.
Additionaly I am adding links to social network accounts and blog.

[Facebook![](https://www.shareicon.net/data/32x32/2016/06/20/606800_facebook_48x48.png)](https://www.facebook.com/Omar.X.Bayramov) [Wordpress![](https://www.shareicon.net/data/32x32/2016/07/14/606997_wordpress_64x64.png)](https://omarbayramov.wordpress.com/) [LinkedIn![](https://www.shareicon.net/data/32x32/2016/06/20/606446_linkedin_48x48.png)](https://www.linkedin.com/in/omarbayramov/)
