from services.booking_services import create_booking
from services.availability_service import get_available_slots


TOOLS = {
    "check_availability": get_available_slots,
    "create_booking": create_booking
}