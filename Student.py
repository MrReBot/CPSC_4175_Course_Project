import Database

class Student:
    name = ""
    remaining_courses = []
    completed_courses = []
    db = None
    def __init__(self, db, remaining_courses):
        if remaining_courses != None:
            self.remaining_courses = remaining_courses
        self.db = db
        self.generate_completed()

    def generate_completed(self):
        self.completed_courses = self.db.all_courses()
        for course in self.remaining_courses:
            if self.db.course_exist(course):
                self.completed_courses.remove(self.db.get_course(course))
            else:
                print(f"{course} doesn't exist")

    def check_credits(self, courses):
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

    def generate_semester(self, course_list, completed, credits=15):
        temp_completed = []
        not_completed = course_list.copy() # Make a copy of the course list
        semester = []
        for course in course_list:
            if course.check_eligible(self.completed_courses+completed):
                if self.check_credits(semester+[course]) <= credits: # If current course does not put us over the credit limit
                    semester.append(course)
        for course in semester:
            not_completed.remove(course)
        return semester, not_completed

    def generate_course_list(self, credits=-1):
        """Generate a course schedule using the given ammount of credit hours. You can also do -1 credits for no limit"""
        if credits == -1: credits = 1000
        if credits < self.db.credit_hours: return False, []
        not_completed = []
        schedule = []
        completed = []
        last_year_courses = []
        for course in self.remaining_courses:
            course = self.db.get_course(course)
            if "LAST-YEAR" in course.get_prereq():
                last_year_courses.append(course)
            else:
                not_completed.append(course)
        not_completed.sort(reverse=True)
        count = 0 # How many times the while loop has ran
        while len(not_completed) > 0:
            semester, not_completed = self.generate_semester(not_completed, completed, credits)
            completed += semester
            schedule.append(semester)
            self.completed_courses += semester
            count += 1
            if count >= len(self.remaining_courses) * 10 and len(not_completed) > 0:
                # If the loop runs for 10 times the length of the course list assume the loop and stuck and end it
                return False, []

        for course in last_year_courses: # Add anything that must be taken in last semester
            schedule[-1].append(course)
        #for course in course_list: # Begin Inital adding to course_schedule
        return True, schedule



def main():
    db = Database.Database("database.txt")

    needed_courses = ['ENVS 1205', 'STAT 1401', 'CPSC 1302', 'CPSC 2105', 'CPSC 2108',
    'CPSC 3125', 'CPSC 3131', 'CPSC 3165', 'CPSC 3175', 'CPSC 4000', 'MATH 5125',
    'CPSC 3121', 'CPSC 4115', 'CPSC 4135', 'CPSC 4148', 'CPSC 4155', 'CPSC 4157', 'CPSC 4175', 'CPSC 4176']

    st = Student(db, needed_courses)
    state, schedule = st.generate_course_list(credits=15)
    i = 0
    for semester in schedule:
        print(f"\nSemester {i}")
        for course in semester:
            print(course.format(), course.get_value())
        i += 1

if __name__ == "__main__":
    main()
