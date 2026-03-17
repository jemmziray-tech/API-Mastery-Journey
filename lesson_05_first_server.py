from fastapi import FastAPI  # 1. Bring in the construction materials

app = FastAPI()  # 2. Build the actual shop!


# 3. Put a sign on the front door ("/" means the main entrance)
@app.get("/")
def welcome_desk():  # 4. Hire a worker for the front desk
    # 5. Hand the customer their data (a dictionary!)
    return {"message": "Hello World! My very first API is alive!"}
