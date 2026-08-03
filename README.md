# 🤖 ChatGPT-Style AI Chatbot

A full-stack, production-ready AI Chatbot application built with Python Flask, SQLite, and Vanilla HTML/CSS/JavaScript with a premium glassmorphism UI.

![Glassmorphism Design](https://img.shields.io/badge/Design-Glassmorphism-7c5cfc)
![Flask Backend](https://img.shields.io/badge/Backend-Python%20Flask-blue)
![SQLite Storage](https://img.shields.io/badge/Database-SQLite-green)
![OpenAI Integration](https://img.shields.io/badge/AI-OpenAI%20API-10b981)

---

## ✨ Key Features

### 🎨 Frontend & Design
- **Glassmorphism UI**: Modern aesthetic with `backdrop-filter`, sleek gradients, and subtle glow effects.
- **Dark & Light Modes**: Seamless theme switching with system preference detection and state persistence.
- **Responsive Layout**: Mobile-first design with a collapsible sidebar and mobile overlay.
- **Smooth Animations**: Fade-in messages, pulse typing dots, skeleton loaders, floating icons.

### 💬 Chat & AI Engine
- **Server-Sent Events (SSE) Streaming**: Token-by-token real-time streaming response delivery.
- **Conversation Memory**: Remembers context across messages in a session.
- **Multimodal Support**: Upload image files (PNG, JPG, GIF, WebP) or drag-and-drop directly into the chat.
- **Markdown & Syntax Highlighting**: Full GFM rendering with Highlight.js code blocks and one-click copy buttons.
- **Voice Input**: Web Speech Recognition API integration for voice-to-text.
- **Text-to-Speech (TTS)**: Read AI responses aloud using the browser's SpeechSynthesis engine.
- **Emoji Picker**: Custom grid picker with search filter.

### 📁 History & Management
- **Multiple Conversations**: Unlimited chats with automatic titling based on initial messages.
- **Pin & Favorite**: Keep important chats pinned to the top or marked as favorite.
- **Search History**: Real-time filtering of past conversations by title or message content.
- **Rename & Delete**: Rename chats inline or remove unwanted conversations.
- **Export Options**: Download chats as PDF, formatted TXT, or raw JSON.
- **Import Support**: Restore exported JSON conversations seamlessly.

### ⚙️ Customization & Control
- **Model Selection**: Switch between GPT-4o, GPT-4o Mini, GPT-4 Turbo, GPT-4, o3-mini, and more.
- **Adjustable Parameters**: Live sliders for Temperature (Creativity) and Max Tokens limit.
- **Custom System Prompt**: Define custom persona and behavior rules for the assistant.
- **Keyboard Shortcuts**: Comprehensive keyboard shortcuts for supercharged productivity.

### 🔒 Security & Performance
- **Hidden API Keys**: OpenAI API key is stored strictly in `.env` server-side and never exposed to the client.
- **Rate Limiting**: Sliding window rate limiting on API endpoints to prevent abuse.
- **Input Validation**: Sanitization and length checks on messages and file uploads.
- **WAL Mode SQLite**: Fast concurrent reads and writes with automatic schema initialization.

---

## 📁 Project Structure

```
chatbot/
│
├── app.py                     # Flask application entry point
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API Key)
├── .gitignore                 # Git ignore patterns
├── README.md                  # Documentation
├── database.db                # SQLite database (auto-generated)
│
├── templates/
│   └── index.html             # Single Page Application HTML shell
│
├── static/
│   ├── style.css              # Glassmorphism design system & styles
│   └── script.js              # Full frontend SPA logic & streaming client
│
├── routes/
│   ├── __init__.py
│   ├── chat.py                # Streaming chat, uploads, history API endpoints
│   └── settings.py            # System configuration endpoints
│
├── database/
│   ├── __init__.py
│   └── models.py              # SQLite schema & CRUD helper functions
│
├── utils/
│   ├── __init__.py
│   └── helpers.py             # Validation, rate limiting, export utilities
│
└── uploads/                   # Stored user upload images
```

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.9+** installed on your system.
- An **OpenAI API Key** from [platform.openai.com](https://platform.openai.com/).

### 2. Installation

Clone or open the project folder:
```bash
cd d:/downloads/chatbot
```

Install the required Python dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration

Open the `.env` file in the root directory and insert your OpenAI API key:
```env
OPENAI_API_KEY=sk-proj-your-actual-api-key-here
```

### 4. Running the Application

Launch the Flask server:
```bash
python app.py
```

Open your browser and navigate to:
👉 **[http://localhost:5000](http://localhost:5000)**

---

## ⌨️ Keyboard Shortcuts Reference

| Shortcut | Action |
|----------|--------|
| `Ctrl` + `N` | Start a new chat |
| `Ctrl` + `Shift` + `S` | Toggle sidebar collapse |
| `Ctrl` + `K` | Focus search bar |
| `Ctrl` + `L` | Focus message input |
| `Enter` | Send message |
| `Shift` + `Enter` | Insert new line |
| `Ctrl` + `Shift` + `T` | Toggle Dark / Light theme |
| `Ctrl` + `/` | Show Keyboard Shortcuts modal |
| `Esc` | Close open modals / pickers |

---

## 📡 API Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/chat` | Send message & receive SSE response stream |
| `GET` | `/api/conversations` | List all conversations (supports `?search=`) |
| `POST` | `/api/conversations` | Create new conversation |
| `GET` | `/api/conversations/<id>` | Get conversation details and messages |
| `DELETE` | `/api/conversations/<id>` | Delete conversation |
| `POST` | `/api/conversations/<id>/rename` | Rename conversation title |
| `POST` | `/api/conversations/<id>/favorite` | Toggle favorite status |
| `POST` | `/api/conversations/<id>/pin` | Toggle pin status |
| `POST` | `/api/conversations/<id>/clear` | Clear message history in chat |
| `GET` | `/api/conversations/<id>/export/<format>` | Export chat (`pdf`, `txt`, `json`) |
| `POST` | `/api/conversations/import` | Import conversation from JSON |
| `POST` | `/api/upload` | Upload image file for vision chat |
| `GET` | `/api/settings` | Retrieve application settings |
| `POST` | `/api/settings` | Update application settings |

---

## 🛡️ License

This project is open-source and free to use for personal or commercial projects.
