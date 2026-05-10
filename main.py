from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin, ModelView
from core.database import engine
from sqladmin import Admin
from core.database import engine

from admin.views import (
    UserAdmin,
    RestaurantAdmin,
    TableAdmin,
    SlotAdmin,
    BookingAdmin,
    TicketAdmin,
    ChatHistoryAdmin,
    AgentLogAdmin
)
from models.user import User
from models.resturant import Restaurant
from models.table import Table
from models.slot import Slot
from models.booking import Booking
from models.ticket import Ticket
from models.chat import ChatHistory
from models.agarnt_logs import AgentLog
from api.chat import router as chat_router
# from app.api.v1.booking import router as booking_router  # future use

# from app.core.config import settings
# from app.core.database import init_db

import logging


def create_app() -> FastAPI:
    app = FastAPI(
        title="Restaurant Agent API",
        description="Agentic AI based restaurant booking system",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    admin = Admin(app, engine)

    admin.add_view(UserAdmin)
    admin.add_view(RestaurantAdmin)
    admin.add_view(TableAdmin)
    admin.add_view(SlotAdmin)
    admin.add_view(BookingAdmin)
    admin.add_view(TicketAdmin)
    admin.add_view(ChatHistoryAdmin)
    admin.add_view(AgentLogAdmin)

    # -----------------------------
    # CORS (important for frontend)
    # -----------------------------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # change in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # -----------------------------
    # Routers
    # -----------------------------
    app.include_router(chat_router, prefix="/chat", tags=["Chat"])
    # app.include_router(booking_router, prefix="/api/v1/booking", tags=["Booking"])

    # -----------------------------
    # Startup Event
    # -----------------------------
    # @app.on_event("startup")
    # async def startup_event():
    #     logging.info("Starting Restaurant Agent API...")
    #     init_db()

    # -----------------------------
    # Shutdown Event
    # -----------------------------
    @app.on_event("shutdown")
    async def shutdown_event():
        logging.info("Shutting down Restaurant Agent API...")

    return app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=False)
app = create_app()