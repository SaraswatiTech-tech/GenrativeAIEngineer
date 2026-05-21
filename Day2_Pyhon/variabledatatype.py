Account_HolderName = input("Enter Holder Name:")
Account_Number = int(input("Enter Account Number:"))
Account_Balance = float(input("Enter Account Balance:"))
is_Account_Active = False
deposit_amount = float(input("Enter Deposit Amount: "))

Account_Balance = Account_Balance + deposit_amount

print(Account_Balance)


if is_Account_Active:
    withdrawal_amount = float(input("Enter withdrawal Amount:"))

    if Account_Balance >= withdrawal_amount:
        Account_Balance = Account_Balance - withdrawal_amount
        print("Withdrawal successful. Updated Balance:", Account_Balance)
    else:
        print("Insufficient balance for withdrawal.")
else:
    print("Account is not active. Cannot perform withdrawal.")