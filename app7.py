
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_jwt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ----------------- User Model -----------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# ----------------- JWT Decorator -----------------
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]  # Bearer <token>

        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.filter_by(username=data["user"]).first()
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired!"}), 401
        except Exception:
            return jsonify({"message": "Token is invalid!"}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# ----------------- Register -----------------
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")


    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists!"}), 400

    hashed_pw = generate_password_hash(password, method="pbkdf2:sha256")
    new_user = User(username=username, password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"})


# ----------------- Login (Generate JWT) -----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials!"}), 401

    token = jwt.encode(
        {"user": user.username, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
        app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return jsonify({"token": token})

# ----------------- Protected Route -----------------
@app.route("/dashboard", methods=["GET"])
@token_required
def dashboard(current_user):
    return jsonify({"message": f"Welcome {current_user.username}, you are in the dashboard!"})

# ----------------- Run -----------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create DB tables
    app.run(debug=True)





# from flask import Flask, render_template, request, redirect, session, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# app.secret_key = "supersecretkey"

# # Database setup
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks9.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# # ------------------- MODELS -------------------
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)


# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Boolean, default=False)


# # ------------------- AUTH ROUTES -------------------
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = generate_password_hash(request.form['password'])
#         if User.query.filter_by(username=username).first():
#             flash("Username already exists!", "warning")
#             return redirect('/register')
#         new_user = User(username=username, password=password)
#         db.session.add(new_user)
#         db.session.commit()
#         flash("User registered successfully! Please login.", "success")
#         return redirect('/login')
#     return render_template('register.html')


# #/register===>GET==>if ==post==>false==>reder==>reg.html==>Ui 





# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()
#         if user and check_password_hash(user.password, password):
#             session['user_id'] = user.id
#             session['username'] = user.username
#             flash("Login successful!", "success")
#             return redirect('/display')
#         else:
#             flash("Invalid credentials", "danger")
#     return render_template('login.html')






# @app.route('/logout')
# def logout():
#     session.clear()
#     flash("Logged out successfully!", "info")
#     return redirect('/login')


# # ------------------- TASK ROUTES (SQLAlchemy code) -------------------

# # Display tasks
# @app.route('/display')
# def display_tasks():
#     if 'user_id' not in session:
#         return redirect('/login')
#     tasks = Task.query.all()
#     return render_template('sqlalchemy.html', received=tasks)


# # Add a new task
# @app.route('/add', methods=['POST'])
# def add_task():
#     if 'user_id' not in session:
#         return redirect('/login')
#     title = request.form['title']
#     new_task = Task(title=title, completed=False)
#     db.session.add(new_task)
#     db.session.commit()
#     flash("Task added successfully!", "success")
#     return redirect('/display')


# # Mark task as completed
# @app.route('/complete/<int:task_id>')
# def complete_task(task_id):
#     if 'user_id' not in session:
#         return redirect('/login')
#     task = Task.query.get(task_id)
#     if task:
#         task.completed = True
#         db.session.commit()
#         flash("Task marked as completed!", "info")
#     return redirect('/display')


# # Delete task
# @app.route('/delete/<int:task_id>')
# def delete_task(task_id):
#     if 'user_id' not in session:
#         return redirect('/login')
#     task = Task.query.get(task_id)
#     if task:
#         db.session.delete(task)
#         db.session.commit()
#         flash("Task deleted successfully!", "danger")
#     return redirect('/display')


# # ------------------- MAIN -------------------
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)



# from flask import Flask, jsonify

# app = Flask(__name__)

# # --- Decorator without wraps ---
# def token_required(f):
#     def decorated(*args, **kwargs):
#         # pretend token check
#         return f(*args, **kwargs)
#     return decorated

# @app.route("/hello")
# @token_required
# def hello():
#     return jsonify({"message": "Hello User!"})

# @app.route("/bye")
# @token_required
# def bye():
#     return jsonify({"message": "Goodbye User!"})

# if __name__ == "__main__":
#     app.run(debug=True)




# from flask import Flask, jsonify, request
# from functools import wraps

# app = Flask(__name__)

# # --- Decorator with wraps ---
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         # pretend token check
#         return f(*args, **kwargs)
#     return decorated

# @app.route("/hello")
# @token_required
# def hello():
#     return jsonify({"message": "Hello User!"})

# @app.route("/bye")
# @token_required
# def bye():
#     return jsonify({"message": "Goodbye User!"})

# if __name__ == "__main__":
#     app.run(debug=True)
