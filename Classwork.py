class Dog:


    def __init__(self, breed= "", color="", gender=""):
        self.breed = breed
        self.color = color
        self.gender = gender
    def __str__(self):
        return (f"The {self.breed} is {self.color} and it is {self.gender}")

class Person:
    def __init__(self, height= 0, weight= 0):
        self.height = height
        self.weight = weight
    def __str__(self):
        return(f"{self.weight /self.height*self.height*703}")
    def updateBMI(self,height, weight):
        self.height = height
        self.weight = weight


class Product:
    def __init__(self, name= "", price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return(f"The {self.name} is ${self.price} for {self.quantity}")
    # def changeProduct(self, newName, newPrice, newQuantity):
    #     self.name = newName
    #     self.price = newPrice
    #     self.quantity = newQuantity



def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()

# Create a class Dog. Make sure it has the attributes name, breed, color, gender. Create a function that will print all attributes of the class. Create an object of Dog in your problem1 function and print all of it's attributes.
def problem1():
    newDog = Dog("Yorkie", "Black", "Female")
    print(newDog)


# Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.
def problem2():
    userInput = ""
    while userInput != "=":
        userInput= input("Enter something ")
        print(userInput)


# In your main file create three Person objects. Change the weight and height of each one. Afterwards, print the BMI (body mass index) of each Person. If you don’t know how to calculate BMI, look at the code I provided for you.
#
# Hint: BMI is (weight / (height * height)) x 703. Weight is in pounds and height is in inches.
#
# Extra:Put the three person objects in an array and use a loop to print out their BMIs.
def problem3():
    newPerson1 = Person(52,175)
    newPerson2 = Person(60,200)
    newPerson3 = Person(40,120)
    newPerson1.updateBMI(54,150)
    newPerson2.updateBMI(65,175)
    newPerson3.updateBMI(43,140)
    print(newPerson1)
    print(newPerson2)
    print(newPerson3)



# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
#
# The class should have changeProduct:
#
# a) If changeProduct has one parameter, it can change the name of the product.
#
#     b) If changeProduct has two parameters it can change the name and price of the product.
#
#     c) If changeProduct has three parameters it can change the name, price, and quantity of the product.
#
# Create an object of Product in your problem4 function and print all of it's attributes.
def problem4():
    newProduct1 = Product("Apple Iphone",1000,1)
    newProduct2 = Product("Samsung")
    newProduct3 = Product("Samsung",2000)
    newProduct4 = Product("Samsung",2000,2)

    print(newProduct1)
    print(newProduct2)
    print(newProduct3)
    print(newProduct4)







if __name__ == '__main__':
    main()