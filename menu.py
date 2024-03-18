import sys
import json

from diarybook import Diary, DiaryBook
from util import read_from_json_into_application
from account import Account,User_list


class Menu:

    def __init__(self):
        self.diarybook = DiaryBook()
        self.account = User_list()
        self.dict1={}

        self.choices = {
            "1": self.show_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.populate_database,
            '5': self.quit,
            
        }

    def display_menu(self):
        print(""" 
                     Notebook Menu  
                    1. Show diaries
                    2. Add diary
                    3. Search diaries
                    4. Populate database
                    5. Quit program
                    
                    """)

    def run(self):
            self.create_eccount()
            while True:
                self.display_menu()
                choice = input("Enter an option: ")
                action = self.choices.get(choice)
                if action:
                    action()
                else:
                    print("{0} is not a valid choice".format(choice))

    def show_diaries(self, diaries=None):
        if not diaries:
            diaries = self.diarybook.diaries
        for diary in diaries:
            print(f"{diary.id}-{diary.memo}")

    def add_diary(self):
        memo = input("Enter a memo:         ")
        tags = input("add tags:             ")
        self.diarybook.new_diary(memo, tags)
        print("Your note has been added")
        print(self.diarybook.new_diary)
        #data= self.diarybook.diaries
        #for x in data:
        self.dict1[self.diarybook.id]=memo

        with open ("data.json","a") as file:
            json.dump(self.dict1,file)
        
                    

    def search_diaries(self):

        filter_text = input("Search for:  ")
        diaries = self.diarybook.search_diary(filter_text)
        for diary in diaries:
            print(f"{diary.id}-{diary.memo}")

    def quit(self):

        print("Thank you for using diarybook today")
        sys.exit(0)

    def populate_database(self):
        diaries1 = read_from_json_into_application('data.json')
        for diary in diaries1:
            self.diarybook.diaries.append(diary)

    def create_eccount(self):
        x=input("login or sing up ")
        if x == "sing up":
            name=input("enter your name ")
            lastname =input("enter your lastname ")
            password = input("enter password ")
            self.account.new_account(name,lastname,password)
            if name not in self.account.data_list and password not in self.account.data_list:
                    print (self.account.account_list)
                    self.account.add_data(name,password)
                    
                
            else:
                print("Change the password")
        elif x== "login":
            name = input("enter your name ")
            password = input("enter your password ")
            if  name in self.account.data_list and password in self.account.data_list:
                print("welcome")

            else:
                print("Invalid password")
            
           
            

    #def write_into_json(self):
    #    data= self.diarybook.diaries
    #    for x in data:
    #        self.dict1[x.id]=x.memo
#
    #    with open ("data.json","w") as file:
    #        json.dump(self.dict1,file)
                    


    
        
        
        



if __name__ == "__main__":
    Menu().run()
