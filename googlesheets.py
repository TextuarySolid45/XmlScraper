##SETUP:
##go to google developer console
##create a service account
##download json credential file
##share file with email in json file
##move file/change name to:
##  linux/MaxOS:~/.config/gspread/service_account.json
##   Windows: %APPDATA%\gspread\service_account.json


import gspread, datetime

##authorized using serivce_account.json
gs= gspread.service_account()

##spreadsheet
ss= gs.open("Times")

##gets 
date=datetime.datetime.now().strftime("%a %x %X")
d=date.split()
##
for wk in ss.worksheets():
    if (wk.title == "Sheet1"):
        print(d[1])
        print(type(wk.find(d[1])))
        
        wk.append_row([d[0],d[1],d[2]])

