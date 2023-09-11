
# I want to test my knowledge of the OOP by building a simple bank app that shows the customers/account
# holder's details

class Bank:

    def __init__(self):
        self.bank = "Timi Plc"
        self.branch = "Magodo, Lagos"

    class Customer:

        def __init__(self):
            self.first_name = ""
            self.last_name = ""
            self.account_type = ""
            self.is_active = False
            self.balance = 600.00

        def OpenAccount(self):

            AccountType = {1: "Savings",
                           2: "Current",
                           3: "Fixed Deposit"
                           }
            self.first_name = input("First Name: ")
            self.last_name = input("Last Name: ")
            for i in AccountType:
                print(i, ">> ", AccountType[i])

            self.account_type = int(input("Select an account option: "))
            if self.account_type == 1:
                self.account_type = AccountType[1]
                pass
            elif self.account_type == 2:
                self.account_type = AccountType[2]
                pass
            elif self.account_type == 3:
                self.account_type = AccountType[3]
                pass
            else:
                self.account_type = input("Select an account option: ")

            print("Account Details: ")
            print("Account Type: ", self.account_type)
            print("Account Name: ", self.first_name)
            print("Account Balance: ", self.balance)
            print("Please deposit to make your account active!")

        def Deposit(self):
            deposit_amount = int(
                input("Enter the amount you want to deposit: "))
            self.balance = int(self.balance) + int(deposit_amount)
            self.is_active = True
            print("You have successfully deposited " +
                  "$" + str(deposit_amount) + ".")
            print("Now your new balance is: " + "$" + str(self.balance))
            if self.is_active == True:
                print("ACCOUNT ACTIVE!")

        def Withdraw(self):
            withdrawal_amount = int(
                input("Enter the amount you want to withdraw: "))
            self.balance = int(self.balance) - int(withdrawal_amount)
            print("$" + str(withdrawal_amount) +
                  " has been successfully withdrawn from your balance.")
            print("Now your new balance is: " + "$" + str(self.balance))


customer1 = Bank()
customer1 = customer1.Customer()


customer1.Withdraw()
print(customer1.last_name)
