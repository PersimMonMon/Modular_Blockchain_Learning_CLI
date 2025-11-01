import blockchain_program.data as data 

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
    data.transactions.append(transaction)
  elif confirmation == "no":
    print("Transaction has not been recorded.\n")
  else:
    print("Transaction voided due to unknown entered value. Please enter 'yes' or 'no' next time.\n")

