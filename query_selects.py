from sqlalchemy.sql import func
from sqlalchemy import desc

from connect__to_db import session
from models import Student, Grade, Subject, Group, Teacher


def select_1():
    res = (
        session.query(
            Student.student_full_name,
            func.round(func.avg(Grade.grade), 2).label('avg_grade')
        ).
        select_from(Grade)
        .join(Student)
        .group_by(Student.student_id)
        .order_by(desc('avg_grade'))
        .limit(5)
        .all()
    )
    return res


def select_2(subject_id):
    res = (
        session.query(
            Student.student_id,
            Student.student_full_name,
            func.round(func.avg(Grade.grade), 2).label('average_grade')
        )
        .join(Grade, Student.student_id == Grade.student_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.student_id, Student.student_full_name)
        .order_by(func.avg(Grade.grade).desc())
        .limit(1)
        .all()
    )
    return res


def select_3(subject_id):
    res = (
        session.query(
            Student.group_id,
            Group.group_name,
            func.round(func.avg(Grade.grade), 2).label('average_grade')
        )
        .join(Grade, Student.student_id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.subject_id)
        .join(Group, Student.group_id == Group.group_id)
        .filter(Subject.subject_id == subject_id)
        .group_by(Student.group_id, Group.group_name)
        .all()
    )
    return res


def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2)).scalar()


def select_5(teacher_id):
    res = (
        session.query(Subject.subject_name, Teacher.teacher_full_name)
        .join(Teacher, Subject.teacher_id == Teacher.teacher_id)
        .filter(Teacher.teacher_id == teacher_id)
        .all()
    )
    return res


def select_6(group_id):
    res = (
        session.query(Student.student_full_name, Group.group_name)
        .join(Group, Student.group_id == Group.group_id)
        .filter(Group.group_id == group_id)
        .order_by(Student.student_full_name)
        .all()
    )
    return res


def select_7(group_id, subject_id):
    res = (
        session.query(
            Student.student_full_name,
            Group.group_name,
            Subject.subject_name,
            Grade.grade
        )
        .join(Student, Grade.student_id == Student.student_id)
        .join(Group, Student.group_id == Group.group_id)
        .join(Subject, Grade.subject_id == Subject.subject_id)
        .filter(Student.group_id == group_id, Subject.subject_id == subject_id)
        .all()
    )
    return res


def select_8(teacher_id):
    res = (
        session.query(
            Teacher.teacher_full_name,
            func.round(func.avg(Grade.grade), 2).label('average_grade')
        )
        .join(Subject, Teacher.teacher_id == Subject.teacher_id)
        .join(Grade, Subject.subject_id == Grade.subject_id)
        .filter(Teacher.teacher_id == teacher_id)
        .group_by(Teacher.teacher_full_name)
        .all()
    )
    return res


def select_9(student_id):
    res = (
        session.query(
            Student.student_id,
            Student.student_full_name,
            Subject.subject_name
        )
        .join(Grade, Student.student_id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.subject_id)
        .filter(Student.student_id == student_id)
        .distinct()
        .all()
    )
    return res


def select_10(student_id, teacher_id):
    res = (
        session.query(
            Student.student_full_name,
            Teacher.teacher_full_name,
            Subject.subject_name
        )
        .join(Grade, Student.student_id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.subject_id)
        .join(Teacher, Subject.teacher_id == Teacher.teacher_id)
        .filter(Student.student_id == student_id, Teacher.teacher_id == teacher_id)
        .distinct()
        .all()
    )
    return res


def select_11(student_id, teacher_id):
    res = (
        session.query(
            Teacher.teacher_full_name,
            Student.student_full_name,
            func.round(func.avg(Grade.grade), 2).label('avg_grade')
        )
        .join(Subject, Teacher.teacher_id == Subject.teacher_id)
        .join(Grade, Subject.subject_id == Grade.subject_id)
        .join(Student, Grade.student_id == Student.student_id)
        .filter(Student.student_id == student_id, Teacher.teacher_id == teacher_id)
        .group_by(Teacher.teacher_full_name, Student.student_full_name)
        .all()
    )
    return res


def select_12(subject_id, group_id):
    subquery = (
        session.query(func.max(Grade.date))
        .filter(Grade.subject_id == subject_id)
        .scalar()
    )
    res = (
        session.query(
            Group.group_name,
            Student.student_full_name,
            Subject.subject_name,
            Grade.grade,
            Grade.date
        )
        .join(Subject, Grade.subject_id == Subject.subject_id)
        .join(Student, Grade.student_id == Student.student_id)
        .join(Group, Student.group_id == Group.group_id)
        .filter(Subject.subject_id == subject_id, Group.group_id == group_id, Grade.date == subquery)
        .all()
    )
    return res


if __name__ == "__main__":
    result = select_12(1, 2)
    print(result)