# 🗨️ Multi-Client Chat Server inside Terminal 💻

A lightweight, real-time multi-client chat server built using Python's `socket` and `threading` modules.

This project demonstrates how to design a basic TCP server that allows multiple clients to connect, communicate, and exchange messages simultaneously — all directly inside the terminal ⚡

Built for learning, experimenting, and understanding how real-time networking works under the hood 🌐

---

## 📌 Overview

This chat server:

- 🌐 Uses TCP socket programming  
- 👥 Supports multiple clients simultaneously  
- 🧵 Handles each client in a separate thread  
- 📡 Broadcasts messages to all connected users  
- 💬 Allows server-side message input  
- 🛑 Supports graceful shutdown using the `exit` command  

---

## ⚙️ How It Works

1️⃣ The server starts on port **5000**.  
2️⃣ Clients connect using TCP.  
3️⃣ Each client runs in a separate thread.  
4️⃣ When a client sends a message, it is broadcast to all other connected clients.  
5️⃣ The server admin can also send messages from the terminal.  
6️⃣ Typing `exit` stops the server safely.  

---

## 🖥️ Requirements

- 🐍 Python 3.x  
- 💻 Works on Windows, Linux, Android and macOS  

---

## 🚀 How to Run

1️⃣ Clone the repository:

git clone (your-repo-link)

2️⃣ Navigate into the project folder:

cd (project-folder)

3️⃣ Run the server:

python mchat.py

4️⃣ Connect from another terminal:

🐧 Linux:
nc (server-ip) 5000

🪟 Windows:
telnet (server-ip) 5000

---

## 🔧 Default Configuration

- 🌍 Host: All available network interfaces  
- 🔌 Port: 5000  

You can change the port inside `mchat.py` if needed.

---

## ✨ Features

- ⚡ Real-time messaging  
- 👥 Multi-client support  
- 🧵 Thread-based handling  
- 📢 Server broadcast capability  
- 🔄 Automatic client disconnection handling  

---

## ⚠️ Limitations

- 🔐 No authentication  
- 🚫 No encryption (not secure for public internet use)  
- 🗂️ No message history storage  
- 🖥️ Command-line only (no GUI)  

---

## 🚀 Possible Improvements

- 🔑 Add user authentication  
- 💬 Add private messaging  
- 🔒 Add SSL encryption  
- 📝 Add logging system  
- 🖼️ Build GUI client  
- ☁️ Deploy to cloud server  

---

## 📄 License

This project is for educational purposes 🎓
