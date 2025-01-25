from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Povolení CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Povolit všechny originy. Změň na specifické originy podle potřeby.
    allow_credentials=True,
    allow_methods=["*"],  # Povolit všechny HTTP metody
    allow_headers=["*"],  # Povolit všechny HTTP hlavičky
)

zvirata = ["bluey", "puma", "panda", "hyena"]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/zvirata")
def read_zvirata():
    return {"zvirata": zvirata }

@app.get("/zvire/{item_id}")
def read_item(item_id: int):
    return {"zvire": zvirata[item_id]}

@app.put("/zvire/{name}")
def create_item(name: str):
    zvirata.append(name)
    return {"zvire": name}
