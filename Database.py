import json
import os
import traceback

class Course:
    name = ""
    prereq = []
    section = ""
    id = ""
    credits = -1
    value = -1
    seasons = [] # Seasons that class is avaliabe in can be Fa, Sp, or Su
    valid_seasons = {"Fall":"Fa","Spring":"Sp","Summer":"Su"}
    db = {}
    def __init__(self,  template = None, db=None):
        self.seasons = []
        if template != None:
            self.__dict__.update(template)
        if db != None:
            self.db = db

    def reset_value(self):
        self.value = -1
    
    def add_season(self, season):
        if season in ["Fa", "Sp", "Su"] and season not in self.get_seasons():
            self.seasons.append(season)
            self.reset_value()

    def get_seasons(self):
        return self.seasons
        
    def toJSON(self):
        """Create a dictionary representation of the course. Mainly for exporting to disk"""
        template = {
            "name":self.name,
            "prereq":self.prereq,
            "credits":int(self.credits),
            "value": self.get_value(),
            "seasons":self.get_seasons()
            }
        return template

    def format(self):
        """Fancy formatted version of course e.g 'CPSC 1301 - Computer Science I'"""
        return f"{self.section} {self.id} - {self.name}"

    def __str__(self):
        """Printed version of a course e.g 'CPSC 1301'"""
        return f"{self.section} {self.id}"

    def __lt__(self, other):
        """This allows a list of course objects to be sorted and represents the less than operator"""
        return self.get_value() < other.get_value()

    def get_prereq(self):
        """Get the list of Prerequisites"""
        return self.prereq

    def check_eligible(self, course_list, semester=[], season=None):
        """Check if a given course_list makes you eligible"""
        temp_course = course_list.copy()
        if season != None and self.seasons != []: # If a season was provided check if the course is in season
            if season not in self.valid_seasons.values():
                season = self.valid_seasons[season]
            if season not in self.seasons:
                return False
        for i in range(len(temp_course)): # Convert course objects into their course name
            if type(temp_course[i]) == Course:
                temp_course[i] = str(temp_course[i])
        for prereq in self.get_prereq():
            if str(self) in self.db.get_course(prereq).get_prereq():
                 #print(f"Taking {self} concurrently with {prereq}")
                 return True
            if self.db.course_exist(prereq):
                if prereq not in temp_course:
                    return False
            else:
                print(f"'{prereq}' cannot be found in the database. Assuming it has already been taken")
                return True
        return True

    def get_value(self, last_course=None, req_list=[]):
        """Get a single courses's value in relation to the other courses"""
        i = 0
        if self.value == -1:
            if last_course == None:
                last_course = [self]
            if self.seasons != []:
                i += (3 - len(self.seasons)) * 2
            #print(str(self), last_course)
            for c in self.db.all_courses(sort=False):
                if type(c) == list: # This skips over any tags that may be in the database
                    continue
                if str(self) in c.get_prereq() and str(c) not in last_course:
                    i+= 1
                    last_course.append(str(c))
                    i += c.get_value(last_course[-2:], req_list)
                    if c in req_list:
                        i += 1
            self.value = i
        else:
            return self.value
        return i




class Database:
    data = {}
    tags = {}
    #default_course = {"req":[],"name":""} # Default template for all courses
    pretty_print = True
    credit_hours = -1

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
                        self.data[section][course] = Course(template=temp_data[section][course],db=self)
                        self.data[section][course].section = section
                        self.data[section][course].id = course
                        if int(self.data[section][course].credits) > self.credit_hours:
                            self.credit_hours = int(self.data[section][course].credits)
        else:
            self.data = {}
        
    def reset_values(self):
        """Clear all stored values so they can be recalculated. Mainly used when the value system is modified"""
        for course in self.all_courses():
            course.reset_value()
        
        
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
        try:
            if self.pretty_print:
                data = json.dumps(self.data, indent=4, default=lambda x: x.toJSON())
            else:
                data = json.dumps(self.data, default=lambda x: x.toJSON())
        except AttributeError:
            print("An error occured while saving")
            traceback.print_exc()
        else:
            with open(self.filename,"w") as f:
                f.write(data)
        self.data.pop("TAGS",None)
        
    # This is just for testing def remove this later
    def reset(self):
        self.data = {}

    def all_sections(self):
        """Get a list of every available course section"""
        return list(self.data.keys())

    def all_courses(self, sort=False, reverse=False):
        """Return a list of all courses. Optionally sorted by course value"""
        temp = []
        for section in self.all_sections():
            temp += list(self.data[section].values())
        if sort:
            temp.sort(reverse=reverse)
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
        self.data[section][id] = Course(template=template, db=self)
        for course in self.all_courses():
            course.value = -1

    def add_prereq(self, course, prereq):
        """" Add a list of prerequisites to a course"""
        for req in prereq:
            if req == course: # Don't add a course to itself
                print(f"ERROR: Not adding {req} to itself")
                continue
            #if self.course_exist(req) and req not in self.get_prereq(course):
            if req not in self.get_prereq(course):
                course = self.get_course(course)
                course.prereq.append(req)

    def course_exist(self, course):
        """Check if a course exists in the database"""
        try:
            section, c_number = course.split(" ")
            self.data[section][c_number] # This will throw a key error if the course doesn't exist
            return True
        except KeyError:
            #print(f"ERROR: {course} doesn't exist")
            return False
        except ValueError:
            #print(f"ERROR: '{course}' isn't a valid course name")
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
            if self.course_exist(query):
                found.append(self.get_course(query))
            if query.lower() in course.name.lower():
                if course.credits >= min_credits:
                    found.append(course.format())
        if sort:
            found.sort()
        return list(dict.fromkeys(found))[:max_size]

def main():
    db = Database("database.txt")

if __name__ == "__main__":
    main()
