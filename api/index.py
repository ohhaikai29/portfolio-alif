from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    try:
        stats = {
            "level": "03",
            "rank": "STRATEGIC PRODUCT ARCHITECT",
            "exp_years": "Aug 2022 - Sept 2025",
            "accuracy": "90%", 
            "efficiency": "80%",
            "persona": "LOGOS",
            "passive": "Logic-based Leadership",
            "contact": {
                "email": "alifoctrio@gmail.com",
                "phone": "+62 813-3670-0117",
                "linkedin": "linkedin.com/in/alifoctrio"
            },
            "inventory": ["Jira", "Asana", "Excel", "Prompt Eng.", "Web Scraping"],
            "skills": [
                {"name": "Project Management", "lvl": "MAX"},
                {"name": "AI Benchmarking", "lvl": "HIGH"},
                {"name": "Reverse Engineering", "lvl": "PRO"}
            ],
            "quests": [
                {
                    "id": "q1",
                    "title": "MISSION: AI TECHNICAL BENCHMARK",
                    "company": "Eklipse.gg",
                    "impact": "60% → 90% ACCURACY",
                    "achievements": ["Signature Skill: Competitor Reverse-Engineering", "Framework: Systematic Technical Analysis"],
                    "dossier": [
                        "Identified AI performance gaps by reverse-engineering competitor outputs.",
                        "Led multi-day technical benchmarking to influence feature prioritization.",
                        "Delivered insights that directly influenced AI roadmap decisions."
                    ]
                },
                {
                    "id": "q2",
                    "title": "MISSION: LEAD AI & DATA OPTIMIZATION",
                    "company": "Eklipse.gg",
                    "impact": "~80% EFFICIENCY BOOST",
                    "achievements": ["Perk: Bottleneck Resolution Mastery", "Loot: R&D-to-Production Pipeline"],
                    "dossier": [
                        "Increased operational success rate by improving execution workflows.",
                        "Boosted AI team efficiency by ~80% through bottleneck resolution.",
                        "Translated R&D experiments into production pipelines."
                    ]
                },
                {
                    "id": "q3",
                    "title": "MISSION: PROJECT MANAGER & STRATEGY",
                    "company": "Eklipse.gg",
                    "impact": "SCALED TO 400+ DAILY SUBS",
                    "achievements": ["Item: User Sentiment Analysis Framework", "Loot: Internal KPI Tracking System"],
                    "dossier": [
                        "Led market intelligence using web scraping and competitor research.",
                        "Developed internal KPI tracking systems (NRU & 400+ daily submissions).",
                        "Acted as a strategic bridge between Product, Marketing, and AI teams."
                    ]
                },
                {
                    "id": "q4",
                    "title": "MISSION: DATA QUALITY FOUNDATION",
                    "company": "PT. MAINGAMES",
                    "impact": "SYSTEM STABILITY +20%",
                    "achievements": ["Loot: Bounding Box Precision Mastery", "Buff: Data Reliability"],
                    "dossier": [
                        "Improved AI system stability by 20% through dataset quality assurance.",
                        "Performed labeling validation, bounding box correction, and audits.",
                        "Integrated user feedback from App Store reviews into data cycles."
                    ]
                }
            ],
            "education": {
                "school": "Universitas Gadjah Mada",
                "major": "Philosophy | GPA: 3.06",
                "desc": "Applied logic and ethics in decision-making."
            }
        }
        return render_template('index.html', stats=stats)
    except Exception as e:
        return f"Build Error: {str(e)}"

app.debug = True
