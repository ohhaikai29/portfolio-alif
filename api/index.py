import os
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    try:
        stats = {
            "level": "03",
            "rank": "STRATEGIC PRODUCT & AI LEAD",
            "exp_years": "Aug 2022 - Sept 2025",
            "performance": "90%", 
            "strategy": "85%",
            "persona": "LOGOS",
            "passive": "Epistemic Sovereignty: Integrating ethics and logic into high-stakes decision making.",
            "social_stats": [5, 5, 5, 4, 5], 
            "contact": {
                "email": "alifoctrio@gmail.com",
                "phone": "+62 813-3670-0117",
                "linkedin": "linkedin.com/in/alifoctrio"
            },
            "inventory": ["Competitor Benchmarking", "Product Roadmap", "Stakeholder Alignment", "Web Scraping", "Market Intelligence"],
            "tech_stack": ["Jira", "Asana", "Advanced Excel", "Prompt Engineering"],
            "quests": [
                {
                    "id": "mission_ai_lead",
                    "title": "MISSION: AI PERFORMANCE ASCENSION",
                    "company": "Eklipse.gg",
                    "role": "Lead AI and Data Optimization",
                    "impact": "SUCCESS RATE 60% → 90%",
                    "summary": "Architected end-to-end AI operations and optimized iteration cycles through systematic benchmarking.",
                    "assets": ["Competitor Intel Data", "Signature: Reverse-Engineering Strategy", "Benchmark Framework"],
                    "dossier": [
                        "Identified AI performance gaps by reverse-engineering competitor outputs.",
                        "Directed multi-day technical benchmarking to influence strategic feature prioritization.",
                        "Established monitoring frameworks to align AI precision with business objectives.",
                        "Drastically reduced AI iteration cycles via systematic analytical audits."
                    ]
                },
                {
                    "id": "mission_pm",
                    "title": "MISSION: PRODUCT MARKET DOMINATION",
                    "company": "Eklipse.gg",
                    "role": "Project Manager & Market Strategy",
                    "impact": "SCALED TO 400+ DAILY SUBS",
                    "summary": "Synchronized AI capabilities with market signals to drive actionable product roadmaps.",
                    "assets": ["Sentiment Analysis Engine", "NRU Tracking Infrastructure", "GTM Strategic Data"],
                    "dossier": [
                        "Orchestrated market intelligence gathering via advanced web scraping techniques.",
                        "Engineered user sentiment analysis frameworks to guide marketing pivot decisions.",
                        "Bridged the execution gap between Product, Marketing, and AI engineering teams.",
                        "Developed internal KPI systems to evaluate real-time campaign effectiveness."
                    ]
                },
                {
                    "id": "mission_foundation",
                    "title": "MISSION: DATA INTEGRITY FOUNDATION",
                    "company": "PT. MAINGAMES",
                    "role": "AI and Data Optimization Staff",
                    "impact": "SYSTEM STABILITY +20%",
                    "summary": "Fortified AI scalability through rigorous data QA and dataset improvement cycles.",
                    "assets": ["Production-Grade Data Reliability", "Bounding Box Precision Mastery"],
                    "dossier": [
                        "Enhanced AI system stability by optimizing training dataset quality.",
                        "Managed labeling validation and dataset audits to minimize training noise.",
                        "Synthesized App Store feedback into continuous data improvement loops.",
                        "Maintained high-grade data reliability to support long-term AI scalability."
                    ]
                }
            ],
            "education": {
                "title": "ACADEMIC SIDE-QUEST",
                "school": "Universitas Gadjah Mada",
                "major": "Philosophy | GPA: 3.06",
                "desc": "Mastered the application of logic and epistemology in leadership and data management."
            }
        }
        return render_template('index.html', stats=stats)
    except Exception as e:
        return f"System Error: {str(e)}"

app.debug = True
