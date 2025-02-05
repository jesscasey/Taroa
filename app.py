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

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run()