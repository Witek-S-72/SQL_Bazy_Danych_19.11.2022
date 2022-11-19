from sqlalchemy import create_engine, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()
session = sessionmaker()


class Student(Base):
    __tablename__ = 'Student'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(255))
    PESEL = Column(String(50), unique=True)  # co w przypadku alphanum? String?
    phone = Column(Integer)
    address = Column(String(255))


class StudentsGrades(Base):
    __tablename__ = 'StudentsGrade'

    enrollment_id = Column(Integer)
    student_id = Column(Integer, primary_key=True)
    course_id = Column(Integer)
    grade = Column(Float)


class Course(Base):
    __tablename__ = 'Course'

    course_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    credits = Column(String(255))
    departamen_id = Column(Integer)
    start_date = Column(DateTime(),default = datetime.now )  # default = now, _get_date, lub objekt datetime ?
    end_date = Column(DateTime(), default = datetime.now, onupdate = datetime.now)
    price = Column(Float)


class OnlineCourse(Base):
    __tablename__ = 'OnlineCourse'

    course_id = Column(Integer, primary_key=True)
    url = Column(String(255))


class OnsiteCourse(Base):
    __tablename__ = 'OnsiteCourse'

    course_id = Column(Integer, primary_key=True)
    address = Column(String(255))
    days = Column(Integer)
    time = Column(Integer)


class Administrator(Base):
    __tablename__ = 'Administrator'

    stuff_id = Column(Integer, primary_key=True, unique=True)
    departament_id = Column(Integer)
    enrollment_date = Column(DateTime(), default = datetime.now, onupdate = datetime.now)


class Departament(Base):
    __tablename__ = 'Departament'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    budget = Column(Float)
    address = Column(String(255))


class Staff(Base):
    __tablename__ = 'Staff'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(255))
    enrollment_date = Column(DateTime(), default = datetime.now, onupdate = datetime.now)
    PESEL = Column(String(50), unique=True)
    phone = Column(Integer)
    address = Column(String(255))


class CourseInstructor(Base):
    __table_name__ = 'CourseInstructor'

    course_id = Column(Integer)
    stuff_id = Column(Integer)
    enrollment_date = Column(DateTime(), default = datetime.now, onupdate = datetime.now)
