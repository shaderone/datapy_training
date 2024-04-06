"""program 1 - print hello world"""

#def main():
#    print("hello world")


#---------------------------------------------------------------------------------------------
""" program 2 - Python program to do sum of 'n' numbers, after taking inputs from the user """

#def main():
#    limit = int(input("Enter the number of numbers you want to sum: "))
#    print(f"Sum of the Given numbers is : {getResult(limit)}")
#    
#
#def getResult(limit): 
#    total = 0;
#    for index in range(limit):
#        num = float(input("Enter the number : "))
#        total += num;
#    
#    return total
#


#---------------------------------------------------------------------------------------------
"""Program 3 -Write a python program to find the area of a square and rectangle."""

#def getAreaSquare(side):
#    return side*side
#
#def getAreaRectangle(length, breadth):
#    return length*breadth
#
#def main():
#    choice = int(input("Find Area of 1 - Square, 2 - rectangle : "))
#    if choice == 1:
#        side = float(input("Enter side dimension : "))
#        print(f'Area of square = {getAreaSquare(side)}')
#    elif choice == 2: 
#        length = float(input("Enter the length of rectangle: "))
#        breadth = float(input("Enter the breadth of rectangle: "))
#        print(f'Area of rectangle = {getAreaRectangle(length, breadth)}')
#    else: 
#        print("Invalid input")


#---------------------------------------------------------------------------------------------
"""Program 4 - Create a string & get the characters of string from 2 to 18 using both positive and negative indexing."""

#def main():
#    string = "redbull give you wings"
#    stringSlicePositive = string[2:18]
#    stringSliceNegative = string[-20: -4]
#    print(f'Postive slicing : {stringSlicePositive} \nNegative slicing : {stringSliceNegative}')

#---------------------------------------------------------------------------------------------
"""Program 5 - Create and print a list with same and different items."""

#def main():
#    listWithMixedItems = ["Verstappan", "Leclerc", "Hamilton", 1, 16, 44, True, False]
#    print(listWithMixedItems)

#---------------------------------------------------------------------------------------------
"""Program 6 - Access an item from the list using its index."""

#def main():
#    twoStrokesList = ["Rx", "Shogun", "GT750"]
#    print(twoStrokesList[0])

#---------------------------------------------------------------------------------------------
"""Program 7 - Access an item from the list using negative index."""

#def main(): 
#    hyperCars = ["Agera", "Valkyrie", "Chrion"]
#    print(hyperCars[-3])


#---------------------------------------------------------------------------------------------
"""Program 8 - Modify an item in the list."""

#def main():
#    jdms = ["GT r34", "shelby GT 500", "supra mk5"]
#    print(f"Before : {jdms}")
#    jdms[1] = "Lancer Evo"
#    print(f"\nAfter : {jdms}")

#---------------------------------------------------------------------------------------------
"""Program 9 - Access the items in the list using slicing."""

#def main():
#    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    #Acces right before index 2
#    print(numbers[:2])
#    #Access every third item
#    print(numbers[::3])
#    #Access item using negative index
#    print(numbers[-2:])
    

#---------------------------------------------------------------------------------------------
"""Program 10 - Create a dictionary and print it."""

#def main():
#    dictionary = {
#        "name": "Porsche",
#        "model": "GT3 RS",
#        "in_production": True,
#        "make_year" : 2003,
#    }
#
#    for key, value in dictionary.items():
#        print(f'{key} : {value}')

#---------------------------------------------------------------------------------------------
"""Program 11 - Change the value of a key."""

def main():
    person = {
        "name" : "Eren",
        "age" : 19,
        "place" : "paradis Island",
        "isAlive" : True,
    }

    person["isAlive"] = False

    for key, value in person.items():
        print(f'{key} : {value}')


#---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()