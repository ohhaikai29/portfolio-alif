from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "CERTIFIED PRODUCT ARCHITECT",
        "accuracy": "90%", 
        "efficiency": "80%",
        "persona": "LOGOS",
        "inventory": [
            {
                "id": "IBM",
                "name": "IBM Project Mgmt.", 
                "desc": "Professional Certification: Introduction to Project Management. ID: QXV93T9APC6A", 
                "type": "LEGENDARY",
                "verify": "https://coursera.org/verify/QXV93T9APC6A",
                "img": "/static/ibm-cert.jpg"
            },
            {"id": "Jira", "name": "Jira", "desc": "Agile sprint planning & AI iteration tracking.", "type": "GEAR"},
            {"id": "Asana", "name": "Asana", "desc": "Cross-functional task orchestration.", "type": "GEAR"},
            {"id": "WebScraping", "name": "Web Scraping", "desc": "Automated competitor intel extraction.", "type": "SKILL"},
            {"id": "PromptEng", "name": "Prompt Eng.", "desc": "Optimizing LLM outputs for product logic.", "type": "SKILL"}
        ],
        "skills": [
            {"n": "STRATEGY", "v": 98},
            {"n": "AI OPERATIONS", "v": 90},
            {"n": "BENCHMARKING", "v": 92}
        ],
        "quests": [
            {
                "id": "q1", "title": "Q1: PM & MARKET STRATEGY", "impact": "SCALED TO 400+ DAILY SUBS", "rank": "S",
                "intel": "Led product initiatives by translating AI capabilities into data-driven decisions. Bridged Marketing and AI teams.",
                "loot": ["KPI Mastery", "Product-Market Fit"]
            },
            {
                "id": "q2", "title": "Q2: LEAD AI & DATA OPS", "impact": "80% EFFICIENCY BOOST", "rank": "S",
                "intel": "Optimized execution workflows and resolved bottlenecks for production-ready AI systems.",
                "loot": ["Ops Scaling", "Process Optimization"]
            },
            {
                "id": "q3", "title": "Q3: AI TECH BENCHMARK", "impact": "90% ACCURACY", "rank": "A+",
                "intel": "Strengthened AI competitiveness through multi-day systematic benchmarking and reverse-engineering.",
                "loot": ["Competitor Intel", "Reverse-Engineering"]
            },
            {
                "id": "q4", "title": "Q4: DATA QUALITY (FB GAMING)", "impact": "STABILITY +20%", "rank": "B",
                "intel": "Fortified AI scalability through FB Gaming content monitoring and dataset quality assurance.",
                "loot": ["QA Skill", "Data Reliability"]
            }
        ],
        "contact": {"email": "alifoctrio@gmail.com", "phone": "+62 813-3670-0117"}
    }
    return render_template('index.html', stats=stats)
