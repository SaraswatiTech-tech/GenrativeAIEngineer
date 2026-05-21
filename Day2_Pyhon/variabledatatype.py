Account_HolderName = input("Enter Holder Name:")
Account_Number = int(input("Enter Account Number:"))
Account_Balance = float(input("Enter Account Balance:"))
is_Account_Active = True
deposit_amount = float(input("Enter Deposit Amount: "))
Account_Balance = Account_Balance + deposit_amount
print(Account_Balance)
