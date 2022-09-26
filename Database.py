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

    def toJSON(self):
        """Create a dictionary representation of the course. Mainly for exporting to disk"""
        ignore = ["section","id"] # Attributes to not be included in dump
        temp = {k:v for k,v in self.__dict__.items() if k  not in ignore}
        return temp
    
    def format(self):
        return f"{self.section} {self.id}: {self.name} ({self.credits})"
        
    def __str__(self): # String version of object
        return f"{self.section} {self.id}" # e.g

    def __lt__(self, other): # Makes the object sortable
        return self.credits < other.credits

    def get_prereq(self):
        """Get the list of Prerequisites"""
        return self.prereq
        
    def check_eligible(self, course_list=[]):
        """Check if a given course_list makes you eligible"""
        for prereq in self.get_prereq():
            if prereq not in course_list:
                return False
        return True




class Database:
    data = {}
    tags = {}
    #default_course = {"req":[],"name":""} # Default template for all courses
    pretty_print = True

    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) != 0: #If it exists and is not empty
            with open(self.filename,"r") as f:
                temp_data = json.loads(f.read())
                if "TAGS" in temp_data.keys():
                    self.tags = temp_data["TAGS"]
                    del temp_data["TAGS"]
                for section in temp_data:
                    for course in temp_data[section]:
                        self.add_section(section)
                        self.data[section][course] = Course(template=temp_data[section][course])
                        self.data[section][course].section = section
                        self.data[section][course].id = course
        else:
            self.data = {}
            
    def all_tags(self):
        """Get every tag"""
        return self.tags
        
    def tag_exist(self, tag):
        """Check if a given tag exists"""
        return tag in self.all_tags().keys()
        
    def get_tag(self, tag):
        """If a tag exists return it"""
        if self.tag_exist(tag):
            return self.tags[tag]
        
        
    def add_tag(self, tag, classes=None):
        """Add a new tag or update an already existing tag"""
        if not self.tag_exist(tag):
            self.tags[tag] = []
        if classes != None:
            self.tags[tag] = classes
        
    def save(self):
        """Save Any Changes to disk"""
        self.data["TAGS"] = self.tags
        with open(self.filename,"w") as f:
            if self.pretty_print:
                f.write(json.dumps(self.data, indent=4, default=lambda x: x.toJSON()))
            else:
                f.write(json.dumps(self.data, default=lambda x: x.toJSON()))
        del self.data["TAGS"]
    # This is just for testing def remove this later
    def reset(self):
        self.data = {}

    def all_sections(self):
        """Get a list of every available course section"""
        return list(self.data.keys())

    def all_courses(self, sort=False):
        """Return a list of all courses. Optionally sorted by credit hours"""
        temp = []
        for section in self.all_sections():
            temp += list(self.data[section].values())
        if sort:
            temp.sort()
        return temp

    def add_section(self, section):
        """If a section does not exist add it"""
        if section not in self.all_sections():
            self.data[section] = {}

    def add_course(self, course, name=None, prereq=[], credits=0):
        """Add a course to the course list"""
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

    def add_prereq(self, course, prereq):
        """" Add a list of prerequisites to a course"""
        for req in prereq:
            if req == course: # Don't add a course to itself
                print(f"ERROR: Not adding {req} to itself")
                continue
            #if self.course_exist(req) and req not in self.get_prereq(course):
            if req not in self.get_prereq(course):
                section, c_number = course.split(" ")
                self.data[section][c_number]["req"].append(req)

    def course_exist(self, course):
        """Check if a course exists in the database"""
        try:
            section, c_number = course.split(" ")
            self.data[section][c_number] # This will throw a key error if the course doesn't exist
            return True
        except KeyError:
            #print(f"ERROR: {course} doesn't exist")
            return False
            
    def section_exist(self, section):
        """Check if a section is a valid name"""
        return section.upper() in self.all_sections()

    def get_course(self, course):
        """If a course exists return it's data"""
        if self.course_exist(course):
            section, c_number = course.split(" ")
            return self.data[section][c_number]

    def get_section(self, section):
        """Get a specific section from the database e.g 'CPSC' for all the computer science classes"""
        if section in self.data.keys():
            return self.data[section]
        else:
            return {}

    def search(self, query, min_credits=0 ,max_size=20, sort=False):
        """Search for a course or section in the database"""
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
