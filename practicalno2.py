#practical no 2.
#Write a Python program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for withdraw and deposit) D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program: D 300
#D 300
#W 200
#D 100
#Then, the output should be: 500

total_ammount = 0
print("(deposit) d-ammount")
print("(withdraw) w-ammount")




while True:
    a = input()
    ops = a.split(" ")
    operation = ops[0]
    ammount = int(ops[1])

    if (operation == "d"):                         # aapan ji amount deu ti total amount madhe add hoil
        total_ammount= ammount+total_ammount

    if (operation == "w"):
        if(ammount > total_ammount):               # aaplyala jevde paise kadayche ahe tevde aaplya katyat nasle tar insufficient amount
            print("\ninsufffficient balance!!")
        else:
            total_ammount= total_ammount-ammount    # aapan jevde paise kadle tevde aaplya katyatun vaja hotil
    print("\nyour total amount is=",total_ammount)

    a= input("\npress y for continue:")
    if not(a=="y"):
        break

print("thank you sir for using our services you total balance is",total_ammount,"rs")
