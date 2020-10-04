from bs4 import BeautifulSoup
import csv
from csv import writer
import struct

def findBreak(s):
    if(s is not None and '<br>' in s):
        return True
    else: 
        return False
def trimText(s):
    ##filter html  <br> tag
    if(s is None):
        return
    if(findBreak(s)):
        s=s[1:]
    
    ##filter xml tags
    x = s.find(':')
    x+=1
    s=s[x:]


    return s.strip()
def trimDate(s):   
    if(s is None):
        return
    x=s.find("(")
    x-=1
    return s[0:x]
def iterable(obj):
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return True

class DataIterator:
    def __init__(self,data):
        self.data=data
        self._index= 0
    def __next__(self):
        if self._index < (len(self.data.dates)) :
           result = (self.data.dates[self._index], self.data.texts[self._index])
           self._index +=1
           return result
        
       # End of Iteration
        raise StopIteration



class Data:
    def __init__(self):
       self.dates = list()
       self.texts = list()
    def addDate(self, date):
       self.dates.append(date)
    def addText(self, text):
       self.texts.append(text)
    def __iter__(self):
        return DataIterator(self)
    def clear(self):
        self.dates.clear()
        self.texts.clear()

data = Data()



files =["2003-2010.xml","2012-2011.xml","2013.xml","2014.xml","2015-2019.xml"]



for file in files:
    print(file)

    f = open("{}.csv".format(file[0:-4]), "a+", encoding ="utf-8", newline='')
    writer = csv.writer(f)

    with open(file,encoding="utf-8") as f:
        soup = BeautifulSoup(f,"lxml-xml")
        
        i =0
       ## print(len(soup.find_all(["PatronQuestion","PatronIncident","LibraryIncident"])))
        ## look for all patron question tags 
        for n in soup.find_all(["PatronQuestion","PatronIncident","LibraryIncident","Date","Text"]):
            ## loop through and look at all children of patronquestion tag
            for info in n.contents:
                ##find date and text

                if(info.name == "Date"):
                    data.addDate(trimDate(info.string))
                    i = i + 1
                elif(info.name == "Text"):
                    data.addText(trimText(info.string))
                    i = i + 1
                elif(i == 1000):
                    writer.writerows(data)
                    data.clear()
                    i=0


        writer.writerows(data)
        data.clear()
        
    
                
    




        


