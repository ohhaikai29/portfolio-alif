from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "STRATEGIC AI OPERATIONS LEAD",
        "exp_years": "2022 - Present",
        "kpi": "90%", 
        "opt": "85%",
        "persona_name": "LOGOS",
        "lore": "Strategic Project Manager and AI Operations Specialist with proven experience driving AI product execution and data-driven decision making in gaming platforms.",
        "social_stats": [5, 5, 4, 4, 5], 
        "contact": {
            "email": "alifoctrio@gmail.com",
            "phone": "+62 813-3670-0117",
            "linkedin": "linkedin.com/in/alifoctrio"
        },
        "inventory": [
            "Project Management", "Business Analysis", "Roadmap Planning", 
            "Stakeholder Management", "Go-to-Market Support", "Web Scraping"
        ],
        "tech_stack": ["Jira", "Asana", "Trello", "Advanced Excel", "Prompt Engineering"],
        "quests": [
            {
                "id": "eklipse_pm",
                "title": "OP: HYPE GAMES STRATEGY",
                "company": "Eklipse.gg",
                "role": "Project Manager & Market Strategy",
                "achievement": "High-Potential Product Identification",
                "loot": ["User Sentiment Analysis Framework", "KPI Tracking (NRU & 400+ daily)", "Strategic Marketing Pivots"],
                "details": [
                    "Translating AI capabilities into actionable product decisions.",
                    "Market intelligence & competitor analysis via web scraping.",
                    "Bridging Product, Marketing, and AI teams for execution alignment.",
                    "Evaluating product-market fit through campaign effectiveness data."
                ]
            },
            {
                "id": "eklipse_ai",
                "title": "OP: AI BENCHMARKING LEAD",
                "company": "Eklipse.gg",
                "role": "Lead AI and Data Optimization",
                "achievement": "Success Rate 60% → 90%",
                "loot": ["Multi-day AI Technical Benchmarking", "Reverse-Engineering Intel", "Iterative Cycle Reduction"],
                "details": [
                    "Led end-to-end AI operations and performance analysis.",
                    "Reverse-engineered competitor outputs to influence feature prioritization.",
                    "Built reporting frameworks for Business & Product stakeholders.",
                    "Systematic benchmark analysis to reduce iteration cycles."
                ]
            },
            {
                "id": "maingames",
                "title": "OP: DATA RELIABILITY",
                "company": "PT. MAINGAMES",
                "role": "AI and Data Optimization Staff",
                "achievement": "System Stability +20%",
                "loot": ["Production-Grade Data Scalability", "Dataset Quality Assurance", "User Feedback Integration"],
                "details": [
                    "High-quality data preparation for AI scalability.",
                    "Labeling validation, bounding box correction, and dataset audits.",
                    "Monitored Facebook Gaming creator content performance.",
                    "Continuous data improvement via App Store & Social Media feedback."
                ]
            }
        ],
        "education": {
            "school": "Universitas Gadjah Mada",
            "major": "Philosophy | GPA: 3.06",
            "focus": "Applied ethics, logic, and philosophy of science in decision-making."
        }
    }
    return render_template('index.html', stats=stats)
