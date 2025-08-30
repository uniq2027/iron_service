from flask import Blueprint,render_template

bp=Blueprint("register",__name__,template_folder='templates')


@bp.route('/register')
def register():
    return render_template('register.html')