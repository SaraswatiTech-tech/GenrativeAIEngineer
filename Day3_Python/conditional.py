Account = True
Balance = 6000

if Account == True:
    print("Enter withdrawal amount:")
    withdrawal_amount = float(input())

    if Balance >= withdrawal_amount:
        Balance = Balance - withdrawal_amount
        print("Withdrawal Successful")
        print("Remaining Balance:", Balance)
    else:
        print("Insufficient balance.")