####################################################
# Name: Besher Kitaz
# username: kitazb
#
# CSC: 226
#
####################################################
#
#
# Inspired by: https://docs.google.com/document/d/1ww0ajH0ahH8wBKCp3uY6fe_THjE8BJZ_3iYgnOO8ovg/edit?tab=t.0#heading=h.qg98s23ap4mh
#
#
####################################################


import sqlite3

from user import User

DATABASE = "registration.db"

class Course:

    def __init__(self, key):
        """
        Creates an Object that relates to a record in the Users database.
        :param key: The key or id of the user in the database
        """
        self.con = sqlite3.connect(DATABASE)
        self.cursor = self.con.cursor()
        self.key = key
        self.name = self.retrieve_data()[0]  # Retrieves the name form the database
        self.crn = self.retrieve_data()[1] # Retrieves the crn form the database
        self.con.close()

    def retrieve_data(self):
        """
        Retrieves the data from the database for the user
        :return: A Tuple of the user data from the record
        """
        con = sqlite3.connect(DATABASE)
        self.cursor = con.cursor()
        self.cursor.execute("SELECT * FROM Courses WHERE id = ?", (self.key,))
        self.data = self.cursor.fetchone() # Retrieves name, crn and id as a Tuple
        con.close()
        return self.data

    def close_connection(self):
        """
        Closes connection to the database
        :return:
        """
        self.con.close()




def course_list():
    """
    Returns a list of all courses
    :return: a list of all course objects
    """
    con = sqlite3.connect(DATABASE)
    cursor = con.cursor()
    sql_query = "SELECT * FROM Courses ORDER BY id;"
    cursor.execute(sql_query)
    courses = cursor.fetchall()

    # Converts the data into objects
    courses_list = list()
    for course in courses:
        course_objects = Course(course[2])
        courses_list.append(course_objects)

    return courses_list




def create_course(name, crn):
    """
    Create a course in the database and returns as a Course object
    :param name: name of the course
    :param crn: crn of the course
    :return: a Course Object
    """
    con = sqlite3.connect(DATABASE)
    cursor = con.cursor()
    add_query = "INSERT INTO Courses (name, crn) VALUES (?, ?)"
    cursor.execute(add_query, (name, crn))
    con.commit()
    cursor.execute("SELECT * FROM Courses ORDER BY id DESC LIMIT 1;")
    name, crn, id = cursor.fetchone()
    course = Course(id)
    con.commit()
    con.close()
    return course
