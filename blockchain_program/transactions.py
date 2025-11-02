from blockchain_program.data import transactions, timestamps

import time





def add_transaction(): 
  print()
  print("Enter transaction details:")
  sender = input("From     : ")
  receiver = input("To       : ")
  amount = input("Amount   : $")
  print("")
  print("Please review your data carefully before submitting.")
  print("Enter 'yes' to confirm and submit your transaction to the blockchain, or 'no' to cancel it.")
  print("Any other response will also cancel the transaction from being added to the blockchain.")
  print("You can edit your transaction later if needed, but doing so may take additional time.\n")
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

