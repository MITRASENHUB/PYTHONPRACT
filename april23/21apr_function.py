def calculate_simple_interest (principal, interst, time) :
    simple_interest=principal*interst*time/100
    return simple_interest        

accounts = {

}

#7% if P is < 20,000, 10% if P is >20000, < 50000, 12% if P > 50000
rate = [7, 10, 12]

while True:
    print("Please enter [done] to finish entering accounts")
    account_number = input("Enter account number:> ")
    if account_number == "[done]":
        break
    amount = input("Enter principal:> ")
    accounts[account_number] = amount
print(accounts)
while True:
    user_acc_nu = input("ENTER ACC NO TO KNOW THE INTEREST AMOUNT, exit to exit:> ")
    if user_acc_nu == "exit":
        break
    principle = int(accounts[user_acc_nu])
    if principle < 20000:
        interest_rate = rate[0]
    elif principle > 20000 and principle < 50000:
        interest_rate = rate[1]
    else:
        interest_rate = rate[2]
    SI = calculate_simple_interest(principle, interest_rate, 1)
    print("INTEREST RATE for acc ", user_acc_nu, " is ", SI)