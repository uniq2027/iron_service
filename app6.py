# from flask import Flask,render_template,request,redirect,url_for

# import sqlite3

# app=Flask(__name__)


# DATABASE='mydatabase1.db'


# def create_table():
#     connection=sqlite3.connect(DATABASE)
#     cursor=connection.cursor()
#     cursor.execute(
#         "create table if not exists books56(id integer  primary key autoincrement,title varchar(100) not null,author varchar(100) not null)"
#     )
#     connection.commit()
#     connection.close()

# @app.route("/db_creation")
# def index():
#     create_table()
#     connection=sqlite3.connect(DATABASE)
#     cursor=connection.cursor()
#     cursor.execute(
#         "select*from books56"
#     )
#     receive_books=cursor.fetchall()
#     connection.close()
#     return render_template("db.html",get_books=receive_books)


# @app.route("/add",  methods=["POST"])
# def add_book():
#     title = request.form['title']
#     author = request.form['author']

#     connection = sqlite3.connect(DATABASE)
#     cursor = connection.cursor()
#     cursor.execute('INSERT INTO books56 (title, author) VALUES (?, ?)', (title, author))
#     connection.commit()
#     connection.close()
#     return redirect(url_for('index'))



# @app.route('/delete/<int:id>')
# def delete_book(id):
#     print(id)
#     connection = sqlite3.connect(DATABASE)
#     cursor = connection.cursor()
#     cursor.execute('DELETE FROM books56 WHERE id = ?', (id,))
#     connection.commit()
#     connection.close()
#     return redirect(url_for('index'))





# if __name__=="__main__":
#     app.run(debug=True)



# ____________________________________________________________

# pip install Flask-MySQLdb



# from flask import Flask, render_template, request, redirect, url_for
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# # # Database Config
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '1234'
# app.config['MYSQL_DB'] = 'climate'

# db = MySQL(app)

# # # Create table if not exists
# def create_table():
#     cursor = db.connection.cursor()
#     cursor.execute(
#         '''CREATE TABLE IF NOT EXISTS collage23(
#             id INT PRIMARY KEY AUTO_INCREMENT,
#             username VARCHAR(50),
#             password VARCHAR(200))'''
#     )
#     cursor.close()



# # `db` is probably your **Flask-MySQLdb instance**.
# # * `.connection.cursor()` creates a **cursor object**.
# # * **Cursor** is used to execute SQL queries and fetch data from the database.




# # # -------------------- CREATE --------------------
# @app.route("/add", methods=["GET", "POST"])
# def add_user():
#     create_table()
#     if request.method == "POST":
#         username = request.form['username']
#         password = request.form['password']
#         cursor = db.connection.cursor()
#         cursor.execute("INSERT INTO collage23(username, password) VALUES (%s, %s)", (username, password))
#         db.connection.commit()
#         cursor.close()
#         return redirect(url_for("index"))
#     return render_template("add.html")

# # # -------------------- READ --------------------
# @app.route("/")
# def index():
#     create_table()
#     cur = db.connection.cursor()
#     cur.execute("SELECT * FROM collage23")
#     users = cur.fetchall()
#     cur.close()
#     return render_template("index.html", users=users)

# # -------------------- UPDATE --------------------
# @app.route("/update/<int:id>", methods=["GET", "POST"])
# def update_user(id):
#     cur = db.connection.cursor()
#     if request.method == "POST":
#         username = request.form['username']
#         password = request.form['password']
#         cur.execute("UPDATE collage23 SET username=%s, password=%s WHERE id=%s",
#                     (username, password, id))
#         db.connection.commit()
#         cur.close()
#         return redirect(url_for("index"))
    
    
#     cur.execute("SELECT * FROM collage23 WHERE id=%s", (id,))
#     user = cur.fetchone()
#     cur.close()
#     return render_template("update.html", user=user)


# # -------------------- DELETE --------------------
# @app.route("/delete/<int:id>")
# def delete_user(id):
#     cur = db.connection.cursor()
#     cur.execute("DELETE FROM collage23 WHERE id=%s", (id,))
#     db.connection.commit()
#     cur.close()
#     return redirect(url_for("index"))

# if __name__ == "__main__":
#     app.run(debug=True)





# ____________________________________________________________


# pip install Flask SQLAlchemy pymysql
# pip install sqlalchemy
# pip install flask-sqlalchemy



# from flask import Flask, render_template, request, redirect 
# from flask_sqlalchemy import SQLAlchemy



# app = Flask(__name__)


# # app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///tasks8.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/country'



# db=SQLAlchemy(app)


# class Work(db.Model):
#      id=db.Column(db.Integer,primary_key=True)
#      title=db.Column(db.String(200),nullable=False)
#      completed=db.Column(db.Boolean,default=False)



# #CRUD



# @app.route("/display")
# def index():
#      data=Work.query.all()
    
#      return render_template("sqlalchemy.html",received=data)

# @app.route('/add_task', methods=['POST'])
# def add_task():
     
#      form_title= request.form['topic']  #get the data from form
#      new_task =Work(title=form_title)  #create the object for pass the data to table
#      db.session.add(new_task)          #pass the  data into table
#      db.session.commit()               #save the data or table
#      return redirect('/display')

# @app.route('/complete_task/<int:id>')
# def update(id):
#      data=Work.query.get(id)
#     #  data==><([id=5,title="going to school",complete=0])>
#      data.completed=True
#      db.session.commit()
#      return redirect("/display")

# @app.route("/delete_task/<int:task_id>")
# def delete(task_id):
#     data=Work.query.get(task_id)
#     db.session.delete(data)
#     db.session.commit()
#     return redirect("/display")

     
# if __name__ == '__main__':
#      with app.app_context():
#          db.create_all()
#      app.run(debug=True)



# from flask import Flask, render_template, request, redirect 
# from flask_sqlalchemy import SQLAlchemy



# SQLAlchemy==module or library
# SQLAlchemy()
# column()
# all()
# add()
# commit()
# get()
# delete()
# create_all()

# app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks7.db'  # SQLite database file
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/country'



# db = SQLAlchemy(app)
# print(db)



# # Define the Task model 
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Boolean, default=False)


# #CRUD


# @app.route('/display')
# def index():
#     data=Task.query.all()
#     return render_template('sqlalchemy.html',received=data)



# @app.route('/add_task', methods=['POST'])
# def add_task():
#     form_title= request.form['topic']  #get the data from form
#     new_task =Task(title=form_title)  #create the object for pass the data to table 
#     db.session.add(new_task)          #pass the  data into table
#     db.session.commit()               #save the data or table
#     return redirect('/display')




# @app.route("/complete_task/<int:task_id>")
# def update(task_id):
#     data=Task.query.get(task_id)
#     data.completed=True
#     db.session.commit()
#     return redirect("/display")



# @app.route("/delete_task/<int:task_id>")
# def delete(task_id):
#     data=Task.query.get(task_id)
#     db.session.delete(data)
#     db.session.commit()
#     return redirect("/display")



# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)

#_________________________________________________________________________________________





# from flask import Flask, render_template, request, redirect, session, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash



# app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # ---------- User Model ----------
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)  # hashed password



# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method=="POST":
#         get_username = request.form.get("username")
#         get_password = request.form.get("password")
        
#         if User.query.filter_by(username=get_username).first():
#             return "username already exists!" 
             
#         hashed_password=generate_password_hash(get_password)
#         new_user=User(username=get_username,password=hashed_password)
       
#         db.session.add(new_user)
#         db.session.commit()
#         return f"user {get_username} register successfully!!"

#     return render_template("register.html")








# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         user = User.query.filter_by(username=username).first()
#         if not user:
#             # Redirect to registration if user does not exist
            
#             return redirect(url_for("register"))
#         if not check_password_hash(user.password, password):
#             return "Invalid password!"
        
#         return f"""
#         <form id='dashboardForm' method='POST' action='/dashboard'>
#             <input type='hidden' name='username' value='{username}'>
#             <input type='hidden' name='password' value='{password}'>
#         </form>
#         <script>document.getElementById('dashboardForm').submit();</script>
#         """
#     return render_template("login.html")



# @app.route("/dashboard", methods=["GET", "POST"])
# def dashboard():
#      if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#      else:
#         # No credentials, redirect to login
#         return redirect(url_for("register"))

#      user = User.query.filter_by(username=username).first()
#      if not user or not check_password_hash(user.password, password):
#         return redirect(url_for("login"))

#      return render_template("dashboard.html",name=username)













# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
























# from flask import Flask, request, make_response

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return """
#         <h2>Cookie Demo</h2>
#         <a href="/set_cookie">Set Cookie</a><br>
#         <a href="/get_cookie">Read Cookie</a><br>
#         <a href="/delete_cookie">Delete Cookie</a>
#     """


# @app.route("/demo")
# def demo():
#     response = make_response()
#     response.set_cookie("username", "poovarasan", max_age=60)
#     response.headers["X-Test"] = "HelloHeader"
#     response.status_code = 404
#     return response



# # 1️⃣ Set cookie
# @app.route('/set_cookie')
# def set_cookie():
#     response = make_response("Cookie has been set! Check response headers.")
#     response.set_cookie('username', 'Alice', max_age=60)  # expires in 60 sec
#     return response

# # 2️⃣ Read cookie
# @app.route('/get_cookie')
# def get_cookie():
#     username = request.cookies.get('username')
#     if username:
#         return f"Hello, {username}! (Check request headers for the cookie)"
#     return "No cookie found. Please set it first."

# # 3️⃣ Delete cookie
# @app.route('/delete_cookie')
# def delete_cookie():
#     response = make_response("Cookie has been deleted! Check response headers.")
#     response.delete_cookie('username')
#     return response

# if __name__ == "__main__":
#     app.run(debug=True)




# from flask import Flask, session, redirect, url_for, request

# app = Flask(__name__)
# app.secret_key = "supersecretkey"  # Required to use sessions

# @app.route('/set_session')
# def set_session():
#     session['username'] = 'Alice'
#     return "Session set for Alice!"

# @app.route('/get_session')
# def get_session():
#     username = session.get('username')
#     if username:
#         return f"Hello, {username}!"
#     return "No session found."

# @app.route('/clear_session')
# def clear_session():
#     session.clear()
#     return "Session cleared!"




# if __name__ == "__main__":
#     app.run(debug=True)


#___________________________________________________________________________________




# from flask import Flask, render_template, request, redirect, session, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)

# # Secret key for session cookies
# app.secret_key = "supersecretkey"

# # Database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks9.db'
# db = SQLAlchemy(app)

# # User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)

# # Task model
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Boolean, default=False)


# ## 🔹 Step 2: Authentication Routes

# ### Register


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = generate_password_hash(request.form['password'])  # hash password
#         new_user = User(username=username, password=password)
#         db.session.add(new_user)
#         db.session.commit()
#         flash("User registered successfully! Please login.", "success")
#         return redirect('/login')
#     return render_template('register.html')

# ### Login


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()
#         if user and check_password_hash(user.password, password):
#             session['user_id'] = user.id   # store user id in session
#             session['username'] = user.username
#             flash("Login successful!", "success")
#             return redirect('/display')
#         else:
#             flash("Invalid credentials", "danger")
#     return render_template('login.html')


# ### Logout

# @app.route('/logout')
# def logout():
#     session.clear()
#     flash("Logged out successfully!", "info")
#     return redirect('/login')


# ## 🔹 Step 3: Protect Routes (Authorization)



# @app.route('/display')
# def index():
#     if 'user_id' not in session:
#         return redirect('/login')
#     data = Task.query.all()
#     return render_template('sqlalchemy.html', received=data)




# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)



#_______________________________________________________________________________________


# #____________________________________________________________________________________


# from flask import Flask, request, redirect, url_for, render_template
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)

# # SQLite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # ---------- User Model ----------
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)  # hashed password

# # ---------- Routes ----------

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         if User.query.filter_by(username=username).first():
#             return "Username already exists!"
#         hashed_password = generate_password_hash(password)
#         new_user = User(username=username, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
#         return f"User {username} registered successfully!"
#     return render_template("register.html")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         user = User.query.filter_by(username=username).first()
#         if not user:
#             # Redirect to registration if user does not exist
#             return redirect(url_for("register"))
#         if not check_password_hash(user.password, password):
#             return "Invalid password!"
#         # Send credentials to dashboard via POST form
#         return f"""
#         <form id='dashboardForm' method='POST' action='/dashboard'>
#             <input type='hidden' name='username' value='{username}'>
#             <input type='hidden' name='password' value='{password}'>
#         </form>
#         <script>document.getElementById('dashboardForm').submit();</script>
#         """
#     return render_template("login.html")

# @app.route("/dashboard", methods=["GET", "POST"])
# def dashboard():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#     else:
#         # No credentials, redirect to login
#         return redirect(url_for("login"))

#     user = User.query.filter_by(username=username).first()
#     if not user or not check_password_hash(user.password, password):
#         return redirect(url_for("login"))

#     return render_template("dashboard.html",name=username)


# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)






from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.secret_key = "supersecretkey"

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks9.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ------------------- MODELS -------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)


# ------------------- AUTH ROUTES -------------------


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash("Login successful!", "success")
            return redirect('/display')
        else:
            flash("Invalid credentials", "danger")
    return render_template('login.html')


# ------------------- AUTH ROUTES -------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if User.query.filter_by(username=username).first():
            flash("Username already exists!", "warning")
            return redirect('/register')
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("User registered successfully! Please login.", "success")
        return redirect('/login')
    return render_template('register.html')




@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully!", "info")
    return redirect('/login')    

# ------------------- TASK ROUTES (SQLAlchemy code) -------------------

# Display tasks

@app.route('/display')
def display_tasks():
    if 'user_id' not in session:
        return redirect('/login')
    tasks = Task.query.all()
    return render_template('sqlalchemy.html', received=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        return redirect('/login')
    title = request.form['title']
    new_task = Task(title=title, completed=False)
    db.session.add(new_task)
    db.session.commit()
    flash("Task added successfully!", "success")
    return redirect('/display')



@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 'user_id' not in session:
        return redirect('/login')
    task = Task.query.get(task_id)
    if task:
        task.completed = True
        db.session.commit()
        flash("Task marked as completed!", "info")
    return redirect('/display')


# Delete task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect('/login')
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted successfully!", "danger")
    return redirect('/display')