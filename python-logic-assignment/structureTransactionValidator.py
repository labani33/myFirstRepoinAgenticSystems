account_balance=int(input("Please enter your balance: "))
withdrawal_amount=int(input("Please enter your withdrawal amount: "))
verified_User = input("Is user verified? (True/False): ").strip().lower() == "true"
if account_balance>=withdrawal_amount and verified_User:
    print("Withdrawal successful")
else:
    print("Transaction Denied")