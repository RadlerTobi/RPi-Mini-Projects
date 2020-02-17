
import datetime as dt
import time
import random
#import RPi.GPIO as GPIO

alle_pflanzen = []

class Pflanze(object):
    def __init__(self, name, dauer, intervall):
        self.name = name
        self.dauer = dauer
        self.intervall = intervall
        self.letztes_giessen = dt.datetime.now()


    def giessen(self):
        print(self.name, " wird jetzt gegossen")
        print("Dauer: ",self.dauer)
        self.letztes_giessen = dt.datetime.now()
    def messen(self):
        self.feuchtigkeit = 17
        print("Aktuelle Feuchtigkeit: ",self.feuchtigkeit)
        # self.feuchtigkeit = Messwert

    def zeitkontrolle(self):
        diff = dt.datetime.now() - self.letztes_giessen

        if diff.seconds > self.intervall:
            return True
        else:
            return False


wilhelm = Pflanze("Wilhelm",10,4)
alle_pflanzen.append(wilhelm)

efeutute = Pflanze("Efeutute",2,17)
alle_pflanzen.append(efeutute)

klaus = Pflanze("Klaus",30,1)
alle_pflanzen.append(klaus)

while(True):
    if dt.datetime.now().hour == 13:
        for p in alle_pflanzen:
            print(p.name, " wird kontrolliert")
            if p.zeitkontrolle():
                p.giessen()
    time.sleep(2)
    
