import sys
sys.path.insert(1, '../..') # Makes it so we can access Database.py
import Database
db = Database.Database("../../database.txt")

# This just checks if any prerequisites cause a recursion Loop
# Games Programming II and Game Jam are an example of one of the loops
for course in db.all_courses():
    coursename = str(course)
    for prereq in course.get_prereq():
        prereqs = db.get_course(prereq)
        if prereqs != None and coursename in prereqs.get_prereq():
            print(coursename)
