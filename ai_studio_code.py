from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Data Persona Anda
    stats = {
        "level": 3,
        "hp": 999,
        "sp": 850,
        "exp_percent": 35,
        "persona_name": "LOGOS",
        "philosophy_perk": "Logical Reasoning +50"
    }
    return render_template('index.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)