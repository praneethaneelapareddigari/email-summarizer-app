# AI Email Summarizer Project
Summarize email content using **Gemma 2B LLM** locally via Ollama, powered by **Flask** and **Docker**.
Docker Desktop installed → [Download here](https://www.docker.com/products/docker-desktop)
Steps to Build & Run

```bash
# Clone this repository
git clone https://github.com/<your-username>/email_summarizer_app.git
cd email_summarizer_app

# Build and start containers
docker-compose up --build
## Overview
This project uses Flask, LangChain, and Ollama to build an app that summarizes email content using LLMs.

## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Run Ollama server and load a model (e.g., llama2)
3. Start the Flask app: `python run.py`
4. Open `http://127.0.0.1:5000` in your browser
