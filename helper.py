from enum import Enum
import csv
import os

# enam
class Actions(Enum):
    ADD = 1
    DELETE = 2
    PRINT = 3
    SEARCH = 4
    APDATE = 5
    EXIT = 6


# def the array var
cars =[]


# print menu and get user selection
def display_menu():
    for x in Actions:
        print(f"{x.value} - {x.name}")
    return Actions(int(input("inter your selection: ")))

# conect each selection to the accurate function
def menu():
    while True:
        user_selection = display_menu()
        if user_selection == Actions.ADD: add()
        if user_selection == Actions.DELETE: delete()
        if user_selection == Actions.PRINT: print(f"""there are corrently {len(cars)} cars on the list
    {cars}""")
        if user_selection == Actions.SEARCH: search()
        if user_selection == Actions.APDATE: apdate()
        if user_selection == Actions.EXIT: return

# add an item to list
def add():
    cars.append({f"color": input("inter color") , "model" : input("inter model"), "type": input("inter type")})

# search an item in the list
def search(): 
    if not cars:
        print("list is empty")
        return
    found_car = None
    input_car = input("Enter car type")
    for car in cars:
        if car["type"] == input_car:
            found_car = car
            print (found_car)
    if found_car == None:
        print("not found")
    return found_car

# delete an item from list
def delete():    
    car2del = search()  
    if car2del != None: 
        cars.remove(car2del)  
        print("was deleted")       

# apdate details of a specific item
def apdate():
    if not cars:
        print("No list")
        return
    car2update = search()
    if car2update:
        car2update["color"] = input("Enter new color: ")
        car2update["model"] = input("Enter new model: ")
        print("successfully updated")

# save list to CSV when program end
def save():
    if cars:
        with open("cars.csv", "w", newline="") as csvfile:
            fieldnames = ["color", "model", "type"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for car in cars:
                writer.writerow(car)
        print("Data saved to cars.csv")
    else:
        print("No data to save")

# load list from CSV when program starts
def load():
    with open("cars.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cars.append({"color": row["color"], "model": row["model"], "type": row["type"]})    

# terminal - clear and change font color when program starts
def terminal():
    os.system("cls")
    os.system("color 0A")
