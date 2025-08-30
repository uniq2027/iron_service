from flask import Flask,Blueprint,render_template,request,flash

app3=Blueprint("form",__name__,template_folder='templates')


app3.secret_key = 'tamil_english_math'  # Required for flash messages

@app3.route("/postinfo",methods=["POST",'GET'])
def post_info():
    if request.method == 'POST':
        # print(request.form.get("password"))


        username=request.form.get("username","NAME") 
        password=request.form.get("password")
        email=request.form.get("email")
        confirm_password=request.form.get("confirmpass")



        # Strict access
        # username = request.form['username']  # will crash if missing
        # password=request.form['password']
        # email=request.form['email']
        # confirm_password=request.form['confirmpass']


        if not username or not password or not email or not confirm_password:
            data1="all fields are required"
            return render_template("user_info.html",flash1=data1)
        if len(username)<=3:
            flash("Invalid username or password", "success")
        if "@"not in email or "."not in email:
            return "invalid email format.."
        if password!=confirm_password:
            return "password do not match.."
        return f"welcome {username} ! you are register successfully..." 
        

    return render_template("user_info.html")




## **When to Use Which**

# | Method        | Use Case                                                                                               |
# | ------------- | ------------------------------------------------------------------------------------------------------ |
# | `.get('key')` | When the field **might not be present** and you want to avoid errors (common in optional form fields). |
# | `['key']`     | When the field is **required** and you want an error if it’s missing (forces validation).              |






### 🧠 Key Concepts

# | Concept                  | Description                                               |
# | ------------------------ | --------------------------------------------------------- |
# | `flash()`                | Stores a temporary message in the session                 |
# | `redirect()`             | Moves user to another route (where message will be shown) |
# | `get_flashed_messages()` | Displays the flash message in the HTML                    |
# | `secret_key`             | Required for sessions and flash to work                   |