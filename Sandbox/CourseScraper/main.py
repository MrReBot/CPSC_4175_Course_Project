import requests
import json
import string
import sys
url = "https://coursesearchapi.columbusstate.edu/v1/data/courses"
# From https://coursesearchapi.columbusstate.edu/v1/data/terms
seasons = {"Fall":"202208", "Spring":"202302", "Summer":"202305"}
sys.path.insert(1, '../..') # Makes it so we can access Database.py
import Database
db = Database.Database("../../database.txt")

def get_subject(term, subject):
    payload = {
        "term": term,
        "subjects": [subject],
        "courseNumber": None,
        "title": None,
        "instructors": None,
        "level": None,
        "coreAreas": None,
        "colleges": None,
        "departments": None,
        "partsOfTerm": None,
        "status": None,
        "meetingAfter": None,
        "meetingBefore": None,
        "online": None,
        "creditHours": None,
        "meetDays": None,
        "campuses": None,
        "materialCost": None
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)
    return json.loads(response.text)
    
def main():
    #fall = get_subject(seasons["Fall"], "CPSC")
    #print(db.all_sections())
    #with open("fall2022.txt","r") as f:
    #    fall = json.loads(f.read())
    #data = get_subject("202208","CPSC")
    #with open("tempdata.txt","w") as f:
    #    f.write(json.dumps(data))
    for subject in db.all_sections():
        season = get_subject(seasons["Summer"], subject)
        for course in season:
            if len(course["courses"]) == 0:
                print(f"Skipping {course}\n\n")
                continue
            temp = course["courses"][0]
            subject = temp["subject"]
            id = temp["courseNumber"].strip(string.ascii_letters)
            name = f"{subject} {id}"
            if db.course_exist(name):
                course = db.get_course(name)
                course.add_season("Su")
                print(f"Adding Spring season to {course}")
            #course = db.get_course(course)
            #course.add_season("Fa")
            #print(course.format(), course.seasons)
    db.save()
        
        
    #for section in fall:
    #    print(section[0]["courseNumber"])
    
main()
