from flask import Flask, render_template

app = Flask(__name__)

favShows = ["Westworld", "Arcane", "Shadow and Bone", "Euphoria", "Pui Pui Molcar"]

@app.route('/')
def index():
    return render_template("index.html", len = len(favShows), favShows = favShows)

app.run(use_reloader = True, debug = True)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0