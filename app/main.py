from fastapi import FastAPI
app = FastAPI(title="Blue-Bus Tracker", version="0.1.0")

@app.get("/")
def root():
    return{"message: ": "Hello from the Blue-Bus Tracker"}

@app.get("/buses/{route_id}")
def get_buses(route_id: int):
    return{"route_id": route_id, "next_bus_min": 4}

@app.get("/deez")
def deez():
    return{"message: ": "Deez Nutzzzz"}