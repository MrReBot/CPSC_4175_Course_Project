import sys
sys.path.insert(1, '../..') # Makes it so we can access Database.py
import Database
db = Database.Database("../../database.txt")

# This just checks if any prerequisites cause a recursion Loop
# Games Programming II and Game Jam are an example of one of the loops
concurrent_courses = []
for course in db.all_courses():
    coursename = str(course)
    for prereq in course.get_prereq():
        prereq = db.get_course(prereq)
        if prereq not in [None, "LAST-Year"] and coursename in prereq.get_prereq():
            #print(course.format() , "<->", prereq.format())
            concurrent_courses.append([course,prereq])

for group in concurrent_courses:
    group[0].add_concurrent(group[1])

db.save()