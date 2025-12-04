from fastapi import FastAPI 

app = FastAPI() 

@app.get("/reward")
def reward(block_index: int): 
    base_reward = 50 
    halving_interval = 2 
    halvings = block_index // halving_interval
    return {"reward": base_reward / (2 ** halvings)}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("miner_rewards:app", host="127.0.0.1", port=5000, reload=True)