# 📖 StoryGenie — Offline AI Story Generator

> *Personalized stories. Local intelligence. Zero cloud dependency.*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?style=flat-square)](https://www.langchain.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black?style=flat-square)](https://ollama.com/)
[![Llama 3](https://img.shields.io/badge/Llama%203-8B-0467DF?style=flat-square&logo=meta&logoColor=white)](https://llama.meta.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

---

## 🌟 Project Overview

**StoryGenie** is a fully **offline, privacy-first Generative AI web application** built to create highly personalized, age-appropriate stories — all without sending a single byte of data to the cloud.

It was built to solve two critical problems with today's AI tools:

| Problem | StoryGenie's Solution |
|---|---|
| 🔒 **Privacy** | Runs 100% locally — no data ever leaves your machine |
| 🌐 **Accessibility** | Works without an internet connection |

Whether you're a parent, educator, or creative writer, StoryGenie lets you generate tailored content for any audience — safely, privately, and instantly.

---

## 🏗️ Architecture Overview

StoryGenie uses a clean **three-tier architecture**, built entirely in Python:

```
┌─────────────────────────────────────────┐
│           User Interface                │
│         (Streamlit Frontend)            │
└────────────────┬────────────────────────┘
                 │ User Inputs
                 ▼
┌─────────────────────────────────────────┐
│        Backend Orchestration            │
│      (LangChain Prompt Engine)          │
└────────────────┬────────────────────────┘
                 │ Formatted Prompt
                 ▼
┌─────────────────────────────────────────┐
│          Local AI Engine                │
│    (Ollama → Llama 3 8B Model)          │
└─────────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

### 🎨 Frontend — Streamlit
The entire UI is built using native Streamlit elements — no custom HTML or CSS injection. This keeps the app lightweight, highly responsive, and easy to maintain from a single Python script.

**Key Concept:** Streamlit's `Session State` serves as the app's memory, ensuring the generated story persists even when the user interacts with other controls (download, rating, editing).

---

### ⚙️ Backend Orchestration — LangChain
LangChain acts as the intelligent bridge between user inputs and the AI model. Instead of raw text, it maps user parameters (Name, Age, Genre, Moral) into a strict, hidden **Prompt Template** that enforces formatting rules and age-appropriate vocabulary constraints automatically.

---

### 🖥️ Local AI Server — Ollama
Ollama runs as a local server on your Windows machine, hosting the LLM directly on your hardware. It completely bypasses any cloud API, ensuring offline operation and zero data leakage.

---

### 🧠 The Model — Llama 3 (8B Parameters)
Meta's **Llama 3 8B** is an open-source, state-of-the-art model. The 8B variant offers an excellent balance of creative writing quality and performance efficiency — capable of running smoothly on consumer hardware without requiring a dedicated server GPU.

---

## 🔄 How It Works — Data Flow

Here's what happens when you click **"Generate"**:

```
1. DATA INGESTION
   └─► User selects: Protagonist Name, Age Group, Genre, Story Moral

2. PROMPT ENGINEERING
   └─► LangChain maps inputs into a hidden prompt template
       e.g., "Write a Fantasy story for a Toddler named Alex.
              Vocabulary MUST be strictly age-appropriate..."

3. LOCAL INFERENCE
   └─► Formatted prompt sent to the Ollama local server
       └─► Llama 3 generates the story and streams it back

4. STATE MANAGEMENT & DISPLAY
   └─► Streamlit captures output → saves to Session State
       └─► Story rendered inside an editable text box

5. POST-PROCESSING
   └─► User can: Edit the story | Download as .txt | Rate (0–10)
```

---

## ✨ Key Technical Achievements

- **🔌 Offline Functionality** — Production-grade Generative AI deployed and used with zero external network dependencies.

- **🎭 Dynamic Tone Mapping** — Successfully restricts Llama 3 to output vocabulary appropriate to specific age tiers. A "horror" story for a "toddler" is guaranteed to remain mild and age-safe.

- **✏️ Interactive Editing Loop** — Bridges the gap between static AI output and human creativity. Users can modify the generated story and "commit" edits before exporting — a true human-in-the-loop workflow.

---

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed on your system:

- [Python 3.10+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/download) (for running the local LLM server)
- The **Llama 3** model pulled via Ollama

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/aizensosuke0617-cyber/Story-Genie.git
cd Story-Genie

# 2. Install Python dependencies
pip install streamlit langchain langchain-community

# 3. Pull the Llama 3 model (one-time setup)
ollama pull llama3

# 4. Start the Ollama server (in a separate terminal)
ollama serve

# 5. Run the Streamlit app
streamlit run app.py
```

> **Note:** Ollama must be running in the background before launching the app.

---

## 📁 Project Structure

```
Story-Genie/
│
├── app.py          # Main application — UI, AI logic, and session management
├── README.md       # Project documentation
└── ...
```

---

## 🎯 Use Cases

- 👨‍👩‍👧 **Parents** — Generate bedtime stories personalized to their child's name and age
- 🏫 **Educators** — Create classroom-safe stories with specific moral lessons
- ✍️ **Writers** — Use as an offline creative writing assistant and idea generator

---

## 🔒 Privacy Guarantee

StoryGenie is designed from the ground up with privacy as a core principle:

- ✅ All computation happens on **your local machine**
- ✅ **No API keys** required
- ✅ **No internet connection** needed after setup
- ✅ **No user data** is sent to any server — ever

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 👤 Author

- GitHub: [@aizensosuke0617-cyber](https://github.com/aizensosuke0617-cyber)

---

*Built with ❤️ using Python, Streamlit, LangChain, Ollama, and Llama 3*
