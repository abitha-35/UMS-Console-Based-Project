print("*********************************")
print("Welcome to ATM")
print("*********************************")
print()
accounts = {
    1110 : ["Abitha","05-03-2002",10000,3585],
    1111 : ["Nithisha","14-09-2002",20000,1489],
    1112 : ["Gouthami","31-05-2002",25000,1234],
    1113 : ["Rishitha","01-01-2002",30000,None],
    1114 : ["pavan","05-10-2001",40000,1485],
    }

dobm = {1:"January",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
while True:
    print("Choose Your Option")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini Statement")
    print("5. Balance Inquiry")
    print("6. Exit")
    option = int(input("Enter Your Option: "))
    print()
    if option == 1:
        print("*********************************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does Not Exist !")
        else:
            pin = int(input("Enter Pin: "))
            if accounts[accno][-1] == None:
                print("Generate Pin")
            else:
                if accounts[accno][-1] != pin:
                    print("Invalid Pin")
                else:
                    amt = int(input("Enter Amount to Withdraw: "))
                    if amt > accounts[accno][-2]:
                        print("Insufficient Funds")
                    else:
                        print("Withdraw Successful !")
                        accounts[accno][-2] -= amt
        print("*********************************")
    elif option == 2:
         print("*********************************")
         accno = int(input("Enter Account Number: "))
         if accno not in accounts:
            print("Account does not Exist")
         else:
            amt = int(input("Enter Amount to Deposite: "))
            accounts[accno][-2] += amt
            print("Deposit Successful")
         print("*********************************")
    elif option == 3:
         print("*********************************")
         accno = int(input("Enter Account Number"))
         if accno not in accounts:
             print("Account does not Exist")
         else:
             if accounts[accno][-1] == None:
                 pin = int(input("Enter Pin: "))
                 cpin = int(input("Confirm Pin: "))
                 if pin != cpin:
                     print("Pin does not Match")
                 else:
                     accounts[accno][-1] = pin
                     print("Pin Generated Successfully")
             else:
                 print("Pin Already Exist")
         print("*********************************")
    elif option == 4:
         print("*********************************")
         accno = int(input("Enter Account Number: "))
         if accno not in accounts:
            print("Account does not Exist")
         else:
             pin = int(input("Enter pin: "))
             if pin != accounts[accno][-1]:
                 print("Invalid Pin")
             else:
                 print(f"Name: {accounts[accno][0]}")
                 print(f"Account Number: {accno}")
                 dob = accounts[accno][1].split("-")
                 date = dob[0]
                 month = dobm[int(dob[1])]
                 year = dob[2]
                 dob = date + "-" + month + "-" + year
                 print(f"Date of Birth: {dob}")
                 print(f"Account Balance: {accounts[accno][-2]}")
         print("*********************************")
    elif option == 5:
         print("*********************************")
         accno = int(input("Enter Account Number: "))
         if accno not in accounts:
            print("Account does not Exist")
         else:
             pin = int(input("Enter pin: "))
             if pin != accounts[accno][-1]:
                 print("Invalid Pin")
             else:
                 print(f" Your current balance is: {accounts[accno][-2]}")
         print("*********************************")
    else:
        break


                 
