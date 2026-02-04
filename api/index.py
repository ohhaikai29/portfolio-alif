from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "SUPREME AI STRATEGIST",
        "accuracy": "90%", 
        "efficiency": "80%",
        "persona": "LOGOS",
        "inventory": ["Jira", "Asana", "Web Scraping", "Prompt Eng.", "Excel"],
        "skills": [
            {"n": "STRATEGY", "v": 95},
            {"n": "AI OPERATIONS", "v": 90},
            {"n": "BENCHMARKING", "v": 92}
        ],
        "quests": [
            {
                "id": "q1", "title": "AI TECHNICAL BENCHMARK", "impact": "90% ACCURACY", "rank": "S",
                "intel": "Strengthened AI competitiveness through systematic benchmarking and competitor reverse-engineering.",
                "loot": ["Competitor Intel Dossier", "Accuracy Buff: +30%", "Strategy Mastery"]
            },
            {
                "id": "q2", "title": "LEAD AI & DATA OPS", "impact": "80% EFFICIENCY", "rank": "S",
                "intel": "Translated R&D experiments into production pipelines and optimized execution workflows.",
                "loot": ["Team Efficiency Perk", "Process Optimization Blueprint"]
            },
            {
                "id": "q3", "title": "PM & MARKET STRATEGY", "impact": "400+ DAILY SUBS", "rank": "A",
                "intel": "Led product initiatives by translating AI capabilities into data-driven market decisions.",
                "loot": ["KPI Tracking Mastery", "Product-Market Fit Insight"]
            },
            {
                "id": "q4", "title": "DATA QUALITY FOUNDATION", "impact": "STABILITY +20%", "rank": "B",
                "intel": "Fortified AI scalability through rigorous labeling validation and dataset audits.",
                "loot": ["Data Reliability Buff", "QA Precision Skill"]
            }
        ],
        "contact": {"email": "alifoctrio@gmail.com", "phone": "+62 813-3670-0117", "linkedin": "alifoctrio"}
    }
    return render_template('index.html', stats=stats)
