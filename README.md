Class Schedule Planner Version 1.0.0

## Description:
This project is a college class scheduler that makes it possible for college students to be able
to plan out the classes that they need to take within an allotted time in college.

## Features:
When run, the user is tasked to input a classlist in the form of a pdf or txt, their identification, and the major of choice. After the program recieves these inputs it will either prompt the user to input their selection of electives or will automatically choose the most popular selectives (based on the programs settings).
The program will then create an organized excel sheet of all of the classes that they wish to take.
The program will be able to assign all classes a priority value based on what classes require it as a
prerequisite, and be able to assign electives a popularity value that will increase when a student of the track manually selects the elective.
The program is also capable of checking for prerequisite errors in existing xlsx schedules.

## Install Instructions:
1. Clone the project:
```bash
  https://github.com/MrReBot/CPSC_4175_Course_Project
```
2. Open the folder and Install the requirements:
```bash
  cd CPSC_4175_Course_Project
  pip install -r requirements.txt
```

## Usage:
You can use **SoftwareEngineering_PROJECT_Main.py** to start the program
