dictionary={"AAPL":180, "TSLA":250, "MBS":400, "JESS":1000}
flag=True
invest=0
while flag is True:
    name=input("enter stock name ").upper()
    if(name in dictionary):
        quantity=int(input("enter quantity "))
        invest+=(dictionary[name]*quantity)
        q=input("to continue:y,to discontinue:n").lower()
        if(q=="y"):
            flag=True
        else:
            flag=False
    else:
        print("enter a valid stock name")
print(f"investment={invest}") 
with open("task2_stock_tracker/result.txt","w") as file:
    file.write(f"Total investment = {invest}")       
    