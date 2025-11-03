import hashlib, random, json
from blockchain_program.data import transactions, timestamps

# track which hash to use 
hash_256 = True
hash_1 = False

def switch_hash():
    # let python know global variables
    global hash_256, hash_1 

    if hash_256 == True and hash_1 == False:
        hash_256 = False
        hash_1 = True
        algorithm = "SHA-1"  
    elif hash_256 == False and hash_1 == True:
        hash_256 = True
        hash_1 = False
        algorithm = "SHA-256" 


    print(f"Hash algorithm has been changed to {algorithm}.")
    print()

# create hash object, send in bytes, and return hex string
def encode(datastring):
    if hash_256 == True: 
        hash = hashlib.sha256()
        hash.update(datastring.encode('utf-8'))
        return hash.hexdigest()
    elif hash_1 == True: 
        hash = hashlib.sha1()
        hash.update(datastring.encode('utf-8'))
        return hash.hexdigest()

def show_blockchain():
    # create temporary previous hash 
    global hash_256, hash_1 
    if hash_256 == True and hash_1 == False:
        previous_hash = "0" * 64
    elif hash_256 == False and hash_1 == True: 
        previous_hash = "0" * 40

    # pair up timestamps and transactions with zip
    link = zip(timestamps, transactions)

    for index, (time, transfer_details) in enumerate(link):
        nonce = random.randint(1, 1000)     # create nonce value for each hash

        

        block_data = {
            "index": index,
            "timestamp": time,
            "sender": transfer_details['sender'],
            "receiver": transfer_details['receiver'],
            "amount": transfer_details['amount'],
            "previous hash": previous_hash,
            "nonce": nonce 
        }

        # create current block's hash using json.dumps to combine all data in a string 
        block_string = json.dumps(block_data)
        current_hash = encode(block_string)

        # display everything in block 
        print(f"-----Block {index}-----")
        print(f"Timestamp     : {time}")
        print("Transaction   :")
        print(f"  From        : {transfer_details['sender']}")
        print(f"  To          : {transfer_details['receiver']}")
        print(f"  Amount      : {transfer_details['amount']}")
        print(f"Hash          : {current_hash}")
        print(f"Previous Hash : {previous_hash}")
        print(f"Nonce         : {nonce}")
        print()

        # update previous hash for next iteration
        previous_hash = current_hash
