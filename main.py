
#_______________________________________________________________


# from flask import Flask,render_template,redirect,url_for,request

# app=Flask(__name__)

# @app.route("/web")
# def webpage():
#     user=["sam","ram","karan","babu"]
#     get_name=request.args.get("input")
#     return render_template("child.html",get_data=get_name,send_user=user)
    

# @app.route("/web2/<name>")
# def webpage2(name):
#     return render_template("main.html",data=name)


# if __name__=="__main__":
#     app.run(debug=True)



#_______________________________________________________________
#Blue Print


# from flask import Flask
# from app1 import auth_bp
# from app2 import bp

# app=Flask(__name__)


# app.register_blueprint(auth_bp)
# app.register_blueprint(bp)


# if __name__=='__main__':
#     app.run(debug=True)


#____________________________________________________________________________


#form validation




from flask_wtf.csrf import CSRFProtect
from flask import Flask,render_template,request
from app1 import auth_bp
from app2 import bp
from app3 import app3
from app4 import app4
from app5 import app5


app=Flask(__name__)



app.secret_key = "your_secret_key"  # Required
csrf = CSRFProtect(app)


app.register_blueprint(auth_bp)
app.register_blueprint(bp)
app.register_blueprint(app3)
app.register_blueprint(app4)
app.register_blueprint(app5)



if __name__=='__main__':
    app.run(debug=True)








#____________________________________________________________________________






# main.py

# @app.route("/postinfo",methods=["POST"])
# def post_info(request):
#     if request.method == 'POST':
#         print(request.POST)  
#         return HttpResponse("Check console")

