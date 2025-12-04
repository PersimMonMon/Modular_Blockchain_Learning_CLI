# CS361 SWE Final Project: Modular Blockchain Learn CLI   

This project is an **educational blockchain system** that runs entirely through a **command line interface (CLI)**, giving users an inside look of how blockchain technology fucntions.    

The program is designed and implemented using microservices architecture and demonstrates fundamental blockchain concepts: data integrity, cryptographic hashing, and microservices design.   

The project includes the following microservices that must be started up before main program: 

**Hashing Microservice**: Generates cryptographic hashes for block data.  
**Mining Reward Microservice**: Calculates block mining rewards.   
**Serialization Microservice**: Serializes blockchain data for storage and transport.  

# Project Structure  
```
Modular_Blockchain_Learning_CLI  
│  
├── main.py             # Main program that interacts with microservices  
├── microservices/        
│ ├── serialize.py      # Python FastAPI microservice for serialization  
│ ├── miner_rewards.py  # Python FastAPI microservice for miner rewards  
│ └── hashing.go        # Go microservice for hashing  
└── README.md
```

# What the Program Can Do:

Users can interact with the system to: 
- Add and edit transactions in the blockchain.
- View the full blockchain and transaction history.
- Follow a **step-by-step walkthrough** of block creation, validation, and linking.
- Observe how cryptographic hashes are generated for blocks and transactions.
- Switching between two hashing methods.
- Calculate mining rewards for blocks.
- Serialize and transport blockchain data across the microservices. 

# Starting the Microservices   
1. **Serialize microservice** (Python)  
Open a new terminal: Change directory to microservices and run the file with python serialize.py. This will create a FastAPI server on port 7000. 
```
cd microservices
python serialize.py
```
2. **Miner Rewards microservice** (Python)  
Open a new terminal: Change directory to microservices and run the file with python miner_rewards.py. This will create a FastAPI server on port 5000.
```
cd microservices
python miner_rewards.py
```
3. **Hashing microservice** (Go)  
Open a new terminal: Change directory to microservices and run the file with go run hashing.go. This will create a HTTP server on port 3000.
```
cd microservices
go run hashing.go
```

**Notes:**       

-Ensure ports 7000, 5000, and 3000 are free before starting the microservices.    
-Keep all microservice terminals open while running main.py.     
-Make sure fastapi, uvicorn, and pydantic are installed. 

**Overview:**  
1. Start serialize.py (terminal 1)   
2. Start miner_rewards.py (terminal 2)    
3. Start hashing.go (terminal 3)  
4. Run main.py (terminal 4)   

