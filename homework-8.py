from abc import ABC, abstractmethod
class   Person(ABC):

    @abstractmethod
    def displaye_details(self):
        pass
class Student(Person):
    list1=[]
    
    def __init__(self,student_id,name,grade):
        self.student_id = student_id
        self.name=name
        self.grade=grade
        

    def add_grade(self):
        while (True):
            w=input("enter a grade--> Press Enter when you are finished entering your grade: ")
            try:
                if type(int(w)) is int and int(w)>0:
                    self.list1.append(int(w))
                    print(self.list1)
            except:
                    print("The grade given to the student is ",self.list1)
                    break
                
    def avarage_grade(self):
        self.list1.append(self.grade)
        self.avarage=sum(self.list1)/len(self.list1)
        print("student avarage grade is ",self.avarage)
    @property
    def displaye_details(self):
        print( "student id is",self.student_id,"name is" ,self.name,"avarage grade is",self.avarage)

student1 = Student( "123","dato",10)
student1.add_grade()
student1.avarage_grade()
student1.displaye_details