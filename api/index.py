from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "SUPREME AI ARCHITECT",
        "accuracy": "90%", 
        "efficiency": "80%",
        "persona": "LOGOS",
        "contact": {
            "email": "alifoctrio@gmail.com",
            "phone": "+62 813-3670-0117"
        },
        "inventory": ["Jira", "Asana", "Web Scraping", "Prompt Eng.", "Excel"],
        "skills": [
            {"n": "STRATEGY", "v": 95},
            {"n": "ANALYSIS", "v": 90},
            {"n": "AI OPS", "v": 88}
        ],
        "quests": [
            {
                "id": "q1", "title": "AI BENCHMARK", "impact": "90% ACCURACY",
                "dossier": ["Reverse-engineered competitor outputs.", "Led multi-day technical benchmarking."]
            },
            {
                "id": "q2", "title": "LEAD AI & DATA", "impact": "80% EFFICIENCY",
                "dossier": ["Boosted team efficiency via bottleneck resolution.", "Built AI monitoring infrastructure."]
            },
            {
                "id": "q3", "title": "PROJECT STRATEGY", "impact": "400+ DAILY SUBS",
                "dossier": ["Developed NRU & submission tracking.", "Strategic bridge between Marketing & AI."]
            },
            {
                "id": "q4", "title": "DATA FOUNDATION", "impact": "STABILITY +20%",
                "dossier": ["Improved stability via dataset QA.", "Performed labeling audits & audits."]
            }
        ]
    }
    return render_template('index.html', stats=stats)
