# 💬 Python Chat Application

This is a simple **multi-user chat application** built using **Python sockets and threading**. It allows users to connect to a chat server, join chat rooms, and exchange real-time messages. A basic **Tkinter GUI** makes the chat interface user-friendly.

---

## ⚙️ How It Works

- A Python server (`server.py`) runs and waits for client connections.
- Each user connects using either a terminal-based client or a GUI client (`client_gui.py`).
- Users can join different chat rooms using `/join roomname`.
- All users in the same room receive messages in real time.
- Commands like `/exit` let users leave the chat gracefully.

---

## 💻 Tech Stack

- **Python 3**
- **Socket Programming** – for real-time communication  
- **Threading** – to handle multiple clients concurrently  
- **Tkinter** – for building the GUI interface

---

## 📦 Files

- `server.py` – Main server script  
- `client.py` – Terminal-based chat client  
- `client_gui.py` – GUI chat client with Tkinter

---


