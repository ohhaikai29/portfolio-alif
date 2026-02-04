from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    stats = {
        "level": "03",
        "rank": "STRATEGIC PRODUCT & AI ARCHITECT",
        "exp_years": "May 2023 - Sept 2025",
        "accuracy_buff": "90%", 
        "team_boost": "80%",
        "persona": "LOGOS",
        "passive": "Epistemic Sovereign: Translating raw market signals into high-value strategic roadmaps.",
        "social_stats": [5, 5, 5, 5, 4], 
        "contact": {
            "email": "alifoctrio@gmail.com",
            "phone": "+62 813-3670-0117",
            "linkedin": "linkedin.com/in/alifoctrio"
        },
        "inventory": ["Competitor Reverse-Engineering", "Technical Benchmarking", "Product Strategy", "Sentiment Frameworks", "GTM Support"],
        "quests": [
            {
                "id": "mission_benchmark",
                "title": "MISSION: AI TECHNICAL BENCHMARK & COMPETITIVE ANALYSIS",
                "company": "Eklipse.gg",
                "role": "Strategic AI Intelligence",
                "impact": "60% → 90% CLIP DETECTION ACCURACY",
                "intel": "Strengthened AI competitiveness through systematic benchmarking and technical analysis.",
                "dossier": [
                    "Improved AI clip detection accuracy through rigorous competitor benchmarking.",
                    "CONDUCTED REVERSE-ENGINEERING of competitor features to identify technical gaps.",
                    "Delivered insights that directly influenced AI feature prioritization and roadmap decisions.",
                    "Reduced iteration cycles by identifying high-impact improvements early in development.",
                    "Maintained competitive intelligence documentation for ongoing evaluation."
                ]
            },
            {
                "id": "mission_lead_ai",
                "title": "MISSION: LEAD AI & DATA OPTIMIZATION",
                "company": "Eklipse.gg",
                "role": "Team Lead & Ops Optimization",
                "impact": "~80% TEAM EFFICIENCY BOOST",
                "intel": "Owned AI execution to ensure research output translated into scalable, production-ready systems.",
                "dossier": [
                    "Increased operational success rate by improving execution workflows and monitoring.",
                    "Boosted AI team efficiency by ~80% through bottleneck resolution.",
                    "Translated R&D experiments into production pipelines with measurable product impact.",
                    "Built AI performance monitoring frameworks to track quality, reliability, and delivery.",
                    "Collaborated with Engineering teams to align AI output with business needs."
                ]
            },
            {
                "id": "mission_pm",
                "title": "MISSION: PROJECT MANAGER & MARKET STRATEGY",
                "company": "Eklipse.gg",
                "role": "PM & Strategic Lead (Hype Games)",
                "impact": "SCALED TO 400+ DAILY SUBMISSIONS",
                "intel": "Led strategic product initiatives by translating AI capabilities into data-driven decisions.",
                "dossier": [
                    "Led market intelligence using web scraping and competitor research to find opportunities.",
                    "Built user sentiment analysis framework to support product direction and marketing pivots.",
                    "Developed internal KPI tracking systems (NRU & 400+ daily submissions).",
                    "Acted as a strategic bridge between Product, Marketing, and AI teams."
                ]
            },
            {
                "id": "mission_maingames",
                "title": "MISSION: DATA QUALITY FOUNDATION",
                "company": "PT. MAINGAMES",
                "role": "AI and Data Optimization Staff",
                "impact": "SYSTEM STABILITY +20%",
                "intel": "Fortified AI scalability through rigorous data preparation and continuous dataset audits.",
                "dossier": [
                    "Improved AI system stability through training dataset quality enhancement.",
                    "Performed labeling validation, bounding box correction, and dataset audits.",
                    "Integrated user feedback from App Store reviews into continuous improvement cycles.",
                    "Maintained production-grade data reliability for long-term scalability."
                ]
            }
        ],
        "education": {
            "school": "Universitas Gadjah Mada",
            "major": "Philosophy | GPA: 3.06",
            "focus": "Applied logic, ethics, and epistemology in decision-making and data management."
        }
    }
    return render_template('index.html', stats=stats)
