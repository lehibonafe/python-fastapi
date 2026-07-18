from fastapi import FastAPI, HTTPException

app = FastAPI()

items = []

@app.get("/")
def root():
    return "Hello, World!"

@app.get("/items")
def create_items(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    
    for item in items:
      if item_id < items:
	return item
