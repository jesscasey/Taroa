from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main/home.html')

@app.route("/directory")
def directory():
    return render_template('tarot/directory.html')

@app.route("/reading")
def reading():
    return render_template('tarot/reading.html')

if __name__ == '__main__':
    app.run()