class classroom:
    def __init__(self, students, boys, girls):
        self.number = students
        self.boys = boys
        self.girls = girls

    def introduction(self):
        print(f"There are {self.number}, {self.boys} are boys and {self.girls} are girls")

    def comparison(self):
        if self.boys > self.girls:
            difference = self.boys - self.girls
            print(f"The boys are {difference} more than the girls")
        elif self.girls > self.boys:
            difference = self.girls - self.boys
            print(f"The girls are {difference} more than boys")
        else:
            print("The boys and girls are equal")

class information(classroom):
    def __init__(self, students, boys, girls, desks, chairs, laptops):
        super().__init__(students, boys, girls)  # removed the extra self
        self.desks = desks
        self.chairs = chairs
        self.laptops = laptops

    def speak(self):
        print(f"Good day, There are {self.desks} desks and {self.chairs} chairs and {self.laptops} laptops")


print(__name__)


if __name__ == "__main__":
    print("done")

    
    students = int(input("Enter the needed students value: "))
    boys = int(input("Enter the needed boys value: "))
    girls = int(input("Enter the needed girls value: "))
    desks = int(input("Enter the needed desks value: "))
    chairs = int(input("Enter the needed chairs value: "))
    laptops = int(input("Enter the needed laptops value: "))
    my_classroom = information(students, boys, girls, desks, chairs, laptops)
    my_classroom.speak()
    my_classroom.introduction()
    my_classroom.comparison()
    my_classroom.speak()