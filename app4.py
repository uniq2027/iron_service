from flask import Flask,render_template,Request,Blueprint


from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email, Length


app4=Blueprint("wtfomr",__name__,template_folder='templates')



# Initialize CSRF protection

class Registration_form(FlaskForm):
    name=StringField("name",validators=[DataRequired()])    
    password=IntegerField("password",validators=[DataRequired()])
    submit=SubmitField("register....")


@app4.route("/wtform",methods=["POST","GET"])
def registration():
    form=Registration_form()
    if form.validate_on_submit():
        return "welcome wt form...!"
    
    

    return render_template("user_info.html",get_form=form)
















# ____________________________________________________________________--

## **2. Why use WTForms instead of plain HTML forms?**

# Without WTForms:

# * You build HTML manually
# * You validate inputs manually
# * You must remember to re-fill fields if validation fails

# With WTForms:

# * Form structure in Python class
# * Built-in validation rules
# * Easy rendering with Jinja2 templates
# * Built-in CSRF protection (security against cross-site request forgery)

# ____________________________________________________________________--



## **6. Built-in Field Types**

# * `StringField` → text input
# * `PasswordField` → password input
# * `EmailField` → HTML5 email input
# * `TextAreaField` → multi-line text
# * `SelectField` → dropdown
# * `BooleanField` → checkbox
# * `FileField` → file upload

# ---

# ## **7. Common Validators**

# * `DataRequired()` → cannot be empty
# * `Email()` → must be valid email
# * `Length(min, max)`
# * `NumberRange(min, max)`
# * `EqualTo(fieldname)` → password confirm
# * `Regexp(pattern)` → custom regex



# ____________________________________________________________________--