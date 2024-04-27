from fastapi import APIRouter, Query
from services.json_service import get_bus_gps
from utilities.deps import pattern
from utilities.exceptions import handle_exceptions

router = APIRouter()

@router.get("/bus_gps")
async def bus_gps_route(
        route_id: str = Query(..., description="Route ID as a string", regex=pattern),
        stId: str = Query(..., description="Station ID as a string", regex=pattern)
):
    try:
        result = await get_bus_gps(route_id, stId)
        return result
    except Exception as e:
        raise handle_exceptions(e)
