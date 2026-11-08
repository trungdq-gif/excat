from flask import Flask, jsonify, render_template

app = Flask(__name__)

# The HTML, CSS, and JavaScript interface embedded as a string

# Route for the Main Page
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/room/<int:number>')
def room(number):
    name = "Host"
    return render_template("roomWait.html", roomNumber=number, GuessName=name)

# Route for the API Data ping
@app.route('/api/ping')
def ping():
    return jsonify({"reply": "Pong! Connection to your cloud server works."})

if __name__ == "__main__":
    app.run(debug=1)