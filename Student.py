import Database
import os
import datetime
import random
import Parser

class Student:
    remaining_courses = []
    completed_courses = []
    db = None
    tags = []
    def __init__(self, db):
        self.db = db

    def generate_completed(self):
        self.completed_courses = self.db.all_courses()
        self.tags=[]
        for course in self.remaining_courses:
            if self.db.course_exist(course):
                try:
                    self.completed_courses.remove(self.db.get_course(course))
                except ValueError:
                    pass
            elif self.db.tag_exist(course):
                self.tags.append(self.db.get_tag(course))
            else:
                print(f"{course} doesn't exist")

    def check_credits(self, courses)  -> int:
        """Check how many credits a given list, dir or course object has"""
        i = 0
        if type(courses) == list:
            for course in courses:
                i+= int(course.credits)
        elif type(courses) == dict:
            for course in courses:
                i+= int(courses[course].credits)
        elif type(courses) == Database.Course:
            i = int(courses.credits)
        return i

    def generate_semester(self, course_list: list, completed: list, season:str, credits=15):
        not_completed = course_list.copy() # Make a copy of the course list
        semester = []
        for course in course_list:
            if course.check_eligible(self.completed_courses+completed, semester, season):
                if self.check_credits(semester+[course]) <= credits: # If current course does not put us over the credit limit
                    semester.append(course)
        for course in semester:
            not_completed.remove(course)
        return semester, not_completed

    def get_tag_courses(self)  -> list:
        """Auto Select courses to satisfy tag"""
        temp = []
        count = 0
        for tag in self.tags:
            course = random.choice(tag)
            while course in temp:
                course = random.choice(tag)
                if count > len(self.tags) * 100:
                    print(f"Error occured getting course for {tag}")
                    break
            if course not in temp:
                temp.append(course)
        return temp

    def generate_course_list(self, seasons:list, credits=[-1]):
        """Generate a course schedule using the given ammount of credit hours. You can also do -1 credits for no limit"""
        for i in range(len(credits)):
            if credits[i] == -1: credits[i] = 1000
            #if credits[i] < self.db.credit_hours: return False, []
        not_completed = []
        schedule = []
        completed = []
        last_year_courses = []
        self.remaining_courses += self.get_tag_courses()
        for course_name in self.remaining_courses: # Loop through all the given courses and filter them
            if self.db.course_exist(course_name):
                course = self.db.get_course(course_name)
            elif self.db.tag_exist(course_name): # If it is a tag ignore it
                continue
            if course != None:
                if "LAST-YEAR" in course.get_prereq():
                    last_year_courses.append(course)
                else:
                    not_completed.append(course)
            else:
                print(f"Skipping {course_name} Since it doesn't exist")
        not_completed.sort(reverse=True)
        count = 0 # How many times the while loop has ran
        place = 0 # Which season to use
        season = seasons[0]
        seasons.append(seasons.pop(0))
        while len(not_completed) > 0:
            try:
                credits[place]
            except IndexError:
                place = 0
            semester, not_completed = self.generate_semester(not_completed, completed, season, credits[place])
            completed += semester
            schedule.append(semester)
            self.completed_courses += semester
            count += 1
            if count >= len(self.remaining_courses) * 10 and len(not_completed) > 0:
                # If the loop runs for 10 times the length of the course list assume the loop is stuck and end it
                print("Infinite Loop?")
                return False, []
            place += 1
            season = seasons[0]
            seasons.append(seasons.pop(0))
        for course in last_year_courses: # Add anything that must be taken in last semester
            schedule[-1].append(course)
        #for course in course_list: # Begin Inital adding to course_schedule
        return True, schedule

    def generate_schedule(self, data, template: dict):
        """Generates a schedule from a list or filename"""
        if type(data) == str: # If we are getting a filename parse it
            self.remaining_courses = Parser.parse_file(data)
            if self.remaining_courses == None:
                return {},[]
        else:
            self.remaining_courses = data
        self.completed_courses = []
        output_schedule = {}
        classlist = []
        #self.remaining_courses = list(dict.fromkeys(self.remaining_courses)) # Dedupe the list
        self.generate_completed()
        credits = list(template.values())
        seasons = list(template.keys())
        state, schedule = self.generate_course_list(seasons.copy(), credits=credits) # This does the actual schedule generation the rest is just formatting
        year = datetime.date.today().year # Get the starting year as a int

        while len(schedule) > 0:
            season = seasons.pop(0) # Take the season from the front of list
            key = season + " " + str(year)
            if key in output_schedule.keys(): # If the season and year have already been done goto he next year
                year += 1
                key = season + " " + str(year)
            seasons.append(season) # Add that season back to the back of list
            output_schedule[key] = []
            for course in schedule.pop(0): # Removes the first semester from the list and formats it
                output_schedule[key] += [str(course), course.credits]
                classlist += [course.format(), course.credits, ""]
        return output_schedule, classlist


def main():
    db = Database.Database("database.txt")

    #needed_courses = ['ENVS 1205', 'STAT 1401', 'CPSC 1302', 'CPSC 2105', 'CPSC 2108',
    #'CPSC 3125', 'CPSC 3131', 'CPSC 3165', 'CPSC 3175', 'CPSC 4000', 'MATH 5125',
    #'CPSC 3121', 'CPSC 4115', 'CPSC 4135', 'CPSC 4148', 'CPSC 4155', 'CPSC 4157', 'CPSC 4175', 'CPSC 4176']
    schedule_template = {
    "Fall": 15,
    "Spring": 15,
    "Summer": 6
    }
    st = Student(db)
    schedule, classlist = st.generate_schedule("Test Files/CompGamesProgramming.txt", schedule_template)
    print(schedule)
if __name__ == "__main__":
    main()
