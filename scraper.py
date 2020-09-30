""" download the xml file, it is called 2013.xml 
and put it in the same directory as this script

I use the element tree library to parse the file
https://docs.python.org/2/library/xml.etree.elementtree.html 

right now, this file outputs all the chat text in
the format of "date \t chat text" into a text file

"""

import csv
import xml.etree.ElementTree as ET
import io
tree = ET.parse('2013.xml')
root = tree.getroot()

##*s acts as a array but doesnt assume so
def trim(*s):
    if(s[0] == "<br>"):
        return True
    else: 
        return False


print(trim("<br>"))


list =[]
with open('output.csv', newline='') as f:
    writer = csv.writer(f)
    
    for neighbor in root.iter("PatronQuestion"):
        ##f= open('clean.txt','w')
        
        if(neighbor.text != None and neighbor.tag != None): 
            ##f.write("{}\t{}".format(neighbor.tag,neighbor.text))
            ##f.write("{}\n".format(str(type(neighbor))))

            for child in neighbor.iter():
                if(child.tag =="Date"):
                    writer.writerows(child.text)
                    f.write("{}\t".format(child.text))
                elif(child.tag == "Text"):
                    if(trim(child.text)):
                        writer.writerows(child.text)
                        f.write("{}\n".format(child.text.split()[1:]))
                    else:
                        writer.writerows(child.text)
                        f.write("{}\n".format(child.text))

    f.close()