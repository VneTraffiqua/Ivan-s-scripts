import random
from datacenter.models import Mark, Chastisement, Schoolkid, Lesson, Commendation


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(
        schoolkid__full_name__contains=schoolkid,
        points__in=[1, 2, 3]
    )
    for bad_mark in bad_marks:
        Mark.points = 5
        bad_mark.save()


def remove_chastisements(schoolkid):
    chastiments = Chastisement.objects.filter(
        schoolkid__full_name__contains=schoolkid
    )
    chastiments.delete()


def create_commendation(schoolkid, lesson):
    try:
        commendations = [
            'Теперь у тебя точно все получится!',
            'Ты многое сделал, я это вижу!',
            'Ты растешь над собой!',
            'Я вижу, как ты стараешься!',
            'Мы с тобой не зря поработали!',
            'С каждым разом у тебя получается всё лучше!',
            'Я тобой горжусь!',
            'Это как раз то, что нужно!',
            'Замечательно!',
            'Очень хороший ответ!',
            'Талантливо!',
            'Ты меня приятно удивил!'
            ]
        schoolkid = Schoolkid.objects.get(full_name=schoolkid)
        desired_lesson = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=lesson
        ).last()
        Commendation.objects.create(
            text=random.choice(commendations),
            created=desired_lesson.date,
            schoolkid=schoolkid,
            teacher=desired_lesson.teacher,
            subject=desired_lesson.subject
        )

        create_commendation('Фролов Иван Григорьевич', 'История')
    except:
        print('Введите корректные данные!')
