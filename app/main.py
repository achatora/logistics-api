from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.shipments import router as shipments_router

app = FastAPI(title="Logistics API")

app.include_router(health_router)
app.include_router(shipments_router)
