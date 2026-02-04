from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "STRATEGIC PRODUCT & AI ARCHITECT",
        "exp_years": "Aug 2022 - Sept 2025",
        "accuracy": "90%", 
        "efficiency": "80%",
        "persona": "LOGOS",
        "passive": "Epistemic Sovereign: Translating raw market signals into strategic roadmaps.",
        "contact": {
            "email": "alifoctrio@gmail.com",
            "phone": "+62 813-3670-0117",
            "linkedin": "linkedin.com/in/alifoctrio"
        },
        "inventory": ["Competitor Reverse-Engineering", "Technical Benchmarking", "Product Strategy", "Sentiment Frameworks"],
        "quests": [
            {
                "id": "q1",
                "title": "MISSION: AI TECHNICAL BENCHMARK",
                "company": "Eklipse.gg",
                "impact": "60% → 90% ACCURACY",
                "achievements": ["Signature Skill: Competitor Reverse-Engineering", "Framework: Systematic Technical Analysis", "Loot: Benchmarking Strategy Dossier"],
                "dossier": [
                    "Identified AI performance gaps by reverse-engineering competitor outputs.",
                    "Led multi-day technical benchmarking to influence feature prioritization.",
                    "Delivered insights that directly influenced AI roadmap decisions.",
                    "Reduced iteration cycles by identifying high-impact improvements early."
                ]
            },
            {
                "id": "q2",
                "title": "MISSION: LEAD AI & DATA OPTIMIZATION",
                "company": "Eklipse.gg",
                "impact": "~80% EFFICIENCY BOOST",
                "achievements": ["Perk: Bottleneck Resolution Mastery", "Loot: R&D-to-Production Pipeline", "Buff: AI Monitoring Infrastructure"],
                "dossier": [
                    "Increased operational success rate by improving execution workflows.",
                    "Boosted AI team efficiency by ~80% through bottleneck resolution.",
                    "Translated R&D experiments into production pipelines with measurable impact.",
                    "Built AI performance monitoring frameworks to track quality & delivery."
                ]
            },
            {
                "id": "q3",
                "title": "MISSION: PROJECT MANAGER & STRATEGY",
                "company": "Eklipse.gg",
                "impact": "SCALED TO 400+ DAILY SUBS",
                "achievements": ["Item: User Sentiment Analysis Framework", "Loot: Internal KPI Tracking System", "Skill: Cross-functional Bridge"],
                "dossier": [
                    "Led market intelligence using web scraping and competitor research.",
                    "Developed internal KPI tracking systems (NRU & 400+ daily submissions).",
                    "Acted as a strategic bridge between Product, Marketing, and AI teams.",
                    "Translated raw market signals into actionable business recommendations."
                ]
            },
            {
                "id": "q4",
                "title": "MISSION: DATA QUALITY FOUNDATION",
                "company": "PT. MAINGAMES",
                "impact": "SYSTEM STABILITY +20%",
                "achievements": ["Loot: Bounding Box Precision Mastery", "Buff: Production-Grade Data Reliability", "Skill: Dataset Audit Excellence"],
                "dossier": [
                    "Improved AI system stability by 20% through dataset quality assurance.",
                    "Performed labeling validation, bounding box correction, and dataset audits.",
                    "Integrated user feedback from App Store reviews into data cycles.",
                    "Maintained high-grade data reliability for long-term AI scalability."
                ]
            }
        ],
        "education": {
            "school": "Universitas Gadjah Mada",
            "major": "Philosophy | GPA: 3.06",
            "desc": "Applied logic and ethics in decision-making and data management."
        }
    }
    return render_template('index.html', stats=stats)
