class Student:
    def __init__(self,name,age,major,gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
    
    def honour(self):
        if self.gpa > 8:
            return True
        else:
            return False