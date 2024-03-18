class Account:
    def __init__(self,name,lastname,password):
        self.name=name
        self.lastname=lastname
        self.password=password

        
class User_list(Account):
    def __init__(self):
        self.account_list=[]
        self.data_list=[]

    
    def new_account(self,name,lastname,password):
        #self.account_list.append(Account(name,lastname,password))
        if name not in self.data_list and password not in self.data_list:
       
            self.account_list.append(name)
            self.account_list.append(lastname)
            self.account_list.append(password)

    def add_data(self,name,password):
        with open("User","+a") as file1:
            self.data2 = file1.read()
            for x in self.data2.strip().splitlines():
                self.data_list.append(x)
                self.data_list.copy
            if name not in self.data_list and password not in self.data_list:
                self.data =self.account_list[0]
                self.data1 =self.account_list[2]
                file1.write(self.data+"\n")
                file1.write(self.data1+"\n")

    


