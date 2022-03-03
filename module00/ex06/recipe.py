
ingreds = ["ham","bread","cheese","tomatoes"]
meal = "lunch"
prep_time = 10
sandwich = {'ingredients': ingreds,'meal': meal,'prep_time': prep_time}
ingreds = ["flour","sugar", "eggs"]
meal = "dessert"
prep_time = 60
cake = {'ingredients': ingreds,'meal': meal,'prep_time': prep_time}
ingreds = ["avocado","tomatoes","arugula","spinach"]
meal = "lunch"
prep_time = 15
salad = {'ingredients': ingreds,'meal': meal,'prep_time': prep_time}
cookbook = {'sandwich': sandwich,'cake': cake,'salad': salad}

def printrecipename(cookbook):
    for recipe in cookbook:
        print(recipe)

def details(recipe):
    print("ingredients list:",recipe['ingredients'])
    print("to be eaten for",recipe['meal'])
    print("takes",recipe['prep_time'],"minutes of cooking")

def delete(recipe):
    cookbook.remove(recipe)

def addrecipe():
    name = input("recipe name : ")
    ingred = input("enter the list of ingredients(spaces between) : ")
    ingreds = ingred.split()
    meal = input("enter meal type : ")
    prep_time = int(input("enter prep time : "))
    recipe = {'ingredients': ingreds,'meal': meal, 'prep_time':prep_time}
    cookbook[name] = recipe
def options():
    print("Welcome to the Python Cookbook !\nList of available option:")
    print("1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit")

def app():
    option = int(input("please select an option :\n"))
    if(option == 1):
        addrecipe()
    elif(option == 2):
        recipe = input("enter the recipe to delete")
        delete(recipe)
    elif(option == 3):
        addrecipe()
    elif(option == 4):
        printrecipename(cookbook)
    elif(option == 5):
        print("Cookbook closed. Goodbye !")
    else:
        print("Sorry, this option does not exist.")
        options()

options()
app()