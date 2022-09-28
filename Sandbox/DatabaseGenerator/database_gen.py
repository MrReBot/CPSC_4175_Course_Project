import re
import json
import sys
sys.path.insert(1, '../..') # Makes it so we can access Database.py
import Database

def get_course(unfiltered_course):
    course = re.findall("[a-zA-Z]+ [0-9]{4}",unfiltered_course)
    try:
        return course[0].strip()
    except IndexError:
        print([unfiltered_course])
        if "TOEFL" in unfiltered_course:
            return "TOEFL"
        else:
            return "REMOVE-ME"

def get_course_name(unfiltered_course):
    course = get_course(unfiltered_course)
    start = unfiltered_course.index(course)+len(course)
    
    end = len(unfiltered_course)
    if unfiltered_course[start+1] == " ":
            start += 2
    if " (" in unfiltered_course:
        end = unfiltered_course.index(" (")
    return unfiltered_course[start:end].strip()

def process_prereq(data, course):
    #data = data.split(" or ")
    output = []
    #Grab a single course from a string
    if ") and (" in data: #Can't do these automatically
        #print(f"'{course}' requires manual updating")
        if course == "CPSC 4127":
            print("Loading CPSC 4127 template")
            return ["CYBR 2160","CYBR 2159"]
        return ["REPLACE-ME"]
    if ") or (" in data:
        data = data.split(") or (")[0]
    if " or " not in data:
        if " and " in data:
            split_data = data.split("and")
            output.append(get_course(split_data[0]))
            output.append(get_course(split_data[1]))
        else:
            output.append(get_course(data))
    else: # If or is in data
        split_data = data.split("or")
        output.append(get_course(split_data[0]))
        output.append(get_course(split_data[1]))
    
    for item in output.copy():
        if item.startswith("CSCI") or item == "REMOVE-ME":
            output.remove(item)
    return list(dict.fromkeys(output)) # Dedupe output

def get_input():
    text = input()
    output = []
    while text != "q":
        output.append(text)
        text = input()
    return output

def get_credits(data):
    data = data.strip()
    return re.findall("[0-9]\)",data)[0][0]

def main():
    db = Database.Database("../../database.txt")
    #with open("data.txt","r",encoding="utf8") as f:
    #    text = f.read().splitlines()
    
    text = get_input()
    template = get_course(text[0]).split(" ")[0]
    if input(f"Template is {template} type 'y' to continue: ") != "y":
        quit()
    for i,line in enumerate(text):
        if line.startswith(template):
            course = get_course(line)
            course_name = get_course_name(line)
            credits = get_credits(line)
            prereq = []
            for sub_line in text[i+1:i+6]:
                if sub_line.startswith(template):
                    break
                if sub_line.startswith("Prerequisite(s): "):
                    prereq = process_prereq(sub_line, course)
            db.add_course(course, course_name, prereq, credits)
    db.save()
    
while True:
    main()
    if input("Enter y to add another course: ") != "y":
        break
#db = Database.Database("data")
#db.add_course("CPSC 1301")
#db.save()
#print(process_prereq(var))
#print(process_prereq(var4))