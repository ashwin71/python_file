from Inheritence_chef import Chef
#    name of the file        class name
#Inheritence chef class all methods are available in this new class this called inheritance
#The same method is overridden by this class(make_special_dish in here)

class Chinese_chef(Chef):
    def __init__(self) -> None:
        pass
    
    def make_chinese(self):
        print("making chinese biriyani")

    def make_special_dish(self):
        print("make chinese beef chukkaa")


new_chef1 = Chinese_chef()
new_chef1.make_chicken()
new_chef1.make_special_dish()