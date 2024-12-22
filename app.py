import os 
import platform
import json
from enum import Enum
import ast

class Actions(Enum):
    EXIT = 0
    DELETE = 1
    SEARCH = 2
    ADD = 3
    DISPLAY = 4
    
cars=[]

def menu(): 
    load_to_cars_display()
    for act in Actions: print(f"{act.value} - {act.name}" )
    return input("choose desired action:")

def clear_terminal():
    os.system('clear') 

def add_cars():
    cars.append({"brand" :input("Brand:"), "model": input("Model:"), "color": input("color:")})
    write_cars_to_file ()
    return

def display_cars ():
    load_to_cars_display ()
    global cars
    for index, car in enumerate(cars):
        print(str(f"Brand: {car['brand']} , Model: {car['model']}, Color: {car['color']}"))

def write_cars_to_file ():
    global cars
    FILE_NAME = 'garage.txt'
    with open(FILE_NAME, 'w+') as f:      
            f.write(str(cars))
            
    f.close() 

def load_to_cars_display():
    global cars
    try:
        FILE_NAME = 'garage.txt'
        with open(FILE_NAME, 'r') as f:
            cars = ast.literal_eval(f.read())
    except Exception as e:  
        print(f"Error loading cars: {e}")
 
def delete_car_from_file():
    global cars
    display_cars()
    delete_selection = input("Choose Brand to delete:")
    deleted = False
    for car in cars[:]:
        if delete_selection == car['brand']:
            cars.remove(car)
            deleted = True
            break
    if deleted:
        print(f" car:{car['brand']}-deleted")
        write_cars_to_file()
        load_to_cars_display ()  
    
def find_car_from_file ():
    global cars
    find_brand = input("look for desired brand:")
    exist = False
    FILE_NAME = 'garage.txt'
    with open(FILE_NAME, 'r') as f:
            for car in cars:
               if find_brand == car['brand']:
                   exist=True
                   break
    if exist:print(str(f"Brand: {car['brand']} , Model: {car['model']}, Color: {car['color']}"))
    else: print("too short on the prudcut")
    return

if __name__ == "__main__":
        user_selection = Actions(int(menu()))
        clear_terminal()
        if user_selection == Actions.EXIT : exit()
        elif user_selection == Actions.ADD:add_cars()
        elif user_selection == Actions.DELETE: delete_car_from_file()
        elif user_selection == Actions.DISPLAY: display_cars()
        elif user_selection == Actions.SEARCH: find_car_from_file()
        else: print("pls choose from the menu")
         



    