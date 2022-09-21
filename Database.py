import json
import os

class Course:
    name = ""
    prereq = []
    section = ""
    id = ""
    credits = -1
    def __init__(self,  template = None):
        if template != None:
            self.__dict__.update(template)

    """Create a dictionary representation of the course"""
    def toJSON(self):
        ignore = ["section","id"] # Attributes to not be included in dump
        temp = {k:v for k,v in self.__dict__.items() if k  not in ignore}
        return temp
    def __str__(self): # String version of object
        return f"{self.section} {self.id}: {self.name} ({self.credits})" # e.g

    def __lt__(self, other): # Makes the object sortable
        return self.credits < other.credits

    """Get the list of Prerequisites"""
    def get_prereq(self):
        return self.prereq
        
    """Check if a given course_list makes you eligible"""
    def check_eligible(self, course_list=[]):
        for prereq in self.get_prereq():
            if prereq not in course_list:
                return False
        return True




class Database:
    data = {}
    #default_course = {"req":[],"name":""} # Default template for all courses
    pretty_print = True

    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) != 0: #If it exists and is not empty
            with open(self.filename,"r") as f:
                temp_data = json.loads(f.read())
                for section in temp_data:
                    for course in temp_data[section]:
                        self.add_section(section)
                        self.data[section][course] = Course(template=temp_data[section][course])
                        self.data[section][course].section = section
                        self.data[section][course].id = course
        else:
            self.data = {}
            
    """Save Any Changes to disk"""
    def save(self):
        with open(self.filename,"w") as f:
            if self.pretty_print:
                f.write(json.dumps(self.data, indent=4, default=lambda x: x.toJSON()))
            else:
                f.write(json.dumps(self.data, default=lambda x: x.toJSON()))

    # This is just for testing def remove this later
    def reset(self):
        self.data = {}

    """Get a list of every available course section"""
    def all_sections(self):
        return list(self.data.keys())

    """Return a list of all courses. Optionally sorted by credit hours"""
    def all_courses(self, sort=False):
        temp = []
        for section in self.all_sections():
            temp += list(self.data[section].values())
        if sort:
            temp.sort()
        return temp

    def add_section(self, section):
        if section not in self.all_sections():
            self.data[section] = {}

    def add_course(self, course, name=None, prereq=[], credits=0):
        section, id = course.split(" ")
        template = {}
        if self.course_exist(course):
            print(f"ERROR: '{course}' already exists")
            return
        if section not in self.all_sections(): # If the section already exists
            self.add_section(section)

        template = {
        "name":name,
        "prereq":prereq,
        "credits":credits,
        "section":section,
        "id":id
        }
        self.data[section][id] = Course(template=template)

    """" Add a list of prerequisites to a course"""
    def add_prereq(self, course, prereq):
        for req in prereq:
            if req == course: # Don't add a course to itself
                print(f"ERROR: Not adding {req} to itself")
                continue
            #if self.course_exist(req) and req not in self.get_prereq(course):
            if req not in self.get_prereq(course):
                section, c_number = course.split(" ")
                self.data[section][c_number]["req"].append(req)

    """Check if a course exists in the database"""
    def course_exist(self, course):
        try:
            section, c_number = course.split(" ")
            self.data[section][c_number] # This will throw a key error if the course doesn't exist
            return True
        except KeyError:
            #print(f"ERROR: {course} doesn't exist")
            return False
            
    """Check if a section is a valid name"""
    def section_exist(self, section):
        return section.upper() in self.all_sections()

    """If a course exists return it's data"""
    def get_course(self, course):
        if self.course_exist(course):
            section, c_number = course.split(" ")
            return self.data[section][c_number]

    """Get a specific section from the database e.g 'CPSC' for all the computer science classes"""
    def get_section(self, section):
        if section in self.data.keys():
            return self.data[section]
        else:
            return {}

    """Search for a course in the database"""
    def search(self, query, min_credits=0 ,max_size=20, sort=False):
        found = []
        if query in [""," "]: # If the query is "" or " "
            return []
        for section in self.all_sections(): #Search for Specific section
            if query in section:
                found.append(f"Section: {section}")
        for course in self.all_courses(): # Search through all the courses
            if query.lower() in course.name.lower():
                if int(course.credits) >= min_credits:
                    found.append(course)
        if sort:
            found.sort()
        return list(dict.fromkeys(found))[:max_size]

def main():
    db = Database("database.txt")
    #db.save()
    #print(type(db.search("Computer")[0]))
    while True:
        query = input("What do you want to search for? (or enter quit to quit): ")
        if query == "quit":
            break
        results = db.search(query, sort=True)

        print(f"Found {len(results)} result(s)")
        print("\n".join([str(i) for i in results]),"\n")
    #print(db.check_eligible("CPSC 1302", [])) # I Can't take CPSC 1302
    #print(db.check_eligible("CPSC 1302", ["CPSC 1301"])) # I Can
    #db.add_course("CPSC 1301","Computer Science 1", credits=4)
    #db.add_course("CPSC 1302","Computer Science 2", ["CPSC 1301"], credits=3)
    #db.add_course("CPSC 1303","Computer Science 3", ["CPSC 1302"], credits=3)
    #print(type(db.get_course("CPSC 1301")))
    #db.save()

if __name__ == "__main__":
    main()
