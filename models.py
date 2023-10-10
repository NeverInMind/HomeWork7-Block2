from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from connect_to_db import engine

Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, name='group_id')
    name = Column(String(20), name='group_name')


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, name='student_id')
    name = Column(String(100), nullable=False, name='student_full_name')
    group_id = Column(Integer, ForeignKey('groups.group_id'))

    group = relationship('Group', backref='students')


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, name='teacher_id')
    name = Column(String(100), nullable=False, name='teacher_full_name')


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, name='subject_id')
    name = Column(String(100), nullable=False, name='subject_name')
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))

    teacher = relationship('Teacher', backref='subjects')


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, name='grade_id')
    student_id = Column(Integer, ForeignKey('students.student_id'))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))
    grade = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)

    student = relationship('Student', backref='grades')
    subject = relationship('Subject', backref='grades')


Base.metadata.create_all(engine)
Base.metadata.bind = engine