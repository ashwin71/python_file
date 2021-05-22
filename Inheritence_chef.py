class Chef:
    #self is neccessary since it cause error called 1 positional argument
    def __init__(self):
        pass
    def make_chicken(self):
        print("chef is making chicken")
    def make_special_dish(self):
        print("chef making beef biriyani")
    def make_biriyani(self):
        print("chef making biriyani")


new_chef = Chef()
new_chef.make_biriyani()