# adminBOT [![GitHub issues](https://img.shields.io/github/issues/limpapud/aze_bots.svg)](https://github.com/limpapud/aze_bots/issues) [![GitHub stars](https://img.shields.io/github/stars/limpapud/aze_bots.svg)](https://github.com/limpapud/aze_bots/stargazers) [![GitHub forks](https://img.shields.io/github/forks/limpapud/aze_bots.svg)](https://github.com/limpapud/aze_bots/network) [![GitHub license](https://img.shields.io/github/license/limpapud/aze_bots.svg)](https://github.com/limpapud/aze_bots/blob/master/LICENSE)
![alt text](https://github.com/limpapud/aze_bots/blob/master/adminBOT/assets/logo.png)

### Qısa məlumat:

**adminBOT** kiçik və orta çətinlikdə olan administrativ tapşırıqları həll etmək üçün istifadə oluna bilər. İstifadə olunan Telegram API-si [pyTelegramBotAPI]( https://github.com/eternnoir/pyTelegramBotAPI).

### İstifadə olunan kitabxanalar və dillər:

- [Python 3.6]( https://www.python.org/downloads/release/python-360/) - sadə olduğu qədər güclü programlaşdırma dili.
- [pyTelegramBotAPI]( https://github.com/eternnoir/pyTelegramBotAPI) - sadə amma çevik pyhton üzərində yazışmış Telegram APİ-si.
- [psutil]( https://github.com/giampaolo/psutil) - sistem monitorinqi və sistem resursları istifadəsi üçün istifadə olunan kitabxana.
- Batch.
- Python daxilində olan [os]( https://docs.python.org/2/library/os.html) modulu əməliyyat sistemi funksiyalarının istifadəsi üçün nəzərdə tutulmuş modul.
- Python daxilində olan [glob]( https://docs.python.org/3/library/glob.html) modulu unix tipli qısayol modulu.
- [SQLite]( https://www.sqlite.org/) modulu. Məlumat bazası kimi çıxış edir.
- Şifrələr və mesajlardan "hash"yaradılması üçün istifadə olunan [hashlib]( https://docs.python.org/2/library/hashlib.html) modulu.


### Bot ilə hal-hazırda mümkün tapşırıqlar:

- *arxivləşdirmə*
- *qovluq rezerv nüsxələrin çıxarılması*
- *məlumat bazası rezerv nüsxələrin çıxarılması*
- *sistem haqqında məlumatın alınması*
- *servislərin "restart"-ı*
- *Log faylların çat üzərindən göndərilməsi*
-  *xüsusi "***əmr modu***" əmrləri bilavasitə mesajdan icra edir.*

### Özəlliklər

- ***artırılmış təhlükəsizlik*** - *şifrlərin məlumat bazasında md5 (salt) vəziyyətində saxlanılması.*
- ***əlavə olunmuş məlumat bazası***- istifadəçi faylların və məlumatların çevik və yüngül SQLite məlumat bazasında saxlanılması.
- ***əmr əsasında təhlükəsizlik funksiyaları və mütərəqqi autentifikasiya & avtorizasiya alqoritmləri*** - hər bir verilmiş əmr avtorizasiya mexanizmından keçir. Hər bir istifadəçi üçün 30-dəqiqəlik sessiya yaradılması Sizi kənar şəxslərin əməllərinən qoruyur.


### Planlaşdırılan funksional:

- *SQL Sorğuların icrası*
- *"Webhook" istifadə olunması*
- *SQL Server Reporting Services integrasiyası (hesabatların icrası və çat üzərindən alınması)*
- *SQL Server Integration Services integration (tapşırıqların icrası)*


### Nümaiş
----------

![alt text](https://github.com/limpapud/aze_bots/blob/master/adminBOT/assets/demo.png)

Fayllar
-------------------
Mövcud faylların və qovluqların açığlaması aşağıdaki kimidir:

Əsas qovluq:

> - *adminBOT.py* - əsas bot faylı.
> - *config.py* - sazlamaların saxlandığı fayl.
> - *adminBOT.db* - bot üçün SQLite məlumat bazası.
> - *audit_functions.py* -  şifrə əsasında əsasında təhlükəsizlik funksiyaları və autentifikasiya & avtorizasiya mexanizmləri.

**BATs** qovluğu
> - *folderbackup.bat* - qovluqlardan faylların yaşına uyğun yerdəyişməsi.
> - *mysql_backup.bat* - MySQL Məlumat Bazalarından sürət çıxarma üçün batch fayl.
> - *restart_oo.bat* - serverdə servisin restartı üçün batch fayl.

İştirak və tövhə vermə
----------------------
Lahiyədə iştirak edib tövhə vermək istəyirsən? Əla! Bunun üçün **Fork** edib lahiyəni öz hesabınıza keçirib tövhələrinizi əlavə edib **Pull** sorğuların edə bilərsiniz.

> **Əlavələr:**
> - Müəllif  istənilən həcmdə tövhəni dəyərləndirir.
> - Təklif və iradları səhifə sonunda qeyd olumuş elektron ünvana və ya **Issues** -ə əlavə ilə qeyd edə bilərsiniz.


İstifadə
-------------
Lahiyə **MIT** lisenziyası ilə yayımlanır.
> **Bu deməkdir ki:**
> - **Kommersiya** məqsədi ilə istifadə etmək **icazəniz var**
> - Dəyişmək **icazəniz var**
> - Yenidən bölüşmək **icazəniz var**
> - Şəxsi məqsədlərdə istifadəyə **icazəniz var**
> - Müəllif heç bir **zəmanət vermir**
> - Müəllif heç bir **məhsuliyyət daşımır**
> - İstifadə olunan zaman istifadə olunan lisenziya və müəllif hüquqları **qeyd olunmalıdır!**


### Əlaqə

Müəllif ilə əlaqə [![](https://www.shareicon.net/data/16x16/2015/11/02/665918_email_512x512.png)](mailto:omarbayramov@hotmail.com) **omarbayramov@hotmail.com** elektron ünvan üzərindən aparıla bilər.
Əlavə olaraq sosial şəbəkə və digər saytlara linklər əlavə olunur.

[Facebook![](https://www.shareicon.net/data/32x32/2016/06/20/606800_facebook_48x48.png)](https://www.facebook.com/Omar.X.Bayramov)
[Wordpress![](https://www.shareicon.net/data/32x32/2016/07/14/606997_wordpress_64x64.png)](https://omarbayramov.wordpress.com/) [LinkedIn![](https://www.shareicon.net/data/32x32/2016/06/20/606446_linkedin_48x48.png)](https://www.linkedin.com/in/omarbayramov/)
