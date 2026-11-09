from flask import Flask, jsonify, render_template, url_for, request, redirect, make_response
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, room, username):
        self.id = user_id  # Flask-Login explicitly expects 'id'
        self.username = username
        self.roomnumber = room

  
app = Flask(__name__)
app.secret_key = "Hmm,not here"
players = 0

login_manager = LoginManager()
login_manager.init_app(app)

users_db = {0: User(0,0,"Dev_User")}

# Route for the Main Page
@app.route('/')
def index():
    return render_template("home.html")

@login_manager.user_loader
def load_user(user_id):
    # Flask-Login uses this to fetch your user object via the session ID
    return users_db.get(int(user_id))

# Route for the API Data ping
@app.route('/api/ping')
def ping():
    return jsonify({"reply": "Pong! Connection to your cloud server works."})

@app.route('/login',methods = ['POST', 'GET'])
def login():
    name = "Host"
    if request.method == 'POST':
        username = request.form['nm']
        room = request.form['rn']
        global players
        players += 1
        
        user = users_db[players] = User(players, room, username) 
    
        # 2. Tell Flask-Login to set this user's ID session
        login_user(user) 

        
        return redirect(url_for('room'))
    else:
        user = request.args.get('nm')
        return redirect(url_for('room',number = "Unknown", name = "Unknown"))


@app.route('/room')
@login_required
def room():
    cookie = ""
    return render_template("roomWait.html", roomNumber=current_user.roomnumber, guessName=current_user.username, ck = str([user.username for user in users_db.values()]))

if __name__ == "__main__":
    app.run(debug=1)

