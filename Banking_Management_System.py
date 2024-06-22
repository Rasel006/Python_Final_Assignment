# rizurasel.cse@gmail.com
# project: Banking Management System
# Final Exam
# Submission Date: 15/10/2023

# test push code 
# for random numbers
import random

class User:

    def __init__(self, Name, Address, Email, Password, AcType) -> None:

        self.Name=Name
        self.Address=Address
        self.Email=Email
        self.Password=Password
        self.AcType=AcType
        self.AcNumber=17841000+random.randint(1,1000)
        self.Balance=00.00
        self.Loan_Cnt=00.00
        self.Total_Take_Loan=00.00
        self.Trans_History=[]
        

    def Withdraw(self, Amount):

        if Admin.Bankrupt:

            print("Now this Bank Bankrupt; So you cannot withdraw any money!")
        else:

            if self.Balance>= Amount:
                self.Balance-= Amount
                self.Trans_History.append(f"Withdrew your Money {Amount}")
                print(f'{Amount} Tk and your money Withdraw Successfuly!')

            else:
                print("Extremely Sorry, your account have not sufficient Money for this withdraw request.")
        
    def Deposit(self, Amount):
        if Admin.Bankrupt:
            print("Now this Bank Bankrupt; So you cannot deposite any money!")
        else:
            self.Balance+= Amount
            self.Trans_History.append(f"Deposited your money {Amount}")
            print(f'{Amount} Tk and your money Deposit Successfuly!')
            
    
    def BalanceCheck(self):

        return f"Your available account balance: {self.Balance}"
    
    
    def TransferMoney(self, Receiver, Amount):
        if Admin.iBankrupt:

            print("Now this Bank Bankrupt.So you cannot Transfer any money!")

        else:
            if Receiver:
                if Amount <= self.Balance:
                    self.Balance -= Amount
                    Receiver.Balance += Amount
                    self.Trans_History.append(f"Transfer Money {Amount} To {Receiver.Name}!")
                    Receiver.Trans_History.append(f"Receiver Money {Amount} From {self.Name}!")
                    print(f"{Amount} Transfer Money To {Receiver.Name} Successfully.") 
                else:
                    print("Sorry, you have not sufficient money") 
            else:
                print("Sorry, your account doesn't exists.")
    
    def TransHistoryCheker(self):
        return self.Trans_History
    
    def Loan(self, Amount):

        if Admin.Bankrupt:
            print("Now this Bank Bankrupt.So you cannot take any money loan!")
        else:
            if Admin.Loan:
                if self.Loan_Cnt < 2:
                    self.Loan_Cnt += 1
                    self.Total_Take_Loan += Amount
                    self.Balance += Amount
                    self.Trans_History.append(f" Your loan money {Amount} adding your account.")
                    print(f"{Amount} You money loan receive successfully.") 
                else:
                    print(f"Before already taken 2 time money loan.") 
            else:
                print("Sorry you are not eligible for the loan! Contacts your near Branch")
                
    def __repr__(self) -> str:
        return f"Bank A/c Number: {self.AcNumber}\nAcoount Name: {self.Name}\nAcoount Email: {self.Email}\nPresent Address: {self.Address}\nYour Bank Account Type: {self.AcType}\nAccount Balance: {self.Balance:.4f}\nMoney Loan: {self.Total_Take_Loan:.4f}"

class Admin(User):
    def __init__(self) -> None:
        self.Users=[]
        self.IsLoan=True
        self.Bankrupt=False
          
    def AccountCreate(self, Name, Address,Email,Password, AcType) -> None:
        Userr = User(Name,Address,Email,Password,AcType)
        self.Users.append(Userr)
        return Userr
    
    def Log_in(self,Email, Password):
        for Userr in self.Users:
            if Userr.Email == Email and Userr.Password == Password:
                return Userr
        return None
    
    def AccountsList(self):
        return self.Users
    
    def AccountDelete(self, Userr):
        if Userr in self.Users:
            self.Users.remove(Userr)
    
    
    def BankBalanceTotal(self):
        return sum(Userr.Balance for Userr in self.Users)

    def LoanAmountTotal(self):
        return sum(Userr.Total_Take_Loan for Userr in self.Users)
        
    def LoanTake(self,aLoan):
        self.iLoan =aLoan
    
    def BankruptSet(self,bankrupt):
        self.xBankrupt =bankrupt

Admin = Admin()
AccountUser1 =Admin.AccountCreate("Md. Rasel", "Tangail","rizuraselcse@gmail.com","10144","Sevings")

AccountUser2 =Admin.AccountCreate("MD. Tahsin Ferdoues", "Cox's Bazar","tahsin23@gmail.com","10684","Sevings")

AccountUser3 =Admin.AccountCreate("Rezuan Alam Rean", "Chittagong","rean211@gmail.com","10594","Sevings")

while True:
    try:
        print()

        print("\n___FSIB Online Banking Management System___")
        print("1 User Section")
        print("2 Admin Section")
        print("3 All Exits")
    
        enter_choice = input("Please enter choice an option number: ")

        if  enter_choice== "1":
            print("User Section\n")
            print("1 Account Registration")
            print("2 Account Login")
            print("3 All Exits")
    
            op= input("Please enter choice an option number: ")
        
            if op== "1":
                UserName = input("Write your name: ")
                UserAddress = input("Write your address: ")
                UserEmail = input("Write your email: ")
                UserPassward = input("Write your password: ")
                UserType = input("Write account type (Savings/Current): ")
                UserAccount =Admin.AccountCreate(UserName,UserAddress,UserEmail,UserPassward,UserType)
        
                while True:
                    print("\nUser Account Profile")
                    print("1 Deposit Money")
                    print("2 Withdraw Money")
                    print("3 Account Balance Check")
                    print("4 Account Transaction History")
                    print("5 Money Loan")
                    print("6 Account Transfer Money")
                    print("7 Account Log Out")
                    
                    user_select = input("Please enter choice an option number:")

                    if user_select == "1":
                        Amount = float(input("Please enter your Deposit amount: "))
                        UserAccount.Deposit(Amount)
                    elif user_select == "2":
                        Amount = float(input("Please enter your withdraw amount: "))
                        UserAccount.Withdraw(Amount)
                    elif user_select == "3":
                        print(f"{UserAccount.BalanceCheck()}")
                    elif user_select== "4":
                        print("\nYour Account Transaction History:")
                        for trans in UserAccount.TransHistoryCheker():
                            print(trans)
                    elif user_select == "5":
                        AmountLoan = float(input("Please enter your loan amount: "))
                        UserAccount.Loan(AmountLoan)
                    elif user_select == "6":
                        Receiverid = int(input("Please enter your receiver account number: "))
                        Receiver = None
                        for Userr in Admin.Users:
                            if Userr.AcNumber == Receiverid:
                                Receiver=Userr
                                break
                        if Receiver:
                            Amount = float(input("Please enter your transfer money amount: "))
                            UserAccount.TransferMoney(Receiver, Amount)
                        else:
                            print("Sorry Your receiver's account doesn't exists.")
                    elif user_select== "7":
                        break
                    else:
                        print("Sorry you select Unknown Option")
            elif op =="2":
                UserEmail = input("Please Enter your account email: ")
                UserPassward = input("Please enter your account password: ")
                UserAccount =Admin.Log_in(UserEmail,UserPassward)
            
                if UserAccount:
                    print(f'{UserAccount.Name},Account successfully login!')
                    while True:
                        print("\nUser Account Profile")
                        print("1 Deposit Money")
                        print("2 Withdraw Money")
                        print("3 Account Balance Check")
                        print("4 Transaction History")
                        print("5 Money Loan")
                        print("6 Account Transfer Money")
                        print("7 Accoount Log Out")
                    
                        user_select = input("Please enter choice an option number:")

                        if user_select == "1":
                            Amount = float(input("Please enter your deposit amount: "))
                            UserAccount.Deposit(Amount)
                        elif user_select == "2":
                            Amount = float(input("Please enter your withdraw amount: "))
                            UserAccount.Withdraw(Amount)
                        elif user_select == "3":
                            print(f"{UserAccount.BalanceCheck()}")
                        elif user_select == "4":
                            print("\nYour Account Transaction History:")
                            for trans in UserAccount.TransHistoryCheker():
                                print(trans)
                        elif user_select== "5":
                            AmountLoan = float(input("Please enter your loan amount money: "))
                            UserAccount.Loan(AmountLoan)
                        elif user_select== "6":
                            Receiverid = int(input("Please enter your receiver's account number: "))
                            Receiver= next((Userr for Userr in Admin.Users if Userr.AcNumber ==Receiverid), None)
                            if Receiver:
                                Amount = float(input("Please enter your transfer amount: "))
                                UserAccount.TransferMoney(Receiver, Amount)
                            else:
                                print("Sorry your receiver's account doesn't exists.")
                        elif user_select == "7":
                            break
                        else:
                            print("Sorry you select Unknown Option")
                else:
                    print('Login failed. Invalid email or password.')
            elif op== "3":
                break
            else:
                print("Sorry you select Unknown option!")
        elif enter_choice == "2":

            print('This is your admin passward = #AD@7878')

            Adpassword = input("write your admin password: ")

            print('admin passward = admin123')
            if Adpassword == "#AD@7878":
                while True:
                    print("\nAdmin Profile")
                    print("1 Click for Create a User Account ")
                    print("2 Click for Delete a User Account")
                    print("3 View for All User Accounts")
                    print("4 Check Total FSIB Bank Balance")
                    print("5 Check Total Loan Amount")
                    print("6 Click for Loan Feature")
                    print("7 FSIB Bankrupt")
                    print("8 Admin Log Out")

                    admin_select = input("Please enter an option: ")

                    if admin_select == "1":
                        try:
                            UserName = input("Please write user's name: ")
                            UserAddress = input("Please write user's present address: ")
                            UserEmail = input("Please write user's email id: ")
                            UserPassward = input("Please write account password: ")
                            UserType = input("Please write account type (savings/Current ): ")
                            Admin.AccountCreate(UserName, UserAddress,UserEmail, UserType,UserPassward)
                        except ValueError:
                            print("Sorry you enter Unknown Option! Please enter a correct number.")
                            continue
                    elif admin_select == "2":
                        try:
                            AcNumber = int(input("Please write the User ID for delete users: "))
                            UserDelete = next((Userr for Userr in Admin.Users if Userr.AcNumber == AcNumber), None)
                            if UserDelete:
                                Admin.AccountDelete(UserDelete)
                                print(f"This User account ID {AcNumber} delete successfully.")
                            else:
                                print("This User account  doesn't exits.")
                        except ValueError:
                            print("You enter Unknown  Option! Please write  a correct option number.")
                            continue
                        
                    elif admin_select == "3":
                        try:
                            print("\nUser Accounts List:")
                            for Userr in Admin.AccountsList():
                                print(Userr)
                        except ValueError:
                            print("You enter Unknown  Option! Please write  a correct option number.")
                            continue
                    elif admin_select == "4":
                        print(f"Total FSIB Bank Balance: ${Admin.BankBalanceTotal()}")
                    elif admin_select == "5":
                        print(f"Total FSIB Loan Amount: ${Admin.BankBalanceTotal()}")
                    elif admin_select == "6":
                        while True:
                            print("\nLoan")
                            print("1 Enable")
                            print("2 disable")
                            bankrup_select= input("Please choice an option:")
                            
                            if bankrup_select=="1":
                                Admin. LoanTake(True)
                                print("can take a loan")
                                break
                            elif bankrup_select=="2":
                                Admin. LoanTake(False)
                                print("Cannot take loan")
                                break
                    elif admin_select== "7":
                        while True:
                            print("\nFSIB Bankrupt ")
                            print("1 Yes")
                            print("2 No")
                            bankrup_select= input("Please select an option:")
                            
                            if bankrup_select=="1":
                                Admin.BankruptSet(True)
                                print("Now FSIB Bankrupt(bankrupt).")
                                break
                            elif bankrup_select=="2":
                                Admin.BankruptSet(False)
                                print("Now FSIB is not Bankrupt(No)")
                                break
                                
                    elif admin_select== "8":
                        break
            else:
                print("Wrong passward.Please try again!")
        elif enter_choice == "3":
            print("Thank you for choosing our bank management system! We appreciate your trust in our services. ")
            break
    except ValueError:
        print("sorry you select Wrong option! Please choice a number.")
        continue
