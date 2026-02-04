from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "AI STRATEGIC BENCHMARK LEAD",
        "exp_years": "Aug 2022 - Sept 2025",
        "kpi": "90%", 
        "opt": "85%",
        "persona_name": "LOGOS",
        "passive": "Epistemic Insight: Unlocked multi-day technical benchmarking & competitive reverse-engineering.",
        "social_stats": [5, 5, 5, 4, 5], 
        "contact": {
            "email": "alifoctrio@gmail.com",
            "phone": "+62 813-3670-0117",
            "linkedin": "linkedin.com/in/alifoctrio"
        },
        "inventory": ["Technical Benchmarking", "Reverse Engineering", "Market Intelligence", "KPI Definition", "Product Strategy"],
        "quests": [
            {
                "id": "eklipse_lead",
                "title": "MISSION: COMPETITIVE AI BENCHMARKING",
                "company": "Eklipse.gg",
                "role": "Lead AI and Data Optimization",
                "impact": "SUCCESS RATE 60% → 90%",
                "dossier": [
                    "IDENTIFIED AI performance gaps by reverse-engineering competitor outputs to influence feature prioritization.",
                    "LED end-to-end AI operations including multi-day technical benchmarking and performance analysis.",
                    "Improved AI operational success rate from 60% to 90% through structured execution monitoring.",
                    "BUILT monitoring and reporting frameworks to align benchmark results with Business stakeholders.",
                    "REDUCED AI iteration cycles by identifying high-impact optimization areas through systematic analysis."
                ]
            },
            {
                "id": "eklipse_pm",
                "title": "MISSION: PRODUCT & MARKET STRATEGY",
                "company": "Eklipse.gg",
                "role": "Project Manager & Market Strategy",
                "impact": "SCALED TO 400+ DAILY SUBS",
                "dossier": [
                    "Translated AI capabilities and market signals into actionable product roadmaps.",
                    "Conducted market intelligence via web scraping and community insights to identify product opportunities.",
                    "Designed user sentiment analysis frameworks to support strategic marketing pivot decisions.",
                    "Developed NRU tracking systems to evaluate product-market fit and campaign effectiveness.",
                    "Acted as a strategic bridge between Product, Marketing, and AI teams."
                ]
            },
            {
                "id": "maingames_ops",
                "title": "MISSION: DATA QUALITY FOUNDATION",
                "company": "PT. MAINGAMES",
                "role": "AI and Data Optimization Staff",
                "impact": "SYSTEM STABILITY +20%",
                "dossier": [
                    "Supported AI performance through high-quality data preparation and dataset audits.",
                    "Improved AI system stability by 20% through training dataset quality assurance.",
                    "Performed labeling validation and bounding box correction to reduce training noise.",
                    "Integrated user feedback from App Store and social media into data improvement cycles.",
                    "Maintained production-grade data reliability to support long-term AI scalability."
                ]
            }
        ],
        "education": {
            "school": "Universitas Gadjah Mada",
            "major": "Philosophy | GPA: 3.06",
            "desc": "Applied ethics, logic, and philosophy of science in decision-making and leadership."
        }
    }
    return render_template('index.html', stats=stats)
