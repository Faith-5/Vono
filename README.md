# 🎙️ Vono - Voice Notepad

> **"Speak your day into existence."**

Vono is a minimalist, voice-controlled Progressive Web App (PWA) that transforms your spoken thoughts into a beautifully organized to-do list. It feels like a native mobile app while running entirely in the browser.

---

## ✨ Features

### 🗣️ Voice-to-Tasks Intelligence
Tap the mic, speak naturally, and your speech is converted into structured, actionable tasks.

### 📱 Progressive Web App (PWA)
- Install directly on Android or iOS home screen
- Fullscreen native-app-like experience
- No browser UI when launched

### 💾 Offline Persistence
Tasks are stored locally using `localStorage`, so your data remains even after refresh or app restart.

### 🎨 Minimalist UI
Clean notebook-style interface inspired by digital productivity apps:
- Task cards with priority indicators
- Smooth interactions
- Focused, distraction-free layout

### ✅ Task Management
- Mark tasks as completed
- Auto-organized task rendering
- Lightweight and fast

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript
- MediaRecorder API (audio capture)
- PWA (Service Workers + Manifest)

### Backend
- Python
- FastAPI
- Groq API (Whisper + LLM)

---

## 🗂️ Project Structure

```text
ULTRAVOICE/
├── app/
│   ├── static/
│   │   ├── index.html        # Frontend UI
│   │   ├── manifest.json     # PWA config
│   │   ├── sw.js             # Service worker (offline support)
│   │   └── icon.png          # App icon
│   │
│   ├── main.py               # FastAPI entry point
│   ├── service.py            # Speech-to-text logic
│   ├── voice.py              # Whisper transcription
│   ├── task_extractor.py     # LLM task parsing
│   └── config.py             # Environment config
│
├── .env                      # API keys (ignored in git)
├── requirements.txt
└── README.md
````

---

## 🚀 Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/Faith-5/Vono.git
cd vono
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run the backend server

```bash
uvicorn app.main:app --reload
```

---

### 6. Open the app

```
http://127.0.0.1:8000
```

> ⚠️ Microphone access works only on `localhost` or HTTPS.

---

## 🌍 Deployment

### Recommended platforms:

* Render
* Railway
* Fly.io

---

### Deploy steps (Render example)

1. Push project to GitHub
2. Create new Web Service on Render
3. Connect repository
4. Set:

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

5. Add environment variable:

```
GROQ_API_KEY=your_key_here
```

6. Deploy 🚀

---

## 📱 Install as PWA

Once deployed:

### Android (Chrome)

* Open site
* Tap menu (⋮)
* “Add to Home Screen”

### iOS (Safari)

* Tap Share button
* “Add to Home Screen”

Now it behaves like a native app 🎉

---

## 🧠 Project Vision

Vono is designed to replace traditional note-taking by turning:

> 🎤 spoken thoughts → structured productivity system

It bridges voice input + AI reasoning + task execution.

---

## 📄 License

MIT License — free to use and modify.
---