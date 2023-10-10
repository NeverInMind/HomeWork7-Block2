DROP TABLE IF EXISTS groups CASCADE;
CREATE TABLE groups (
        group_id SERIAL PRIMARY KEY,
        group_name VARCHAR(20)
    );
    
DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
        student_id SERIAL PRIMARY KEY,
        student_full_name VARCHAR(100) NOT NULL,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups (group_id)
    );
    
DROP TABLE IF EXISTS teachers CASCADE;
CREATE TABLE teachers (
        teacher_id SERIAL PRIMARY KEY,
        teacher_full_name VARCHAR(100) NOT NULL 
    );
    
DROP TABLE IF EXISTS subjects CASCADE;
CREATE TABLE subjects (
        subject_id SERIAL PRIMARY KEY,
        subject_name VARCHAR(100) NOT NULL,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
    );
    
DROP TABLE IF EXISTS grades CASCADE;
CREATE TABLE grades (
        grade_id SERIAL PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER NOT NULL,
        date DATE NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students (student_id),
        FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
    );