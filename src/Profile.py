from doctest import ELLIPSIS_MARKER
from operator import contains
from datetime import datetime

class Profile:
    def __init__(self,profile):
        self.name = profile["generalInfo"]["name"]
        self.title = profile["generalInfo"]["title"]
        #self.location = profile["generalInfo"]["location"] --- To implement in extension
        self.photoURL = profile["generalInfo"]["photouRL"]
        self.contactCard = self.initContactCard(profile["profilecard"])
        self.experiences = self.initExperience(profile["experiences"])
        self.education = self.initEducation(profile["education"])
        self.currentWork = self.initCurrentWork(profile["experiences"])
        self.lastUpdated = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def initContactCard(self,profileCard):
        contactCard = {
            "profileUrl": profileCard.get("profileUrl", ""),
            "email": profileCard.get("email", ""),
            "website": profileCard.get("website", ""),
            "twitter": profileCard.get("twitter", ""),
        }
        return contactCard


    def initExperience(self,expArr):
        
        if(len(expArr) == 0):
            return []
        
        else:
            experiences = []
            for exp in expArr:
                experience = {
                    "company": exp.get("company", ""),
                    "position": exp.get("position", ""),
                    "location": exp.get("location", ""),
                    "periodo": exp.get("dateRange", ""),  # TODO: format to date
                }
                experiences.append(experience)
                #experience.clear()
            return experiences
            
    def initEducation(self,educArr):
        if(len(educArr) == 0):
            return []
        
        else:
            educs = []
            for educ in educArr:
                experience = {
                    "institution": educ.get("institution", ""),
                    "degree": educ.get("degree", ""),
                    "periodo": educ.get("dateRange", ""),  # TODO: format to date 
                }
                educs.append(experience)
                #experience.clear()
            return educs

    def cleanDates(self,dateRange):
        if(dateRange == ""):
            return ""
    
    def initCurrentWork(self,expArr):
        lastJob = expArr[0]
        if 'actualidad' in lastJob.get("dateRange", "").lower():
            return {
                    "status": "Empleado",
                    "company": lastJob.get("company", ""),
                    "position": lastJob.get("position", ""),
                    "location": lastJob.get("location", ""),
                    "startDate": lastJob.get("dateRange", ""),  # TODO: format to date
                }
        else:
            return {
                    "status": "Desempleado",
                }

    def getDataProfiles(self):
        return {'name':self.name, 'title':self.title, 'photoURL':self.photoURL, 'contactCard':self.contactCard, 'experiences':self.experiences, 'education':self.education, 'currentWork':self.currentWork, 'lastUpdated':self.lastUpdated}