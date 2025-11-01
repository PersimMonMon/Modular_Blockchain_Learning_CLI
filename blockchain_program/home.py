from blockchain_program.data import transactions

def show_home(): 
  if not transactions:
    print("No transactions yet.\n")
    return 

  for transaction in transactions:
    sender = transaction["sender"]
    receiver = transaction["receiver"]
    amount = transaction["amount"] 
    print(f"{sender} sends {receiver} ${amount}")
  
  print()
