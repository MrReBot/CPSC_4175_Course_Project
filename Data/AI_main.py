

from collections import Counter

# Allows for Random Selection
import Database
import Parser
import random
from os.path import exists

# Variables for AI Module
ManualSelection = False
ComputerScience_games_Selected = True
ComputerScience_cyber_Selected = False
db = Database.Database("database.txt")
defaultGeneralElectiveList = ["Elective1", "Elective2", "Elective3"]


#-------------------------New Code------------------------
#This method reads the dynamic database text file and turns it into a dictionary
def readDynamicDatabase():
    fileDictionary = {}
    courselist= Parser.parse_txt("Data/DynamicElectives_Database.txt",db)
    for line in courselist:
        if "{" in line:
            currentName = line.split("{")[0]
            fileDictionary[currentName]= list()
        elif "}" not in line:
            course = line.split(", ")
            fileDictionary[currentName].append(course[0])
            fileDictionary[currentName].append(course[1])
    return fileDictionary

#Create a default electives database for computer science electives
def createCompElectivesText():
    if(exists("Data/DefaultElectives_Database.txt") == False):
        file =open("Data/DefaultElectives_Database.txt", "a")
        for course in db.get_tag("CPSC-ELECT"):
            file.write(course +"\~n")

#Method to choose courses from the dynamic database
def chooseFromDynamicDatabase(courseList, numberOfElectives):
    currentChosenCourse = ""
    currentHighestPriority = 0
    electiveList = []
    electiveNumber = 0
    electiveIndex = 0
    #While electives still need to be chosen if the courselist is not empty
    while electiveNumber < numberOfElectives:
        if courseList:
            #If the current courses priority/popularity is greater than the currentHighest
            for currentPriority in courseList:
                if(currentPriority.isdigit()):
                    if int(currentPriority) > currentHighestPriority:
                        #Change the currentHighest to the current and choose the course with that popularity
                        currentHighestPriority = int(currentPriority)
                        currentChosenCourse = courseList[courseList.index(currentPriority)-1]
                        electiveIndex = courseList.index(currentPriority)
            #Add the chosen course to the elective list and remove it from the selection process
            currentHighestPriority = 0
            electiveList.append(currentChosenCourse)
            courseList.pop(electiveIndex)
            courseList.pop(electiveIndex-1)
            electiveNumber = electiveNumber + 1
        #If the courselist is empty, choose the remaining courses randomly from the default database
        else:
            defaultList = self.chooseFromDefaultDatabase(numberOfElectives-electiveNumber)
            for course in defaultList:
                #if the chosen course is not already in the list, add it to the list
                if course not in electiveList:
                    electiveList.append(course)
                    electiveNumber = electiveNumber + 1
    return electiveList

#Method to choose from the default database text file
def chooseFromDefaultDatabase(numberOfElectives):
    chosenCourse = ""
    electiveList = []
    #Save the text file as a list of courses
    courseList= Parser.parse_txt("Data/DefaultElectives_Database.txt",db)
    #Loop until it selects the number of random electives desired
    for i in range(numberOfElectives):
        chosenCourse = courseList.pop(random.randint(0,len(courseList)-1))
        electiveList.append(chosenCourse)
    return electiveList

#Method to choose the electives from the dynamic database
def chooseElectives(majorName, number_of_electives):
    fileDictionary = {}
    electiveList = []
    fileDictionary =readDynamicDatabase()
    #If there is data for the major in the database, choose the electives using the dynamic method
    if majorName in fileDictionary:
        electiveList = chooseFromDynamicDatabase(fileDictionary[majorName],number_of_electives)
    #else choose all randomly from the default
    else:
        electiveList = chooseFromDefaultDatabase(number_of_electives)
    return electiveList;

#Method updates the dynamic database
#Give it a majorName and className, and it will store those values in the dynamic database
def saveToDynamicDatabase(majorName, className):
    fileDictionary = {}
    fileDictionary =readDynamicDatabase()
    #If the major name already exists in the database
    if majorName in fileDictionary:
        #And the class already exists under the major
        if className in fileDictionary[majorName]:
            #Increase the level of popularity/priority of the class
            priorityIndex = fileDictionary[majorName].index(className) +1
            fileDictionary[majorName][priorityIndex] = str(int(fileDictionary[majorName][priorityIndex]) +1)
        #Else add the class to the major with a base priority of 1
        else:
            fileDictionary[majorName].append(className)
            fileDictionary[majorName].append('1')
    #Else add the major to the database and add the class to the major with a base priority of 1
    else:
        fileDictionary[majorName]=list()
        fileDictionary[majorName].append(className)
        fileDictionary[majorName].append('1')
    #Rewrite the data to the dynamic database and close
    file = open("Data/DynamicElectives_Database.txt",'w')
    for major in fileDictionary:
        file.write(major+"{\n")
        for course in fileDictionary[major]:
            if(course.isdigit()):
                file.write(course+ "\n")
            else:
                file.write(course+ ", ")
        file.write("}\n")
    file.close();
    return fileDictionary;

#Method that completely wipes the dynamic database of all priorities
#Using essentially sets all priority levels back to zero
def deleteDynamicData():
    open('Data/DynamicElectives_Database.txt', 'w').close()


#---------------------------------------------------------
