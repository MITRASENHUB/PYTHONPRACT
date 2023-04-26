
def calculate_Simple_interest(principal,interest,time):
    SI=(principal*time*interest/100)
    return SI

#Take multiple accounts as inputs

account={



}

rate=[10,20,30,40,50]

#First account number must be entered and then the principle must be entered
while True :
    print("please stop entering accounts once written [done]")
    ac_no=input("please enter the account number :  ")
    if ac_no=="[done]":
        break
    ammount=int(input("please enter principal"))
    account[ac_no]=ammount
    print(account)
while True : 
    user_ac_no=input("enter ac no to know the interest amount, exit to exit:> ")
    if user_ac_no=="exit":
        break
    principle=int(account[user_ac_no])
    interest_rate = 5
    k=1000
    if principle <= 50000 :
        interest_rate = rate [0]
    elif principle < 60000 and principle>50000:
        interest_rate = rate [1]
    elif principle < 70000 and principle > 60*k:
        interest_rate = rate [2]
    elif principle < 80000 and principle > 70*k:
        interest_rate = rate [3]    
    elif principle < 90000 and principle > 80*k:
        interest_rate = rate [4]
    SI=calculate_Simple_interest(principle,interest_rate,1)
    print("Interest rate for acc", user_ac_no, " is ", SI)            



#Take the user input as account number
#Get the principle of the account number

#calculate interesent


#show
