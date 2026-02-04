from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    try:
        stats = {
            "level": "03",
            "rank": "S.E.E.S. STRATEGIC ARCHITECT", # Vibe P3R
            "exp_years": "Aug 2022 - Sept 2025",
            "accuracy": "90%", 
            "efficiency": "80%",
            "persona": "LOGOS",
            "passive": "Analysis & Execution Mastery",
            "contact": {
                "email": "alifoctrio@gmail.com",
                "phone": "+62 813-3670-0117",
                "linkedin": "linkedin.com/in/alifoctrio"
            },
            "inventory": ["Jira", "Asana", "Excel", "Prompt Eng.", "Web Scraping"],
            "skills": [
                {"name": "Project Management", "lvl": "MAX"},
                {"name": "AI Benchmarking", "lvl": "RANK 9"},
                {"name": "Reverse Engineering", "lvl": "RANK 8"}
            ],
            "quests": [
                {
                    "id": "q1",
                    "title": "MISSION: AI TECHNICAL BENCHMARK",
                    "impact": "60% → 90% ACCURACY",
                    "achievements": ["Signature Skill: Reverse-Engineering", "Framework: Technical Analysis"],
                    "dossier": ["Identified gaps by reverse-engineering competitor outputs.", "Led multi-day technical benchmarking.", "Influenced strategic roadmap decisions."]
                },
                {
                    "id": "q2",
                    "title": "MISSION: LEAD AI & DATA OPS",
                    "impact": "80% EFFICIENCY BOOST",
                    "achievements": ["Perk: Bottleneck Resolution Mastery", "Loot: R&D-to-Production"],
                    "dossier": ["Increased operational success rate via workflows.", "Boosted team efficiency by 80%.", "Built performance monitoring frameworks."]
                },
                {
                    "id": "q3",
                    "title": "MISSION: PM & MARKET STRATEGY",
                    "impact": "400+ DAILY SUBS",
                    "achievements": ["Item: Sentiment Analysis Framework", "Loot: KPI Tracking System"],
                    "dossier": ["Led market intelligence via web scraping.", "Developed NRU & submission tracking systems.", "Strategic bridge between teams."]
                },
                {
                    "id": "q4",
                    "title": "MISSION: DATA QUALITY FOUNDATION",
                    "impact": "SYSTEM STABILITY +20%",
                    "achievements": ["Loot: Bounding Box Precision", "Buff: Data Reliability"],
                    "dossier": ["Improved stability via dataset QA.", "Performed labeling validation & audits.", "Integrated user feedback cycles."]
                }
            ]
        }
        return render_template('index.html', stats=stats)
    except Exception as e:
        return f"Error: {str(e)}"
