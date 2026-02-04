from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "SENIOR AI OPERATIONS LEAD",
        "exp_years": "Aug 2022 - Present",
        "kpi": "90%", 
        "opt": "85%",
        "persona_name": "LOGOS",
        "philosophy_perk": "Logic, Ethics, & Epistemology in Decision Making",
        "social_stats": [5, 5, 4, 4, 5], # PM, AI Ops, Analysis, Stakeholder, Strategy
        "contact": {
            "email": "alifoctrio@gmail.com",
            "phone": "+62 813-3670-0117",
            "linkedin": "linkedin.com/in/alifoctrio"
        },
        "inventory": [
            "Jira", "Asana", "Trello", "Advanced Excel", "Web Scraping", "Prompt Engineering"
        ],
        "quests": [
            {
                "id": "eklipse_pm",
                "title": "OP: HYPE GAMES STRATEGY",
                "role": "Project Manager & Market Strategy",
                "achievement": "Market Intelligence & Product-Market Fit",
                "how": "Translating AI capabilities, market signals, and user insights into actionable product decisions.",
                "loot": ["User Sentiment Framework", "KPI Tracking System (NRU & 400+ Submissions)", "Market Intelligence Data"],
                "details": [
                    "Conducted market intelligence through web scraping and community insights.",
                    "Designed and implemented user sentiment analysis frameworks for marketing pivots.",
                    "Developed internal KPI tracking systems for 400+ daily submissions.",
                    "Acted as a strategic bridge between Product, Marketing, and AI teams."
                ]
            },
            {
                "id": "eklipse_ai",
                "title": "OP: AI OPTIMIZATION LEAD",
                "role": "Lead AI and Data Optimization",
                "achievement": "AI Success Rate: 60% → 90%",
                "how": "Reverse-engineering competitor outputs and multi-day technical benchmarking to influence feature prioritization.",
                "loot": ["AI Performance Monitoring Framework", "Systematic Benchmark Analysis", "Optimized Iteration Cycles"],
                "details": [
                    "Led end-to-end AI operations and multi-day technical benchmarking.",
                    "Identified gaps by reverse-engineering competitor outputs.",
                    "Built monitoring frameworks to align AI results with business stakeholders.",
                    "Reduced AI iteration cycles through systematic benchmark analysis."
                ]
            },
            {
                "id": "maingames",
                "title": "OP: DATA SCALABILITY",
                "role": "AI and Data Optimization Staff",
                "achievement": "System Stability Boost: +20%",
                "how": "Training dataset quality enhancement and large-scale data QA.",
                "loot": ["Clean Training Datasets", "Bounding Box Precision", "User Feedback Loop"],
                "details": [
                    "Supported AI performance through high-quality data preparation.",
                    "Performed labeling validation, bounding box correction, and dataset audits.",
                    "Integrated App Store reviews and social media feedback into data cycles.",
                    "Maintained production-grade data reliability for long-term scalability."
                ]
            }
        ],
        "education": {
            "school": "Universitas Gadjah Mada",
            "major": "Philosophy | GPA: 3.06",
            "focus": "Ethics, Logic, & Philosophy of Science in Data Management."
        }
    }
    return render_template('index.html', stats=stats)
