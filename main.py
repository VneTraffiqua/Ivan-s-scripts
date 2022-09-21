import random
from datacenter.models import Mark, Chastisement, Schoolkid, Lesson, Commendation


def fix_marks(student_full_name):
    Mark.objects.filter(
        schoolkid__full_name__contains=student_full_name,
        points__in=[1, 2, 3]
    ).update(points=5)


def remove_chastisements(student_full_name):
    chastisements = Chastisement.objects.filter(
        schoolkid__full_name__contains=student_full_name
    )
    chastisements.delete()


def create_commendation(student_full_name, lesson):
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
        student_full_name = Schoolkid.objects.get(full_name=student_full_name)
        desired_lesson = Lesson.objects.filter(
            year_of_study=student_full_name.year_of_study,
            group_letter=student_full_name.group_letter,
            subject__title=lesson
        ).last()
        Commendation.objects.create(
            text=random.choice(commendations),
            created=desired_lesson.date,
            schoolkid=student_full_name,
            teacher=desired_lesson.teacher,
            subject=desired_lesson.subject
        )
    except:
        print('Введите корректные данные!')
