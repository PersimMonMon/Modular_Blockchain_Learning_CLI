from blockchain_program.home import show_home
from blockchain_program.transactions import add_transaction
from blockchain_program.help import show_commands
from blockchain_program.walkthrough import show_walkthrough
from blockchain_program.blockchain import show_blockchain

commands = {
  "add": add_transaction,
  "home": show_home,
  "help": show_commands,
  "walkthrough": show_walkthrough,
  "blockchain": show_blockchain
}

def main(): 
  print('\nWelcome to CLI_T-Chain')
  print('---------------------\n')
  print("This is a simulated blockchain with manueal overrides for\nlearning purposes. Understand blockchains from behind the scenes! \nTo get started enter 'help' to show a list of commands.\n")

  ## check what users enter 
  while True: 
    user_input = input(">").strip().lower() 

    if user_input == 'exit': 
      print("Goodbye!")
      break 

    elif user_input in commands: 
      commands[user_input]() 

    else: 
      print(f"Unknown command: {user_input}. Enter 'help' to see list of commands.")

  
if __name__ == "__main__":
  main()