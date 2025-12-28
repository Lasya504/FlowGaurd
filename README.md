# 🚀 FlowGaurd

FlowGaurd is a backend-focused application designed to validate workflows using rule-based logic and AI-assisted decision handling.  
It demonstrates clean backend architecture, modular design, and real-world API structuring.

---

## 📌 Features

- Workflow validation using structured rules  
- AI-powered logic handling  
- Modular and scalable backend architecture  
- Clear separation of routes, services, models, and utilities  

---

## 🏗️ Project Structure

FlowGaurd/
│
├── app/
│   ├── main.py
│   ├── models/
│   │   └── workflow.py
│   ├── routes/
│   │   └── validate.py
│   ├── services/
│   │   ├── ai_engine.py
│   │   └── rules.py
│   └── utils/
│       └── prompts.py
│
├── requirements.txt
├── .gitignore
└── README.md

---

## ⚙️ Tech Stack

- Language: Python  
- Framework: FastAPI  
- Architecture: Modular / Service-oriented  
- AI Integration: Prompt-driven logic  

---

## ▶️ How to Run

```bash
git clone https://github.com/Lasya504/FlowGaurd.git
cd FlowGaurd
pip install -r requirements.txt
python app/main.py
