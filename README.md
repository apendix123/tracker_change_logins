# tracker_change_logins
Change tracker logins in author, assignee, followers fields
1. Получить токен и его вместе с айди организации вписать в скрипт. Он сгенерирует при первом запуске список всех пользователей и их id (from.txt)
2. На основе полученного файла (from.txt) сделать маппинг - вписать рядом с первым айди второй , сохранить в to.txt и запустить еще раз
3. Раскомментировать строки где применение изменений, без этого - в холостую будет работать 
4. Для верности несколько раз можно прогнать пока не перестанет находить задач со старыми пользователями (могут проскакивать ошибки и как следствие пропуски некоторых задач)

Запускать: python3 changelogins.py

Пример файла from.txt после первого запуска:
1130000012345678 # ivan@mydomain.com
87654321 # ivan@yandex.ru

Привер строки для замены доменной учетки на яндексовую в файле to.txt:
1130000012345678 87654321# 


