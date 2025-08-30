
# from flask import Flask, render_template, request, redirect ,Blueprint
# from flask_mail import Mail, Message



# # # mail()
# # # message()
# # # sent()




# app5=Blueprint("email",__name__,template_folder='templates')




# @app5.route("/send",methods=['GET','POST'])
# def sendmail():
#     if request.method=="POST":
#         from_email=request.form.get("fromemail")
#         receiver=request.form.get("toemail")
#         body=request.form.get("body")
#         msg=Message('subject',sender=from_email ,recipients=[receiver])
#         msg.body = body
#         mail.send(msg)

#         return "mail send...!1"

    
#     return render_template("email.html")
   

#_________________________________________________________________________



from flask import Flask, render_template, request, redirect, Blueprint, flash, url_for
from flask_mail import Mail, Message
from flask_wtf import CSRFProtect


# # mail()
# # message()
# # sent()



app = Flask(__name__)



# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kingpoovarasan49@gmail.com'   # replace with your email
app.config['MAIL_PASSWORD'] = 'yqkacjtnuvjirdfs'   # use App Password if Gmail
app.config['MAIL_DEFAULT_SENDER'] = 'poovarasanuniq@gmail.com'

mail = Mail(app)

# Create Blueprint
app5 = Blueprint("email", __name__, template_folder="templates")

@app5.route("/sendemail", methods=['GET', 'POST'])
def sendmail():
  
    if request.method == "POST":
        from_email = request.form.get("fromemail")
        receiver = request.form.get("toemail")
        subject = request.form.get("subject")
        body = request.form.get("body")
        print("welcome error...")

        try:
            msg = Message(subject=subject,
                          recipients=[receiver],
                          body=body,
                          sender=from_email)
            mail.send(msg)
            return "✅ Email sent successfully!", "success"
        except Exception as e:
            return f"❌ Error sending email: {str(e)}", "danger"

        return redirect(url_for("email.sendmail"))

    return render_template("email.html")

