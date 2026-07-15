from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Renders the template with all our UI sections and nav bars
    return render_template('index.html')

if __name__ == '__main__':
    # Boot server locally on port 5000
    app.run(debug=True, port=5000)