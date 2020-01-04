# Взлом дневника 

Данный скрипт предназначен для взлома электронного дневника. Он умеет: <br>
```Удалять плохие оценки и менять их на 5``` <br>
```Удалять замечания ```<br>
```Добавлять похвалу ```

## Инструкция скрипта

В коде есть 3 разные функции, а именно: <br>
```fix_marks ``` - удаляет плохие оценки и меняет их на 5;<br>
```remove_chastisements ``` - удаляет замечания;<br>
```create_commendation ``` - добавляет случайным образом одну из 30 фраз, для похвалы;<br>

#### Аргументы функций и их значения 

``` schoolkid``` - фамилия и имя ученика, которому хотим исправить что-то; <br>
```name_of_lesson``` -  названия урока;<br>  

## Инструкция по запуску скрипта 

Для того, что бы внести изменения, вам нужно открыть ```shell``` у себя в консоле/терминале следующем образом:<br>
```python manage.py shell ```<br>
После выполнения данной команды, вы увидите у себя следующее:<br>
``` Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```
<br>
#### Пример запуска скрипта 

Следующем шагом, выберите нужную вам функцию и подставьте значения, которые вам нужно ("Фролов Иван" пример)

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

В функции ```fix_marks(schoolkid)```,
<br>
где аргумент - ```schoolkid``` фамилия и имя ученика, которому вы хотите исправить оценки;
<br>
После того, как вы задали аргумент ```schoolkid```, скопируйте код и вставьте в терминале.
<br>
Готово, теперь у вас нету 2 и 3, а вместо них, одни 5.
<br>
Eсли вы хотите удалить замечания, то тогда, нужно использовать следующую функцию: 
``` from datacenter.models import Schoolkid
    from datacenter.models import Mark 
    from datacenter.models import Chastisement
    from datacenter.models import Lesson
    from datacenter.models import Commendation
    import random
     
    def remove_chastisements(schoolkid):
        child = Schoolkid.objects.get(full_name__contains=schoolkid)
        chastisements = Chastisement.objects.filter(schoolkid=child)
        for chastisement in chastisements:
            chastisement.delete()

remove_chastisements(schoolkid)

```
Перед запуском скрипта, напишите свой аргумент ```schoolkid```, в функцию ```remove_chastisements()``` .
<br>
А если хотите похвалить себя, тогда нужно использовать следующий скрипт:
```from datacenter.models import Schoolkid
   from datacenter.models import Mark 
   from datacenter.models import Chastisement
   from datacenter.models import Lesson
   from datacenter.models import Commendation
   import random

   praise = ['Молодец!','Отлично!','Хорошо!','Гораздо лучше, чем я ожидал!','Ты меня приятно удивил!','Великолепно!','Прекрасно!','Ты меня очень обрадовал!','Именно этого я давно ждал от тебя!','Сказано здорово – просто и ясно!','Ты, как всегда, точен!','Очень хороший ответ!','Талантливо!','Ты сегодня прыгнул выше головы!','Я поражен!','Уже существенно лучше!'
,'Потрясающе!','Замечательно!','Прекрасное начало!','Так держать!','Ты на верном пути!','Здорово!','Это как раз то, что нужно!','Я тобой горжусь!','С каждым разом у тебя получается всё лучше!','Мы с тобой не зря поработали!','Я вижу, как ты стараешься!','Ты растешь над собой!','Ты многое сделал, я это вижу!','Теперь у тебя точно все получится!']

    def create_commendation(schoolkid,name_of_lesson):
       text = random.choice(praise)
       child = Schoolkid.objects.get(full_name__contains=schoolkid)
       child_year_of_study = child.year_of_study
       child_group_letter = child.group_letter 
       lesson_child = Lesson.objects.filter(
                                 year_of_study=child_year_of_study,
                                 group_letter= child_group_letter,
                                 subject__title=name_of_lesson
                                 )
       date = lesson_child[0].date
       teacher = lesson_child[0].teacher
       subject = lesson_child[0].subject
       commendation = Commendation.objects.create(
                                                 text = text,
                                                 created = date,
                                                 schoolkid = child,
                                                 subject = subject,
                                                 teacher = teacher
       )
       return print(commendation.text)

     create_commendation(schoolkid,name_of_lesson)
```
Перед запуском скрипта, в функции ```create_commendation()```, где два аргумента:<br>
 ```schoolkid``` - фамилия и имя ученика,<br>
```name_of_lesson``` - названия предмета<br>
Замените на свои. Готово, теперь у вас есть в дневнике новая похвала, поздравляю! 
