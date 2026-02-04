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
        "inventory": ["Jira", "Asana", "Web Scraping", "Prompt Eng.", "Excel"],
        "skills": [
            {"n": "PROJECT MGMT", "v": 95},
            {"n": "AI OPS", "v": 90},
            {"n": "BENCHMARKING", "v": 92}
        ],
        "quests": [
            {
                "id": "q1", "title": "AI TECH BENCHMARK", "impact": "90% ACCURACY",
                "intel": "Reverse-engineered competitor features to identify technical gaps and influence roadmap decisions.",
                "loot": ["Competitor Intel Dossier", "Accuracy Buff: +30%"]
            },
            {
                "id": "q2", "title": "LEAD AI & DATA OPS", "impact": "80% EFFICIENCY",
                "intel": "Optimized execution workflows and resolved bottlenecks to boost AI team performance.",
                "loot": ["Process Efficiency Perk", "R&D Pipeline Blueprint"]
            },
            {
                "id": "q3", "title": "PRODUCT STRATEGY", "impact": "400+ DAILY SUBS",
                "intel": "Translated AI capabilities into actionable product roadmap and GTM strategies.",
                "loot": ["KPI Tracking Mastery", "Market Signal Logic"]
            },
            {
                "id": "q4", "title": "DATA FOUNDATION", "impact": "STABILITY +20%",
                "intel": "Fortified AI scalability through rigorous dataset audits and quality assurance cycles.",
                "loot": ["Data Reliability Buff", "QA Precision Mastery"]
            }
        ],
        "contact": {"email": "alifoctrio@gmail.com", "phone": "+62 813-3670-0117"}
    }
    return render_template('index.html', stats=stats)
