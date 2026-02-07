from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "SUPREME PRODUCT & AI ARCHITECT",
        "accuracy": "90%", 
        "efficiency": "80%",
        "persona": "LOGOS",
        "inventory": [
            {"name": "Jira", "desc": "Used for Agile sprint planning & tracking AI iteration cycles between R&D and Production."},
            {"name": "Asana", "desc": "Coordinated cross-functional tasks across Product, Marketing, and Engineering teams."},
            {"name": "Web Scraping", "desc": "Automated competitor data extraction to identify market gaps and benchmark AI accuracy."},
            {"name": "Prompt Eng.", "desc": "Optimized LLM outputs for sentiment analysis frameworks, increasing success rates by 30%."},
            {"name": "Advanced Excel", "desc": "Built complex KPI dashboards (NRU & Daily Submissions) for real-time campaign audits."}
        ],
        "skills": [
            {"n": "PRODUCT STRATEGY", "v": 95},
            {"n": "AI OPERATIONS", "v": 90},
            {"n": "BENCHMARKING", "v": 92}
        ],
        "quests": [
            {
                "id": "q1", 
                "title": "MISSION: PM & MARKET STRATEGY", 
                "impact": "SCALED TO 400+ DAILY SUBS", "rank": "S",
                "intel": "Led product initiatives by translating AI capabilities into data-driven market decisions. Acted as a strategic bridge between Product, Marketing, and AI teams.",
                "loot": ["KPI Tracking Mastery", "Product-Market Fit Insight", "Sentiment Analysis Framework"]
            },
            {
                "id": "q2", 
                "title": "MISSION: LEAD AI & DATA OPS", 
                "impact": "80% EFFICIENCY BOOST", "rank": "S",
                "intel": "Translated R&D experiments into production pipelines and optimized execution workflows through bottleneck resolution.",
                "loot": ["Team Efficiency Perk", "Process Optimization Blueprint", "Ops Scaling Mastery"]
            },
            {
                "id": "q3", 
                "title": "MISSION: AI TECH BENCHMARK", 
                "impact": "90% ACCURACY", "rank": "A+",
                "intel": "Strengthened AI competitiveness through systematic benchmarking and competitor reverse-engineering of features.",
                "loot": ["Competitor Intel Dossier", "Accuracy Buff: +30%", "Strategic Benchmarking"]
            },
            {
                "id": "q4", 
                "title": "MISSION: DATA QUALITY (FACEBOOK GAMING)", 
                "impact": "STABILITY +20%", "rank": "B",
                "intel": "Fortified AI scalability through rigorous labeling validation, dataset audits, and monitoring Facebook Gaming content performance.",
                "loot": ["Data Reliability Buff", "QA Precision Skill", "Creator Content Analytics"]
            }
        ],
        "contact": {"email": "alifoctrio@gmail.com", "phone": "+62 813-3670-0117"}
    }
    return render_template('index.html', stats=stats)
