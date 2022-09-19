import json
import os
class Database:
    data = {}
    folder_mode = False # If we are storing a single directory or splitting it up by section
    #default_course = {"req":[],"name":""} # Default template for all courses
    pretty_print = False
    
    def __init__(self, filename):
        self.filename = filename
        if os.path.isdir(filename) or "." not in filename:
            self.folder_mode=True
        self._load()
            
    def _load(self):
        if self.folder_mode: # If we are loading from a folder
            for file in os.listdir(self.filename):
                path = os.path.join(self.filename,file)
                if os.path.getsize(path) != 0: # If the file is not empty
                    with open(path,"r") as f:
                        self.data.update(json.loads(f.read()))
        else:
            if os.path.exists(self.filename):
                if os.path.getsize(self.filename) != 0: # If the file is not empty
                    with open(self.filename,"r") as f:
                        self.data = json.loads(f.read())
            else:
                self.data = {}
    def save(self):
        if self.folder_mode:
            if not os.path.isdir(self.filename):
                os.mkdir(self.filename)
            for sec in self.data:
                temp = {sec: self.data[sec]}
                path = os.path.join(self.filename,sec+".txt")
                with open(path,"w") as f:
                    if self.pretty_print:
                        f.write(json.dumps(temp, indent=4))
                    else:
                        f.write(json.dumps(temp))
        else:
            with open(self.filename,"w") as f:
                if self.pretty_print:
                    f.write(json.dumps(self.data, indent=4))
                else:
                    f.write(json.dumps(self.data))
            
    # This is just for testing def remove this later
    def reset(self):
        self.data = {}
    
    """Get a list of every available course section"""
    def all_sections(self):
        return list(self.data.keys())
        
    def add_section(self, section):
        if section not in self.all_sections():
            self.data[section] = {}
        
    def get_default_course(self):
        return {"req":[],"name":""}
    
    def add_course(self, course, name=None, prereq=None):
        section, c_number = course.split(" ")
        if self.course_exist(course):
            print(f"ERROR: '{course}' already exists")
            return
        if section in self.all_sections(): # If the section already exists
            self.data[section][c_number] = self.get_default_course()
        else: # If the section doesn't exist
            self.add_section(section)
            self.data[section][c_number] = self.get_default_course()
        # Add the prerequisites
        if prereq is not None: # If a list of prereqs were provided
            self.add_prereq(course, prereq)
        if name is not None: # If a name was provided
            self.data[section][c_number]["name"] = name
            
    # Add a list of prereqs to a course
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
    
    def get_prereq(self, course):
        return self.get_course(course)["req"]
            
    # Check if a course list makes you eligable for a course
    def check_eligible(self, course, course_list):
        for prereq in self.get_prereq(course):
            if prereq not in course_list:
                return False
        return True
    
    """Get a specific section from the database e.g 'CPSC' for all the computer science classes"""
    def get_sections(self, section):
        if section in self.data.keys():
            return self.data[section]
        else:
            return {}
        
    """Search for a course in the database"""
    def search(self, query, max_size=20):
        found = []
        if query in [""," "]: # If the query is "" or " "
            return []
        for section in self.data:
            if query in section:
                found.append(f"Section: {section}")
            for course in self.data[section]:
                if query in course.lower():
                    found.append(course)
                if query.lower() in self.data[section][course]["name"].lower():
                    temp = self.data[section][course]["name"]
                    found.append(f"{section} {course}: {temp}")
        return list(dict.fromkeys(found))[:max_size]
            
def main():
    db = Database("database.txt")
    #db.save()
    while True:
        query = input("What do you want to search for? (or enter quit to quit): ")
        if query == "quit":
            break
        results = db.search(query)
        print(f"Found {len(results)} result(s)")
        print("\n".join(results),"\n")
    #print(db.check_eligible("CPSC 1302", [])) # I Can't take CPSC 1302
    #print(db.check_eligible("CPSC 1302", ["CPSC 1301"])) # I Can
    #db.add_course("CPSC 1302","Computer Science 1", ["CPSC 1302"])

if __name__ == "__main__":
    main()