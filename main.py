from sqlClient import mySqlClient
import json

file = open('config.json', 'r')
configData = json.load(file)

sqlClient = mySqlClient(username=configData['user'], password=configData['pass'], host=configData['host'], database=configData['database'], port=configData['port'])

def homeScreen():
    print("Welcome to the Employee Management System!")
    print("1. Add New Employee")
    print("2. Delete An Employee")
    print("3. Update An Employee")
    print("4. View All Employees")
    
    

   

    
    




def allEmployeeScreen():
    print("View All Employees Screen")
    employees = sqlClient.getAllEmployees()
    if employees:
        for employee in employees:
            print(employee)
    else:
        print("No employees in the database.")

   
try:
    while True:
        allEmployeeScreen()
except KeyboardInterrupt:
    print("closing......................")
