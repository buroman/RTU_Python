'''

THIS PROGRAMM HAS BEEN MADE TO ASSIST TO FOLLOW/TRACE THE DEADLINES OF THE "SEND OUT" REQUESTS TO THE CLIENTS. 
IN THE FUTURE, I AM GOING TO USE TELEGRAM LIBRARIES AND MAKE THE TELEGRAM BOT WHICH WILL SEND REMINDERS AUTMATICALY TO THE MOBILE PHONE 
AS WELL NEW FUNCTIONS WILL BE ADDED WHEN I WILL BE MORE COMPETENT.

'''

import datetime
import json
from time import strftime # FOR OPTION - DEADLINE
import sys  # FOR EXITING THE SCRIPT

my_dict = {}

# INFORMATION EXTRACTING TO "DICT" FROM THE "JSON FILE" - IT STARTS FIRST. AFTER INFO EXTRACTION JSON FILE IS AUTOMATICALLY CLOSED

def info_from_json():                              #COMMENT:
    with open('diana_reminder.json', 'r') as f:    # IF WE HAVE GREATED A NEW FILE, WE HAVE TO WRITE IT In  {} (EMPTY DICT)
        read = json.load(f)                        # IN OTHER WAY - WE WILL GET THE ERROR
        my_dict.update(read)
        f.close()

# CONTROL PANEL FUNCTION. THIS FUNCTION STARTS AFTER INFO EXTRACTION AND WE CAN CHOOSE ONE OF THE 3 OPTIONS:

def menu():
    marker = ''
    marker = input('New input: n \nData check: c\nExit: e \n')
    if marker == 'n':
        return add_info()  # WE CAN ADD NEW INFORMATION (SUBJECT NAME AND DEADLINE)
    elif marker == 'c':
        return data_chek_from_json()   # WE CAN CHECK OUR DEADLINES
    elif marker == 'e':
        return exit() # SAVE INFORMATION FROM THE DICTIONARY AND CLOSE THE PROGRAMM
    else:
        return menu()

# INFORMATION CHECK REGARDING DEADLINES
    
def data_chek_from_json():

    for k,v in my_dict.items():
 
        dt_time = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S") # CONVERTS DEADLINE "ISO STRING" TO THE "DATETIME" FORMAT

        now = datetime.datetime.now()
        delta = dt_time - now # TIME PERIOD BETWEEN DEADLINE AND NOW

        if  delta.days > 14:
            print("DEADLINE for ", k ," is: ", dt_time, "!  You have time: ",dt_time - now) # NO REMINDERS
        elif 3 < delta.days < 15:
            print("Reminder: provide documents for ", k ," you have only ",delta.days," days till DEADLINE!" ) # FIRST REMINDER
        elif 0 < delta.days < 4:
            print("LAST Reminder: provide documents for ", k ," you have only ",delta.days," days till DEADLINE!" ) # FINAL REMINDER
        elif delta.days < 0:
            print("DEADLINE was: ", dt_time, "Your account is closed") # TIME EXCEEDED, CLOSURE OF THE CLIENT'S ACCOUNT

# INFORMATION ADDING FUNCTION TO THE DICTIONARY      
            
def add_info():
    
# INPUT THE COMPANY NAME
    
    company_name = input("Input the company name: ")    # ADD SUBJECT NAME
    
# INPUT OF THE DEADLINE
    
    year = int(input("year: "))
    month = int(input("month: "))
    day = int(input("day: "))
    deadline_ISO = datetime.datetime(year, month, day).isoformat() # CONVERTS DEADLINE IN TO THE  "ISO FORMAT", TO CONVERT DEADLINE INFO TO STRING AND SAVE IT TO JSON FILE
    my_dict.update({company_name:deadline_ISO})      # ADD NEW INFORMATION TO THE DICTIONARY

# EXIT AND INFORMATION SAVE TO JSON FILE FUNCTION

def exit():
    with open('diana_reminder.json', 'w') as f:  # OVERWRITE INFORMATION TO THE JSON FILE AN CLOSE IT
        data = json.dump(my_dict,f)
        f.close()
        print("You are not in the programm!")
        print(sys.exit())    # EXIT FROM THE SCRIPT
        
# PROGRAM CODE
      
while True:
    
    info_from_json()
    menu()
    
    continue
