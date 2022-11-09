

from collections import Counter

# Allows for Random Selection
import random

# Variables for AI Module
global ManualSelection = False
ComputerScience_games_Selected = True
ComputerScience_cyber_Selected = False

defaultGeneralElectiveList = ["Elective1", "Elective2", "Elective3"]


# Method for determining most frequently selected electives
# --- If there is more than one elective of the same popularity,
# --- the program will randomly choose from the that popular list
# --- If there is NO Most Popular Elective, it will choose a random elective
def popularElectives(myList):
    counts = Counter(myList)
    max_count = counts.most_common(1)[0][1]
    mostPopularList = [value for value, count in counts.most_common() if count == max_count]
    if len(mostPopularList) > 1:
        randomElectiveIndex = random.randrange(len(mostPopularList))
        return mostPopularList[randomElectiveIndex]
    else:
        return mostPopularList


# Checks which Pathway was Selected (or not Selected)
# --- Also, this computes which elective is the most popular to recommend
if ManualSelection == False:
    if ComputerScience_games_Selected == True:
        testList1 = ["Art Appreciation", "Introduction to Philosophy", "Descriptive Astronomy"]
        print(popularElectives(testList1))
    elif ComputerScience_cyber_Selected == True:
        testList2 = ["Survey of Chemistry", "World Literature", "Principles of MicroEconomics", "Survey of Chemistry"]
        print(popularElectives(testList2))

else:
    print("ManualSelection is TRUE")
