from fastapi import APIRouter

from app.api.schemas.shipment import (
    CreateShipmentRequest,
    ShipmentResponse,
)

router = APIRouter()


@router.post(
    "/shipments",
    response_model=ShipmentResponse,
)
def create_shipment(request: CreateShipmentRequest):
    shipment = request.convert_to_domain()

    return shipment
