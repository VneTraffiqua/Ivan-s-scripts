# Скрипты для работы с базой данных электронного дневника.

## Начало работы
1. Запустите сервер командой:
```
python3 manage.py runserver
```

2. Создайте еще одно окно консоли и зайдите в Django Shell командой:
```
python3 manage.py shell
```

3. После того как вы окажитесь в shell, скопируйте все содержимое файла `main.py` в shell и два раза нажмите Enter.


## Описание скриптов

* **fix_marks**

Скрипт исправляет все плохие оценки ученика.
Пример использования скрипта:
```
fix_marks('Фролов Иван Григорьевич')
```

* **remove_chastisements**

Скрипт удаляет все замечания ученика.
Пример использования скрипта:
```
remove_chastisements('Фролов Иван Григорьевич')
```

* **create_commendation**

Скрипт добавляет рандомную похвалу ученику, на вход подается ФИО ученика и предмет по которому нужно сделать похвалу. Скрипт добавит похвалу к последнему уроку.
Пример использования скрипта:
```
create_commendation('Фролов Иван Григорьевич', 'Музыка')
```
