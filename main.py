from fastapi import FastAPI  
  
app = FastAPI() 
  
@app.get("/")  
def index():
    return {"message": "Hello World"} 

@app.get("/nombre")  
def nombre():
    return {"message": "joimar"} 