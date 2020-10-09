# Hello this is my .py file for oop
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_person_details(self):
        return self.name,self.age
    def set_name(self,name):
        self.name = name
    
p = Person("Qazi Arsalan",20)
name,age= p.get_person_details()
print(f"{name} : {age}")