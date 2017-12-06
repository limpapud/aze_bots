robocopy %Mənbə% %Təyinat% /MOV /LOG:%Log təyinat qovluğu%\BackupLog_%DATE%_%time:~0,2%_%time:~3,2%.Log /minage:7
REM Uğurlu prosses üçün lazimi dəyərləri əlavə edin.
REM Daha ətraflı məlumat üçün "robocopy /?"-dən istifadə edin.
REM Batch Mənbə govuğundan 7 gündən "köhnə" faylları götürüb Təyinat qovluğuna yerləşdirir.
REM Prosses əsnasında baş verən əməliyyatlar Log təyinat qovluğunda yerləşəcək vaxt möhürü ilə adlandırılan fayl içərisinə yazılır.
