import random, json, requests 
from blockchain_program.data import transactions, timestamps

# ----------------------------------------
# Global settings 
# ----------------------------------------
current_algorithm = "sha256"
reward_url = "http://127.0.0.1:5000/reward" 
hash_url = "http://127.0.0.1:3000/hash"
serialize_url = "http://127.0.0.1:7000/serialize"

# ----------------------------------------
# Function to Swtich Hashes
# ----------------------------------------
def switch_hash():
    global current_algorithm

    if current_algorithm == "sha256":
        current_algorithm = "sha1"
    else:
        current_algorithm =="sha256"

    print(f"Hash algorithm switched to {current_algorithm}")

# ---------------------------------------- 
# Serialization Microservice
# ---------------------------------------- 
def serialize_service(data_dict):
    payload = {"data": data_dict}

    response = requests.post(serialize_url, json=payload)
    if response.status_code != 200:
        raise Exception(f"Serializer service error: {response.text}")
    
    return response.json()["serialized"]

# ---------------------------------------- 
# Call on the Hashing Microservice 
# ----------------------------------------
def go_hash(input_string):
    global current_algorithm
    
    payload = {
        "input": input_string,
        "hash": current_algorithm
    }

    response = requests.post(hash_url, json=payload)

    if response.status_code != 200:
        raise Exception(f"Go service error: {response.text}")

    hash = response.json()
    return hash["hash"]

def show_blockchain():
    global current_algorithm

    # Record previous hashes (temp)
    previous_hash = "0" * (64 if current_algorithm == "sha256" else 40)

    # pair up timestamps and transactions with zip
    link = zip(timestamps, transactions)

    for index, (time, transfer_details) in enumerate(link):
        nonce = random.randint(1, 1000)     # create nonce value for each hash

        response = requests.get(f"{reward_url}?block_index={index}")
        reward = response.json()

        block_data = {
            "index": index,
            "timestamp": time,
            "sender": transfer_details['sender'],
            "receiver": transfer_details['receiver'],
            "amount": transfer_details['amount'],
            "previous hash": previous_hash,
            "nonce": nonce,
            "reward": reward['reward']  
        }

        # create current block's hash using json.dumps to combine all data in a string 
        block_string = serialize_service(block_data)
        current_hash = go_hash(block_string)

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
        print(f"Miner Reward  : {reward['reward']}")
        print("====================================================================")
        print()

        # update previous hash for next iteration
        previous_hash = current_hash
