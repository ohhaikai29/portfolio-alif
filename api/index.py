from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "MID-TIER STRATEGIST", # Leveling system
        "exp_years": "3+ Years Experience",
        "hp": 999,
        "sp": 850,
        "persona_name": "LOGOS",
        "philosophy_perk": "Logical Reasoning & Ethics +50",
        "social_stats": [5, 4, 4, 3, 4],
        "contact": {
            "email": "alifoctrio@gmail.com",
            "phone": "+62 813-3670-0117",
            "linkedin": "linkedin.com/in/alifoctrio",
            "portfolio": "portfolio-alif-two.vercel.app"
        },
        "quests": [
            {
                "id": "eklipse",
                "title": "OP: EKLIPSE MASTERY",
                "short": "Optimized AI Accuracy 60% → 90%",
                "details": [
                    "Translating AI capabilities into actionable product roadmaps.",
                    "Conducted competitor analysis via web scraping & market signals.",
                    "Implemented sentiment analysis frameworks for marketing pivots.",
                    "Developed KPI systems tracking 400+ daily submissions."
                ]
            },
            {
                "id": "maingames",
                "title": "OP: DATA FOUNDATION",
                "short": "Stability +20% | Reduced Training Noise",
                "details": [
                    "Improved AI system stability through large-scale data QA.",
                    "Performed labeling validation and bounding box correction.",
                    "Integrated App Store & social media feedback into data cycles.",
                    "Assisted TM data entry to monitor Facebook Gaming content."
                ]
            }
        ]
    }
    return render_template('index.html', stats=stats)

app.debug = True
