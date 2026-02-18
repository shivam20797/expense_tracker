# Expense Tracker

print("Welcome to Expence Tracker")

expenceList = []

while True:
  print("\n====== Menu ========\n")
  print("1 Add Expense")
  print("2 View All Expense")
  print("3 View Total Spending")
  print("4 Exit")
  try : 
    choice = int(input("Enter choice (1-4): "))
    if choice == 1:
      date = input("Enter date (DD-MM-YYYY): ")
      expenceName = input("Enter expence name: ")
      desc = input("Enter description: ")
      amount = float(input("Enter amount: "))
      expenceList.append({
        'date' : date,
        'expenceName' : expenceName,
        'desc' : desc,
        'amount' : amount
      })
      print("\n Expence added successfully")
    elif choice == 2 :
      if(len(expenceList) == 0) : 
        print("\nNo data found!!")
      else:
        print("\nExpences List\n")
        index = 0
        for element in expenceList:
          print(f"{index} -> {element['date']}, {element['expenceName']}, {element['desc']}, {element['amount']}")  
          index+=1
    elif choice == 3 :
      totalSpend = 0
      for element in expenceList:
        totalSpend = totalSpend + element["amount"]
      print("\nTotal Spends = ",totalSpend)
    elif choice == 4 :
      print("\nThanks you")
      break
    else :
      print("\nInvalid choice!! Try Again !! ")
  except ValueError:
    print("Invalid input! Please enter number.")
    continue


  







