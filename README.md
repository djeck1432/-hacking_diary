# Взлом дневника 

Данный скрипт предназначен для взлома электронного дневника. Он умеет: <br>
```Удалять плохие оценки и менять их на 5``` <br>
```Удалять замечания ```<br>
```Добавлять похвалу ```

## Инструкция скрипта

В коде есть 3 разные функции, а именно : <br>
```fix_marks ``` - удаляет плохие оценки и меняет их на 5;<br>
```remove_chastisements ``` - удаляет замечания ;<br>
```create_commendation ``` - добавляет случайным образом одну из 30 фраз, для похвалы;<br>

#### Аргументы функций и их значения 

``` schoolkid``` - фамилия и имя ученика, которому хотим исправить что-то; <br>
```name_of_lesson``` -  названия урока;<br>  

## Инструкция по запуску скрипта 

Для того, что бы внести изменения , вам нужно открыть ```shell``` у себя в консоле/терминале следующем образом :<br>
```python manage.py shell ```<br>
После выполнения данной команды, вы увидите у себя следующее:<br>
``` Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```
<br>
Следующем шагом, выберите нужну вам функцию и подставте значения, которые вам нужно ("Фролов Иван" пример)

```  from datacenter.models import Schoolkid
     from datacenter.models import Mark 
     from datacenter.models import Chastisement
     from datacenter.models import Lesson
     from datacenter.models import Commendation
     import random

     def fix_marks(schoolkid):
          child = Schoolkid.objects.get(full_name__contains=schoolkid)
          bad_mark = Mark.objects.filter(schoolkid = child, points__lt=4)
          for mark in bad_mark:
            mark.points = 5
            mark.save()

     fix_marks(schoolkid)
```

В функции ```fix_marks(schoolkid)``` ,
<br>
где аргумент - ```schoolkid``` фамилия и имя ученика, которому вы хотите исправить оценки;
<br>
После того, как вы задали аргумент ```schoolkid```, скопируйте код и вставте в терминале.
<br>
Готово, теперь у вас нету 2 и 3, а вместо них, одни 5.

