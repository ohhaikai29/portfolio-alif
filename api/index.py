from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "AI STRATEGIST",
        "exp_years": "3.5 Years Experience",
        "kpi": "90%", # Ganti HP jadi KPI (Key Performance Index)
        "opt": "85%", # Ganti SP jadi OPT (Optimization Level)
        "persona_name": "LOGOS",
        "philosophy_perk": "Decision-making based on Logic & Ethics",
        "social_stats": [5, 4, 4, 4, 3],
        "contact": {
            "email": "alifoctrio@gmail.com",
            "phone": "+62 813-3670-0117",
            "linkedin": "linkedin.com/in/alifoctrio"
        },
        "quests": [
            {
                "id": "eklipse",
                "title": "OP: EKLIPSE MASTERY",
                "achievement": "AI Accuracy 60% → 90%",
                "how": "Reverse-engineered competitor outputs and implemented multi-day technical benchmarking.",
                "loot": ["High-Precision AI Framework", "400+ Daily Submission Pipeline", "NRU Tracking Mastery"],
                "details": ["Data-driven product strategy", "Market intelligence via web scraping", "Cross-functional bridge: Product, AI, & Marketing"]
            },
            {
                "id": "maingames",
                "title": "OP: DATA STABILIZATION",
                "achievement": "System Stability +20%",
                "how": "Enhanced training dataset quality and large-scale QA to reduce training noise.",
                "loot": ["Production-Grade Data Reliability", "Bounding Box Precision Skill", "Feedback Integration Blueprint"],
                "details": ["Labeling validation", "Bounding box correction", "Facebook Gaming creator content monitoring"]
            }
        ],
        "education": {
            "title": "SIDE QUEST: ACADEMIC FOUNDATION",
            "school": "Universitas Gadjah Mada",
            "major": "Philosophy | GPA: 3.06",
            "reward_skill": "Philosopher's Stone: Unlocked Advanced Ethics & Epistemology in Decision Making"
        }
    }
    return render_template('index.html', stats=stats)
