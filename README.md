# 🍽️ AI Restaurant Booking Agent

An AI-powered restaurant reservation assistant built using FastAPI and LangGraph.  
The system automates restaurant table booking workflows through conversational AI and intelligent tool-calling.

---

## 🚀 Features

- AI-powered restaurant booking assistant
- Slot availability checking
- Automated reservation workflow
- Conversational booking experience
- Tool-calling using LangGraph
- FastAPI backend APIs
- Database integration for reservation management
- Modular and scalable architecture

---

## 🛠️ Tech Stack

- Python
- FastAPI
- LangGraph
- SQLAlchemy
- SQLite
- OpenAI API

---



## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/Raju995/restaurant-booking-agent.git
cd restaurant-booking-agent
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=sqlite:///./restaurant.db
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Server will start at:

```plaintext
http://127.0.0.1:8000
```

---

## 📌 API Documentation

Swagger UI:

```plaintext
http://127.0.0.1:8000/docs
```

---

## 🧠 How It Works

1. User requests a restaurant reservation
2. AI agent processes the request
3. System checks slot availability
4. Reservation details are validated
5. Booking confirmation is generated

---

## 🔮 Future Improvements

- WhatsApp integration
- Voice-enabled reservations
- Multi-agent workflow
- Admin dashboard
- Email/SMS notifications
- PostgreSQL support

---



## 👨‍💻 Author

Raju Chatterjee

- GitHub: https://github.com/Raju995

---

