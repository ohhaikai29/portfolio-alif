from flask import Flask, render_template

# Flask otomatis nyari folder 'templates' di lokasi yang sama dengan index.py
app = Flask(__name__)

@app.route('/')
def home():
    stats = {
        "level": 3,
        "hp": 999,
        "sp": 850,
        "exp_percent": 35,
        "persona_name": "LOGOS",
        "philosophy_perk": "Logical Reasoning +50"
    }
    return render_template('index.html', stats=stats)

# Ini wajib supaya Vercel bisa nangkep aplikasinya
app.debug = True
