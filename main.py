from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Cake(BaseModel):
    id: int
    name: str
    comment: str
    imageUrl: str
    yumFactor: int

cakes = []

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Welcome to the Cake API"}

@app.get("/cakes", response_model=List[Cake], tags=["Cakes"])
def list_cakes():
    """
    Retrieve a list of all cakes.
    """
    return cakes

@app.post("/cakes", response_model=Cake, tags=["Cakes"])
def create_cake(cake: Cake):
    """
    Create a new cake.
    """
    cakes.append(cake)
    return cake

@app.delete("/cakes/{cake_id}", response_model=Cake, tags=["Cakes"])
def delete_cake(cake_id: int):
    """
    Delete a cake by ID.
    """
    for i, cake in enumerate(cakes):
        if cake.id == cake_id:
            deleted_cake = cakes.pop(i)
            return deleted_cake
    raise HTTPException(status_code=404, detail="Cake not found")

# Include OpenAPI documentation
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info", reload=True)
