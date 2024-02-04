class student:
    university='SkilWill'
    def __init__(self,name,grade,age):
        self.name =name 
        self.grade =grade
        self.age =age
    def __str__ (self):
        return f"name:{self.name},grade:{self.grade},age:{self.age}"
    @property
    def is_passing(self):
        if self.grade>60:
            return True
        else:
            return False
    def increase_grade(self,value):
        self.value=value
        Grade=self.grade+self.value
        print (Grade)
    
student1 = student("dato",10,20)
print(str(student1))
print(student1.is_passing)
student1.increase_grade(10)

