#homework-5
class person:
    def __init__(self,name,surname,age):
        self.name =name
        self.surname= surname
        self.age = age
class mixin:
    def __str__(self):
        return f"name:{self.name} surname:{self.surname} age:{self.age}"
    
class student(mixin,person):
    def __init__(self,name:str,surname:str,age:int,university:str):
        self.university = university
        super().__init__(name,surname,age)
    def get (self):
        print(self.name, self.surname,  self.age, self.university)
        
student1=student("Dato","Tsertsvadze",20,"SkillWill")
student1.get()
print(str(student1))