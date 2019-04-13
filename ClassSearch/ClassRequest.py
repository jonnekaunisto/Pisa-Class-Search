import os
import requests

class UCSCClass:

    def __init__(self, career, grading, classNum, type, credits, genEd, status, availableSeats, enrollCap, enrolled, waitlistCap, waitlistTotal):
        self.career = career
        self.grading = grading
        self.classNum = classNum
        self.type = type

class Section:
req = requests.Request("POST", "https://pisa.ucsc.edu/class_search/index.php")