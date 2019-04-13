import os
import requests
import re

class UCSCClass:
    def __init__(self,html):    
        splitr = '<div class="col-xs-12 col-sm-6 col-md-6" >(.*?)</div>'
        isor = '<dd>(.*?)</dd>'

        html = html.replace('\n','')
        tbls = re.findall(splitr,html)#Split table to left and right side
        leftmatches = re.findall(isor,tbls[0])
        rightmatches = re.findall(isor,tbls[1])    

        self.career = leftmatches[0]
        self.grading = leftmatches[1]
        self.classNum = leftmatches[2]
        self.type = leftmatches[3]
        self.credits = leftmatches[4]
        self.genEd = leftmatches[5] if leftmatches[5] != '&nbsp;' else None
        self.status = "Open" if "Open" in rightmatches[0][:-7] else "Closed" if "Closed" in rightmatches[0][:-7] else "Waitlist"
        self.availibleSeats = rightmatches[1][:-7]
        self.enrollCap = rightmatches[2][:-7]
        self.enrolled = rightmatches[3][:-7]
        self.waitlistCap = rightmatches[4][:-7]
        self.waitlistTotal = rightmatches[5][:-7]
        print(self.career, self.grading,self.waitlistCap)
class Section:
    req = requests.Request("POST", "https://pisa.ucsc.edu/class_search/index.php")

if __name__ == "__main__":
    print("Run some other way")