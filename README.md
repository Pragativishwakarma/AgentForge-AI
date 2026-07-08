# 🤖 AgentForge-AI

> **An Intelligent Multi-Agent AI Automation System powered by LangChain, Groq LLM, and Tool Calling Agents.**

AgentForge-AI is a modular multi-agent framework that demonstrates how multiple AI agents can collaborate to solve complex tasks through intelligent reasoning, tool invocation, and workflow automation. The project leverages Large Language Models (LLMs), external tools, and memory to execute tasks autonomously.

---

## 🚀 Features

* 🧠 Multi-Agent Architecture
* 🤖 Groq LLM Integration
* 🛠️ Tool Calling with LangChain
* 💬 Conversational Memory
* 🌦️ Weather Information Agent
* 🗄️ SQL Database Query Agent
* 📧 Email Automation Support
* ⚡ Fast and Modular Design
* 🔐 Secure API Key Management using `.env`
* 🧩 Easily Extendable with Custom Agents and Tools

---

## 📂 Project Structure

```text
AgentForge-AI/
│
├── main.py                 # Application entry point
├── runner.py               # Agent execution logic
├── agent.py                # Main AI agent configuration
├── weather_agent.py        # Weather-specific AI agent
├── sql_agent.py            # SQL query agent
├── tool.py                 # Custom tool definitions
├── company.db              # Sample SQLite database
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (not committed)
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

* Python 3.x
* LangChain
* LangChain Groq
* Groq LLM
* SQLite
* Requests
* Pydantic
* Python Dotenv

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pragativishwakarma/AgentForge-AI.git

cd AgentForge-AI
```

### 2. Create a virtual environment

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

> **Important:** Never commit your `.env` file or API keys to GitHub.

---

## ▶️ Running the Project

```bash
python main.py
```

---

## 💡 Example Use Cases

* Retrieve weather information
* Execute SQL queries using AI
* Build and test tool-calling agents
* Develop autonomous AI workflows
* Experiment with multi-agent collaboration
* Learn LangChain agent orchestration

---

## 📈 Future Enhancements

* Web-based user interface
* Retrieval-Augmented Generation (RAG)
* Persistent conversation memory
* Vector database integration
* Multi-agent planning and coordination
* API deployment with FastAPI
* Docker support
* Cloud deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📜 License

This project is intended for educational and learning purposes. You are welcome to modify and extend it for your own projects.

---

## 👩‍💻 Author

**Pragati Vishwakarma**

* AI & Data Science Engineer
* Passionate about Generative AI, Multi-Agent Systems, NLP, Computer Vision, and Intelligent Automation.

If you found this project useful, consider giving it a ⭐ on GitHub.
