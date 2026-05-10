from sqladmin import ModelView

from models.user import User
from models.resturant import Restaurant
from models.table import Table
from models.slot import Slot
from models.booking import Booking
from models.ticket import Ticket
from models.chat import ChatHistory
from models.agarnt_logs import AgentLog


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name, User.email, User.created_at]


class RestaurantAdmin(ModelView, model=Restaurant):
    column_list = [Restaurant.id, Restaurant.name, Restaurant.location]


class TableAdmin(ModelView, model=Table):
    column_list = [Table.id, Table.restaurant_id, Table.capacity]


class SlotAdmin(ModelView, model=Slot):
    column_list = [Slot.id, Slot.restaurant_id, Slot.table_id, Slot.date, Slot.time, Slot.is_available]


class BookingAdmin(ModelView, model=Booking):
    column_list = [Booking.id, Booking.user_id, Booking.restaurant_id, Booking.status]


class TicketAdmin(ModelView, model=Ticket):
    column_list = [Ticket.id, Ticket.user_id, Ticket.status]


class ChatHistoryAdmin(ModelView, model=ChatHistory):
    column_list = [ChatHistory.id, ChatHistory.ticket_id, ChatHistory.sender, ChatHistory.agent_step]


class AgentLogAdmin(ModelView, model=AgentLog):
    column_list = [AgentLog.id, AgentLog.ticket_id, AgentLog.step]