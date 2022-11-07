import requests
import json
import string
import sys
url = "https://coursesearchapi.columbusstate.edu/v1/data/courses"
# From https://coursesearchapi.columbusstate.edu/v1/data/terms
seasons = {"Fall":"202208", "Spring":"202302", "Summer":"202305"}
season_names = {"Fall":"Fa","Spring":"Sp","Summer":"Su"}
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
    input("This will scrape the Course Search API and update the database accordingly.\nPress Enter to Continue:")
    count = 0
    for season, season_id in seasons.items():
        for subject in db.all_sections():
            try:
                classes = get_subject(season_id, subject)
            except json.decoder.JSONDecodeError:
                print(f"Can't Process {subject}")
                continue
            for course in classes:
                if len(course["courses"]) == 0:
                    print(f"Skipping {course}\n\n")
                    continue
                temp = course["courses"][0]
                subject = temp["subject"]
                id = temp["courseNumber"].strip(string.ascii_letters)
                name = f"{subject} {id}"
                if db.course_exist(name):
                    course = db.get_course(name)
                    if season_names[season] not in course.get_seasons():
                        course.add_season(season_names[season])
                        print(f"Adding {season} season to {course}")
                        count += 1
                #course = db.get_course(course)
                #course.add_season("Fa")
                #print(course.format(), course.seasons)
    print(f"Updated {count} entires")
    db.save()
        
        
    #for section in fall:
    #    print(section[0]["courseNumber"])
    
main()
