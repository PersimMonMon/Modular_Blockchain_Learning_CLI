from blockchain_program.data import transactions, timestamps

import time





def add_transaction(): 
  print()
  print("Enter transaction details:")
  sender = input("From     : ")
  receiver = input("To       : ")
  amount = input("Amount   : $")
  confirmation = input("Confirm? (yes/no) ")

  if confirmation == "yes":
    print("Transaction has been added to a block.\n")
    transaction = {
      "sender": sender,
      "receiver": receiver,
      "amount": amount
    }
    transactions.append(transaction)    # add dictionary into list 
    
    # record time
    current_time = time.time()
    string_time = str(current_time)
    timestamps.append(string_time)      # add time in strings into list 
    
  elif confirmation == "no":
    print("Transaction has not been recorded.\n")
  else:
    print("Transaction voided due to unknown entered value. Please enter 'yes' or 'no' next time.\n")

