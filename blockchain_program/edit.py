from blockchain_program.data import transactions

def show_edit():

    # determine which block to edit
    print("\nBlockchain starts from zero to five. Please enter a nubmer from zero to five only.\n")
    edit_block = input("Which block would you like to edit? ")

    # display to user existing transaction and get new values
    for index, value in enumerate(transactions):
        if index == int(edit_block):            # match int to int 
            print()
            print(f"Editing Block {index}")
            print(f"Current From      : {value["sender"]}")
            print(f"Current To        : {value["receiver"]}")
            print(f"Current Amount    : {value["amount"]}")
            print()

            new_from = input("New From          : ")
            new_to = input("New To            : ")
            new_amount = input("New Amount        : ")
            print()

            # change database list to match new transaction
            value["sender"] = new_from
            value["receiver"] = new_to
            value["amount"] = new_amount