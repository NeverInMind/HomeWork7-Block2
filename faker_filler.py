from datetime import datetime, timedelta
import re
from random import randint

import faker
from connect_to_db import session
from models import Group, Teacher, Subject, Student, Grade


NUMBER_OF_TEACHERS = 4
NUMBER_OF_STUDENTS = 50
DBNAME = 'postgres'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'

fake = faker.Faker('uk-UA')


def seed_groups(cursor):
    groups = [('БДКН-15',), ('ФРЕЗ-23',), ('НГПУ-64',)]
    cursor.executemany('INSERT INTO groups (group_name) VALUES (%s)', groups)


def seed_teachers(cursor):
    teachers = [(re.sub(r'^пані? ', '', fake.name()),)
                for _ in range(NUMBER_OF_TEACHERS)]
    cursor.executemany(
        'INSERT INTO teachers (teacher_full_name) VALUES (%s)', teachers)


def seed_subjects(cursor):
    subjects = [
        ('Програмування', randint(1, NUMBER_OF_TEACHERS)),
        ('Вища математика', randint(1, NUMBER_OF_TEACHERS)),
        ('Економіка', randint(1, NUMBER_OF_TEACHERS)),
        ('Англійська мова', randint(1, NUMBER_OF_TEACHERS)),
        ('Філософія', randint(1, NUMBER_OF_TEACHERS)),
        ('Маркетинг', randint(1, NUMBER_OF_TEACHERS)),
        ('Креслення', randint(1, NUMBER_OF_TEACHERS)),
    ]
    cursor.executemany(
        'INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s)', subjects)


def seed_students(cursor):
    students = [
        (re.sub(r'^пані? ', '', fake.name()), randint(1, 3))
        for _ in range(NUMBER_OF_STUDENTS)
    ]

    cursor.executemany(
        'INSERT INTO students (student_full_name, group_id) VALUES (%s, %s)', students)


def seed_grades(cursor):
    grades = [
        (randint(1, 50), randint(1, 5), randint(1, 100),
         (datetime(2023, 1, 1) + timedelta(days=randint(0, 364))).strftime('%Y-%m-%d'))
        for _ in range(1000)
    ]

    cursor.executemany(
        'INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s)', grades)


def main():
    seed_groups()
    seed_teachers()
    seed_subjects()
    seed_students()
    seed_grades()

    session.commit()


if __name__ == '__main__':
    main()