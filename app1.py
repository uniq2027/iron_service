


from flask import Blueprint,render_template,request


auth_bp=Blueprint('auth',__name__,template_folder='templates')


@auth_bp.route('/')
def login():
    return render_template('login.html')




@auth_bp.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        return f"<h1>welcome {username}...</h1>"
    return "<h1>this is not method:post...</h1>"
    


