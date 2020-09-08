import xml.etree.ElementTree as ET
import io
tree = ET.parse('/Users/Jennifer Lopez/Downloads/2013.xml')
root = tree.getroot()


list =[]
##with io.open('/Users/Jennifer Lopez/Desktop/Python/allTags.txt', "w", encoding="utf-8") as f:
for neighbor in root.iter():
    ##f= open('/Users/Jennifer Lopez/Downloads/clean.txt','w')
    
    
    if(neighbor.text != None and neighbor.tag != None): 
       print(neighbor.tag+neighbor.text)

