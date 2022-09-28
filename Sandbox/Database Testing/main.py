import re
import json
import sys
sys.path.insert(1, '../..') # Makes it so we can access Database.py
import Database
db = Database.Database("../../database.txt")


def get_value(course, last_course=None):
    i = 0
    if last_course == None:
        last_course = [course]
    for c in db.all_courses():
        if course.format() in c.get_prereq() and c.format() not in last_course:
            i+= 1
            last_course.append(c.format())
            i += get_value(c.format(),last_course[-2:])
    return i

def main():
    temp = {}
    #print(db.all_courses())
    for course in db.all_courses(sort=True):
        #c = db.get_course(course)
        value = get_value(course.format())
        #value = course.get_value()
        print(f"{course.format()}: {course.get_value()}")

    
main()