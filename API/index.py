from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Data dari CV kamu yang dikonversi ke format Game RPG
    stats = {
        "level": 3, # Berdasarkan 3 tahun pengalaman
        "hp": 999,
        "sp": 850,
        "exp_percent": 35,
        "persona_name": "LOGOS",
        "philosophy_perk": "Logical Reasoning & Ethics +50",
        "social_stats": [5, 4, 4, 3, 4] # Knowledge, Guts, Proficiency, Kindness, Charm
    }
    return render_template('index.html', stats=stats)

# Penting untuk Vercel
app.debug = True