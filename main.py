from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

katalog = [
    {"id": 1, "nama": "Laptop", "harga": 15000000, "stok": 10},
    {"id": 2, "nama": "Mouse", "harga": 150000, "stok": 50},
    {"id": 3, "nama": "Keyboard", "harga": 350000, "stok": 30},
    {"id": 4, "nama": "Monitor", "harga": 2500000, "stok": 15},
]


@app.get("/")
def root():
    return {"message": "Katalog Barang API"}


@app.get("/barang")
def semua_barang():
    return {"data": katalog}


@app.get("/barang/{barang_id}")
def barang_by_id(barang_id: int):
    for item in katalog:
        if item["id"] == barang_id:
            return item
    return {"error": "Barang tidak ditemukan"}
