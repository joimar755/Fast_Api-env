from fastapi import FastAPI  
  
app = FastAPI() 
  
@app.get("/")  
def index():
    return {"message": "Hello World"} 

@app.get("/nombre/{nombre}")  
def nombre(nombre: str):
    return {"message":"el nombre es:"+str(nombre)}  

