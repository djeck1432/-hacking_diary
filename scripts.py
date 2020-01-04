from datacenter.models import Schoolkid
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

fix_makr(schoolkid)

def remove_chastisements(schoolkid):
  child = Schoolkid.objects.get(full_name__contains=schoolkid)
  chastisements = Chastisement.objects.filter(schoolkid=child)
  for chastisement in chastisements:
      chastisement.delete()

remove_chastisements(schoolkid)


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
