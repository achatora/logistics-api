from fastapi import APIRouter

from app.api.schemas.shipment import CreateShipmentRequest

router = APIRouter()


@router.post("/shipments")
def create_shipment(request: CreateShipmentRequest):
    return {"message": "Shipment request received"}
