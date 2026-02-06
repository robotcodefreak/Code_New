#class 1: BOOK

class book:
    def __init__(self, tob, author, pages):
        self.tob = tob
        self.author = author
        self.pages = pages
    def display(self):
        print(f"The book {self.tob} is {self.pages} pages long and is written by {self.author} ")
    def long(self):
        if self.pages <= 499:
            print("THIS BOOK IS SHORTER THEN YOU, KING")
        elif self.pages >= 500:
            print("MY GLORIOUS KING THATS A LOOOOONG BOOOOOK")
HP = book("Harry Potter", "J.K. Rowling", 500)
HP.display()
HP.long()
#class 2: STUDENT
# Attributes: name, age, grade
# Methods: get grade, check if passing
class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        print(f"{self.name}'s current grade is {self.grade}")
    def ispassing(self):
        if self.grade <= 55:
            print (f"{self.name} is an absolute dumbass")
        elif self.grade > 55:
            print (f"{self.name} cooked.")
Student1 = student("Cameron Fee", 13, 90)
Student1.ispassing()
Student1.get_grade()
#Class#6 (skipping a few):InventoryItem
# Attributes: name, quantity, price
# Methods: restock, sell, total value

