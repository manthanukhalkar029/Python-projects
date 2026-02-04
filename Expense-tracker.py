# Expense Tracker Project 

Expense_List = []
print('Welcome to Personal ExpenseTracker')

while True:
    print("===MENU===")
    print("1. ADD Expenses:")
    print("2. View all Expenses:")
    print("3. Total Spendings: ")
    print("4.--Exit--")
    Choice = int(input("Enter your Choice:"))
    print()

#ADD Expense
    if(Choice==1):
        print("ADD your Expense")
        Date = input("Enter date:")
        Category = input("Enter Category:")
        Description = input("Enter Des.:")
        Amount = float(input("Enter amount:"))
        Amount_type = input("Payment method?(Card,Cash,UPI):")

        each_expense={
            "date": Date,
            "category": Category,
            "description": Description,
            "amount": Amount,
            "type": Amount_type,
        }
        Expense_List.append(each_expense)
        print("Expense Added Successfully!!!")
        print()


#VIEW Expense:
    elif(Choice==2):
        if(len(Expense_List)==0):
                print("Please Add your Expenses!!!")
        else:   
            count =1
            print("---Your Expenses---") 
            for i in Expense_List:
                print(f'Expense No.{count} ->',i)
                count+=1
        print()


#Total Spending:
    elif(Choice==3):
        total =0
        for i in Expense_List:
            total+= i["amount"]
        print("Your total Spendings are of Rupees:",total)
        print()


#Exit
    elif(Choice==4):
        print("Thanks For Visiting!!!")
        break
        print()

    else:
        print("INVALID CHOICE.... TRY AGAIN!!")
