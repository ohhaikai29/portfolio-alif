from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "LEAD AI OPERATIONS & STRATEGIC PM",
        "exp_years": "Aug 2022 - Sept 2025",
        "performance": "90%", 
        "strategy": "85%",
        "persona": "LOGOS",
        "passive": "Epistemic Sovereignty: Logic & Ethics in High-Stakes AI Management.",
        "social_stats": [5, 5, 5, 4, 5], 
        "contact": {
            "email": "alifoctrio@gmail.com",
            "phone": "+62 813-3670-0117",
            "linkedin": "linkedin.com/in/alifoctrio"
        },
        "inventory": ["Competitor Benchmarking", "Reverse Engineering", "Market Intelligence", "Web Scraping", "Roadmap Planning"],
        "quests": [
            {
                "id": "mission_ai_lead",
                "title": "MISSION: AI BENCHMARKING & REVERSE ENGINEERING",
                "company": "Eklipse.gg",
                "role": "Lead AI and Data Optimization",
                "impact": "AI SUCCESS RATE 60% → 90%",
                "summary": "Mastered competitor intelligence by reverse-engineering outputs and conducting multi-day technical benchmarking.",
                "assets": ["Competitor Intel Reports", "Reverse-Engineering Framework", "Accuracy Benchmarks"],
                "dossier": [
                    "Identified AI performance gaps by REVERSE-ENGINEERING competitor outputs.",
                    "Led end-to-end AI operations and MULTI-DAY technical benchmarking.",
                    "Influenced feature prioritization by benchmarking accuracy against market leaders.",
                    "Reduced AI iteration cycles through systematic benchmark analysis."
                ]
            },
            {
                "id": "mission_pm",
                "title": "MISSION: STRATEGIC PRODUCT DOMINATION",
                "company": "Eklipse.gg",
                "role": "Project Manager & Market Strategy",
                "impact": "SCALED TO 400+ DAILY SUBS",
                "summary": "Orchestrated data-driven product strategy by synchronizing AI capabilities with market insights.",
                "assets": ["Sentiment Analysis Framework", "NRU Tracking System", "Market Intelligence Data"],
                "dossier": [
                    "Conducted deep market intelligence via web scraping and community insights.",
                    "Designed user sentiment analysis frameworks to support marketing pivots.",
                    "Developed internal KPI tracking systems (NRU & 400+ daily submissions).",
                    "Acted as a strategic bridge between Product, Marketing, and AI teams."
                ]
            }
        ],
        "education": {
            "title": "ACADEMIC SIDE-QUEST",
            "school": "Universitas Gadjah Mada",
            "major": "Philosophy | GPA: 3.06",
            "desc": "Applied logic and epistemology to data management and strategic decision making."
        }
    }
    return render_template('index.html', stats=stats)

# Hapus app.run agar tidak loading terus di Vercel
