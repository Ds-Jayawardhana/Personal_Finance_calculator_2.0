'''
Date:-12/04/2024
Name:Disandu Sanhida
IIT Student ID:-20230469
Westminster Student Id:-2083055
'''

#Importing the JSON module for handling data
import json

# Global dictionary to store transactions
transactions = {}

# Function to load transactions from JSON file (improved error handling)
def load_transactions(file_path="data.json"):
   global transactions
   #calling the gloabal transactions list
   file_path = "data.json"
    #error handling ifthere isn't exsist a file in the directory
   try:
        #Attempting to open the JSON file and load its contents into the 
        with open(file_path, "r") as json_file:
            transactions = json.load(json_file)
   except FileNotFoundError:
        print("File not found. Creating a new file...")
        transactions = {}
        return#if file not found,initalize transactions
    #Decode json file if there isn't any data in the file when programme intilizly start
   except json.decoder.JSONDecodeError:
        print()
        transactions = {}#if the file not found initalize transactions list as empty
        return
# Function to save transactions to JSON file
def save_transactions():
    global transactions# Accessing the global 'transactions' Variable
    ans = input("Do You Want To Save Changes(yes/no): ").lower()
    #Asking user to confirm the changes
    if ans == "yes":
    #if User enters yes    
        file_path = "data.json"
        with open(file_path, "w") as json_file:
            json.dump(transactions, json_file,indent=2)
            #Save user entered data to JSON File
        print("Changes Saved Successfully...")
    elif ans == "no":
        print("Changes are not stored ")
    else:
        print("Incorrect Input please enter Yes/No")

# Function defined to read bulk of transactions from a exsisiting file
def read_bulk_transactions_from_file(bulk_file_name):
    global transactions
    #Calling the global transactions
    with open(bulk_file_name, 'r') as file:
        current_transaction = {}
        for line in file:
            #Split the line in the file into 2 parts by :
            parts = line.strip().split(":")
            if parts[0] == "Transaction":
                current_transaction = {}
                #Defining a new dictionary if part 1 of the line is transaction
            elif parts[0] == "Purpose":
                current_transaction["Purpose"] = parts[1].strip().lower()
            elif parts[0] == "Amount":
                current_transaction["Amount"] = parts[1].strip()
            elif parts[0] == "Date":
                current_transaction["Date"] = parts[1].strip()
            elif parts[0] == "Type":
                current_transaction["Type"] = parts[1].strip().lower()
                transactions.setdefault(current_transaction["Purpose"], []).append({
                    "amount": current_transaction["Amount"],
                    "type": current_transaction["Type"],
                    "date": current_transaction["Date"]
                })                   
    save_transactions()            
    return transactions

# Function to add a transaction (assuming 'transactions' is a dictionary)
def add_transaction():
    global transactions
    load_transactions()
    print("---------------------Add Transactions------------------------")
    #Asking user to input the purpose
    purpose = input("Enter the transaction purpose: ").lower()
    #Check whether the user inputed purpose exsist in the transactions
    if purpose in transactions:
        print("This transaction already exists. Do you want to add details to it?")
        pur_ans = input("Enter Yes or No: ").strip().lower()
        #converting user inputed answer into the lower case
        if pur_ans == "yes":
            #Using Error handling to handle the Valueerror if user input strings for the amount
            try:
                amount = float(input("Enter the Amount: Rs."))
                if amount <= 0:
                  print("Amount cannot be negative.")
                  return   
            except ValueError:
                print("Please Enter a Amount in Integers.")
                return
            #Check the user entered amount is less than 0 or equals to zero    
            #Asking user what is the type of transaction    
            trs_type = str(input("Enter the Transaction Type (Income/Expense): ")).strip().lower()
            #Check whether the user input Income, expense word correctly
            if trs_type not in ("income", "expense"):
                print("Invalid type. Please enter 'Income' or 'Expense'.")
                #if user input wrong it return s to enter it again
                return
            date = input("Enter the Date in Format DD/MM/YY: ")
            #Appending user inputed data into a dictionary with keys
            transactions[purpose].append({"amount": amount, "type": trs_type, "date": date})
  
        elif pur_ans == "no":
            return
            '''
            try:
                amount = float(input("Enter the Amount: Rs."))
            except ValueError:
                print("Please Enter Only Integers")
                return
            if amount < 0:
                print("Amount cannot be negative.")
                return
            trs_type = input("Enter the Transaction Type (Income/Expense): ").strip().lower()
            if trs_type not in ("income", "expense"):
                print("Invalid type. Please enter 'Income' or 'Expense'.")
                return
            date = input("Enter the Date in Format DD/MM/YY: ")
            transactions[purpose] = [{"amount": amount, "type": trs_type, "date": date}]
            '''
        else:
            print("Please Enter only (Yes/No)")
    else:
        try:
          amount = int(input("Enter the Amount: Rs."))
          if amount <= 0:
            print("Amount cannot be negative.")
            return
        except ValueError:
          print("Enter Only Integers for the Amount")
          return
        #Check the user entered amount is less than 0 or equals to zero    
        trs_type = input("Enter the Transaction Type (Income/Expense): ").strip().lower()
        if trs_type not in ("income", "expense"):
            print("Invalid type. Please enter 'Income' or 'Expense'.")
            return
        date = input("Enter the Date in Format DD/MM/YY: ")
        transactions[purpose] = [{"amount": amount, "type": trs_type, "date": date}]

    save_transactions()


#Function Defined to View saved transaction in JSON File
def view_transactions():
    global transactions
    print("------------------------------View Transactions---------------------------------")
    load_transactions()  # Load transactions before viewing
    # Check if there are any transactions existing
    if not transactions:
        print("Sorry, there aren't any transactions.")
        return
    else:
        # Iterate through transactions list
        for purpose, details in transactions.items():
            print(f"Transaction Purpose: {purpose}")
            #Iterates through transactions under the 
            for transaction in details:
                print(f"Amount: Rs. {transaction['amount']}, Type: {transaction['type']}, Date: {transaction['date']}")
            print()

#Defining Function for Updating Transactions                                                    
def update_transaction():
    load_transactions()
    view_transactions()
    #Asking user what purpose want to update
    trans_purpose_update = input("Enter the Transaction Purpose Which you want to Update: ")
    #Check whether the user entered purpose is in transactions
    if trans_purpose_update not in transactions:
        print("Enter an Existing Transaction Purpose to Update.")
        return
    else:
        transactions_under_purpose = transactions[trans_purpose_update]
        num_transactions = len(transactions_under_purpose)
        print(f"There are {num_transactions} transactions under {trans_purpose_update}.")
        try:
            trans_number_updt = int(input(f"Enter the transaction number to update (1 to {num_transactions}): "))
        except ValueError:
            print("Enter the Transaction Number Only In Integers")
            return
        if trans_number_updt <= 0 or trans_number_updt > len(transactions_under_purpose):
            print(f"Please enter a number between 1 and {num_transactions}.")
            return
        else:
            trans_number_updt -= 1
            trans_data = transactions_under_purpose[trans_number_updt]
            print("----------------------------------------------------------------")
            print("Current Transaction Details:")
            print(f"Amount: Rs. {trans_data['amount']}, Type: {trans_data['type']}, Date: {trans_data['date']}")
            print("----------------------------------------------------------------")
            trans_value_updt = input("Enter the field to update (amount, type, or date): ").lower()
            if trans_value_updt == "amount":
                try:
                    new_amount = float(input("Enter the new amount: Rs. "))
                except ValueError:
                    print("Enter Integers Only")
                    return
                transactions_under_purpose[trans_number_updt]["amount"] = new_amount
            elif trans_value_updt == "type":
                new_type = input("Enter the new transaction type (income/expense): ").strip().lower()
                if new_type not in ("income", "expense"):
                    print("Invalid type. Please enter 'income' or 'expense'.")
                    return
                #Updating Type to user Inputr=ed New type
                transactions_under_purpose[trans_number_updt]["type"] = new_type
            elif trans_value_updt == "date":
                #Updating Date into new transaction date
                new_date = input("Enter the new date in format DD/MM/YY: ")
                transactions_under_purpose[trans_number_updt]["date"] = new_date
            else:
                print("Invalid field. Please enter 'amount', 'type', or 'date'.")
                return
    save_transactions()

def delete_transaction():
    delete_answer = 0
    # call the function view transaction to view the list of transactions existing
    view_transactions()
    # assign the value None to the num variable
    
    print("------------------------------ Delete Transactions-------------------------------")
    if not transactions:
        return
    print("If you want to Delete All transactions under one purpose?")
    print("Enter yes If you want to delete All Transactions In a Purpose")
    print("Enter No to delete one transaction under a purpose")
    delete_answer = input("Enter Yes Or No: ").lower()
    if delete_answer == "yes":
        delete_purpose = input("Enter the transaction Purpose You want to delete: ").lower()
        if delete_purpose not in transactions:
            print("There is Not Such Purpose In Transactions List")
        else:
            del transactions[delete_purpose]
            print(f"Transactions under {delete_purpose} deleted Successfully...")
            save_transactions()
    elif delete_answer == "no":
        delete_purpose = input("Enter the transaction Purpose You want to delete: ").lower()
        if delete_purpose not in transactions:
            print("There is Not Such Purpose In Transactions List")
        else:
            transactions_under_purpose = transactions[delete_purpose]
            num_transactions = len(transactions_under_purpose)
            try:    
                dlt_trans_num = int(input(f"Enter the Transaction Number to Delete between 1 to {num_transactions}: "))
                dlt_trans_num -= 1
            except ValueError:
                print("Enter Transaction Number Only in integers")   
                return 
                
                if dlt_trans_num <= 0 or dlt_trans_num > len(transactions_under_purpose):
                   print(f"Please enter a number between 1 and {num_transactions+1}.") 
            
            del transactions[delete_purpose][dlt_trans_num]
            print(f"Transaction In purpose {delete_purpose} deleted Successfully")
            if transactions[delete_purpose]==[]:
               del transactions[delete_purpose]
               save_transactions()
            else:    
               save_transactions()
    else:
        print("Please Enter only (Yes/No)")

def display_summary():
    global transactions
    print("------------------------------ Display Summary -------------------------------")
    # Initializing total_incomes
    total_incomes = 0
    # Initializing total_expenses
    total_expenses = 0
    # Initializing count_E
    count_E = 0
    # Initializing count_I
    count_I = 0
    # Check if there are any transactions in the transactions list
    if not transactions:
        print("There aren't any transactions to display Summary.")
    else:
        for purpose, details in transactions.items():
            for transaction in details:
                amount = float(transaction["amount"])
                if transaction["type"] == "income":
                    count_I += 1
                    total_incomes += amount  
                elif transaction["type"] == "expense":
                    count_E += 1
                    total_expenses += amount  
        print(f"The total Amount of Incomes are:- {total_incomes}")   
        print(f"The Total Amount of Expenses Are:-{total_expenses}")           
        print(f"Number of Incomes Are:- {count_I}")  
        print(f"Number of Expenses Are:- {count_E}")    
        print(f"Net Value is:{total_incomes-total_expenses}")


def main_menu():
    #call function to load transactions
    load_transactions()

    while True:
        #print main menu header
        print("\n-----------------------Personal Finance Tracker---------------------------") 
        #disaplay add transaction as option 01
        print("(1) Add Transaction")
        #disaplay view transaction as 2
        print("(2) View Transactions")
        #display update transactioon as 3
        print("(3) Update Transaction")
        #disaplay delete transaction as option 4
        print("(4) Delete Transaction")
        #display display summary as option 5
        print("(5) Display Summary")
        #display exit as option 6
        print("(6) Read Bulk Transactions from File")
        #display exit as option 6
        print("(7) Exit\n")
        #prompt user to enter the choice
        choice = input("Enter your choice: ")
      

        #call the add transaction function if user enters one
        if choice == '1':
            add_transaction()
        #call the view transaction function if user enters one    
        elif choice == '2':
            view_transactions()
        #call the update transaction function if user enters one
        elif choice == '3':
            update_transaction()
        #call the delete transaction function if user enters one    
        elif choice == '4':
            delete_transaction()
        #call the display function if user enters one    
        elif choice == '5':
            display_summary()
        elif choice == '6':
            try:
               bulk_file_name=input("Enter a File name to Read Transactions in Bulk:-")
               read_bulk_transactions_from_file(bulk_file_name)
            except FileNotFoundError:
                print("File Not Found Please enter a Exsisting File")
                
            


        #if user enters 7 exit from the program   
        elif choice == '7':
            save_transactions()
            print("Data Saved...")
            print("Exiting program...")
           
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()