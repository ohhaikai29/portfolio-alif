import os
from flask import Flask, render_template

# Konfigurasi static folder agar foto tidak hilang
app = Flask(__name__, static_url_path='/static', static_folder='static')

import os
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "STRATEGIC AI OPERATIONS & PM LEAD",
        "exp_years": "Aug 2022 - Sept 2025", # Sudah diperbaiki sesuai CV
        "kpi": "90%", 
        "opt": "85%",
        "persona_name": "LOGOS",
        "passive": "Epistemic Insight: Applying ethics, logic, and philosophy of science to data-driven leadership.",
        "social_stats": [5, 5, 5, 4, 5], 
        "contact": {
            "email": "alifoctrio@gmail.com",
            "phone": "+62 813-3670-0117",
            "linkedin": "linkedin.com/in/alifoctrio"
        },
        "inventory": ["Reverse Engineering", "Benchmark Analysis", "Market Strategy", "Web Scraping", "Technical PM"],
        "tech_stack": ["Jira", "Asana", "Trello", "Advanced Excel", "Prompt Engineering"],
        "quests": [
            {
                "id": "eklipse_lead",
                "title": "OP: AI LEADERSHIP AWAKENING",
                "company": "Eklipse.gg",
                "role": "Lead AI and Data Optimization",
                "achievement": "AI SUCCESS RATE 60% → 90%",
                "how": "Directed end-to-end AI operations and identified gaps by reverse-engineering competitor outputs.",
                "loot": ["Competitor Performance Data", "Signature: Benchmark Analysis", "Optimized Model Framework"],
                "details": [
                    "Identified AI performance gaps by REVERSE-ENGINEERING competitor outputs.",
                    "Led multi-day technical benchmarking to influence feature prioritization.",
                    "Built monitoring frameworks to align AI results with business stakeholders.",
                    "Reduced AI iteration cycles through systematic benchmark analysis."
                ]
            },
            {
                "id": "eklipse_pm",
                "title": "OP: MARKET STRATEGY DOMINATION",
                "company": "Eklipse.gg",
                "role": "Project Manager & Market Strategy",
                "achievement": "400+ Daily Submissions Pipeline",
                "how": "Translated AI capabilities and market signals into actionable product decisions.",
                "loot": ["Sentiment Analysis Framework", "NRU Tracking System", "Product-Market Fit Data"],
                "details": [
                    "Conducted market intelligence via web scraping and community insights.",
                    "Designed user sentiment analysis frameworks for marketing pivot decisions.",
                    "Developed NRU tracking systems to evaluate campaign effectiveness.",
                    "Strategic bridge between Product, Marketing, and AI teams."
                ]
            },
            {
                "id": "maingames_ops",
                "title": "OP: DATA FOUNDATION QUEST",
                "company": "PT. MAINGAMES",
                "role": "AI and Data Optimization Staff",
                "achievement": "System Stability +20%",
                "how": "Enhanced training dataset quality and large-scale data quality assurance.",
                "loot": ["Bounding Box Precision Mastery", "Production-Grade Data Reliability", "User Feedback Loop"],
                "details": [
                    "Improved AI system stability through dataset quality enhancement.",
                    "Performed labeling validation, bounding box correction, and dataset audits.",
                    "Integrated App Store reviews and social media into data cycles.",
                    "Maintained production-grade data reliability for long-term scalability."
                ]
            }
        ],
        "education": {
            "title": "SIDE QUEST: HIGHER EDUCATION",
            "school": "Universitas Gadjah Mada",
            "major": "Philosophy | GPA: 3.06",
            "desc": "Applied ethics, logic, and epistemology to data management and leadership."
        }
    }
    return render_template('index.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
    return render_template('index.html', stats=stats)

app.debug = True
