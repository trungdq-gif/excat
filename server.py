from flask import Flask, jsonify

app = Flask(__name__)

# The HTML, CSS, and JavaScript interface embedded as a string
HTML_INTERFACE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud Hosted Web App</title>
    <style>
        body { font-family: system-ui, sans-serif; background: #f4f4f9; padding: 2rem; text-align: center; }
        .card { background: white; padding: 2rem; border-radius: 8px; max-width: 400px; margin: auto; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        button { background: #2563eb; color: white; border: none; padding: 0.6rem 1.2rem; border-radius: 6px; cursor: pointer; font-size: 1rem; font-weight: 500; }
        button:hover { background: #1d4ed8; }
        #response { margin-top: 1.5rem; font-weight: bold; color: #059669; min-height: 24px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Cloud-Hosted Web App</h2>
        <p>This app is running live on PythonAnywhere cloud servers!</p>
        <button onclick="sendPing()">Ping Backend</button>
        <div id="response"></div>
    </div>

    <script>
        async function sendPing() {
            try {
                const res = await fetch('/api/ping');
                const data = await res.json();
                document.getElementById('response').innerText = data.reply;
            } catch (err) {
                document.getElementById('response').innerText = "Error connecting to backend.";
            }
        }
    </script>
</body>
</html>
"""

# Route for the Main Page
@app.route('/')
def index():
    return HTML_INTERFACE

# Route for the API Data ping
@app.route('/api/ping')
def ping():
    return jsonify({"reply": "Pong! Connection to your cloud server works."})
