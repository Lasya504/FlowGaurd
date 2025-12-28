FlowGaurd

FlowGaurd is a backend-focused application designed to validate workflows using rule-based logic and AI-assisted decision handling.  
It demonstrates clean backend architecture, modular design, and real-world API structuring.

## 📌 Features

- Workflow validation using structured rules  
- AI-powered logic handling  
- Modular and scalable backend architecture  
- Clear separation of routes, services, models, and utilities  

## 🏗️ Project Structure

```
FlowGaurd/
├── app/
│   ├── main.py                 # Application entry point
│   │
│   ├── models/
│   │   └── workflow.py         # Workflow data models
│   │
│   ├── routes/
│   │   └── validate.py         # API routes for validation
│   │
│   ├── services/
│   │   ├── ai_engine.py        # AI-based logic handling
│   │   └── rules.py            # Rule evaluation logic
│   │
│   └── utils/
│       └── prompts.py          # Prompt templates & helpers
│
├── requirements.txt            # Project dependencies
├── .gitignore                  # Ignored files and folders
└── README.md                   # Project documentation
```


## ⚙️ Tech Stack

- Language: Python  
- Framework: FastAPI  
- Architecture: Modular / Service-oriented  
- AI Integration: Prompt-driven logic  

## ▶️ How to Run

```bash
git clone https://github.com/Lasya504/FlowGaurd.git
cd FlowGaurd
pip install -r requirements.txt
python app/main.py




