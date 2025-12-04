# CS361 SWE Final Project: Modular Blockchain Learn CLI   

This project is a multi-microservice application with Python FastAPI services and a Go service. You must start all microservices BEFORE running the main program. 

# Project Structure  
```
Modular_Blockchain_Learning_CLI  
│  
├── main.py             # Main program that interacts with microservices  
├── microservices/      # Folder containing all microservices  
│ ├── serialize.py      # Python FastAPI microservice for serialization  
│ ├── miner_rewards.py  # Python FastAPI microservice for miner rewards  
│ └── hashing.go        # Go microservice for hashing  
└── README.md
```

# Starting the Microservices   
1. Serialize microservice (Python)  
Open a new terminal: Change directory to microservices and run the file with python serialize.py. This will create a FastAPI server on port 7000. 
```
cd microservices
python serialize.py
```
2. Miner Rewards microservice (Python)  
Open a new terminal: Change directory to microservices and run the file with python miner_rewards.py. This will create a FastAPI server on port 5000.
```
cd microservices
python miner_rewards.py
```
3. Hashing microservice (Go)  
Open a new terminal: Change directory to microservices and run the file with go run hashing.go. This will create a HTTP server on port 3000.
```
cd microservices
go run hashing.go
```

# Notes:       

-Ensure ports 7000, 5000, and 3000 are free before starting the microservices.    
-Keep all microservice terminals open while running main.py.     
-Make sure fastapi, uvicorn, and pydantic are installed. 

Overview:  
1. Start serialize.py (terminal 1)   
2. Start miner_rewards.py (terminal 2)    
3. Start hashing.go (terminal 3)  
4. Run main.py (terminal 4)   
