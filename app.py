from datetime import date, datetime
from socket import timeout
from flask import Flask, flash, render_template_string, send_file, session
from flask_sqlalchemy import SQLAlchemy
from pkg_resources import require
from sqlalchemy import update
from flask_login import login_user, current_user, LoginManager, UserMixin, login_required
from flask import render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.widgets import TextArea
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
import hashlib


app = Flask(__name__)

app.config['SECRET_KEY'] = 'FLAG{ServerSideTemplateInjecti0n}' # sets the flag as secret key

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_BINDS'] = {'User': 'sqlite:///db.db'}

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

######################################BROKEN ACCESS CONTROL START#########################################
"""
Broken access control
https://www.toxicsolutions.net/2020/07/exploit-a-simple-idor-vulnerability-with-python/
"""



# broken access users
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    profession = db.Column(db.String(100), nullable=True)
    profilepic = db.Column(db.String(100), nullable=True)
    scn = db.Column(db.String(100), nullable=True)
    flag = db.Column(db.Integer, nullable=True)

db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


admin_user = Users(username='admin', 
                   password='admin', 
                   age=30, 
                   profession="System admin", 
                   profilepic="https://www.crimsondesigns.com/blog-images/website-hacker-at-work.jpg",
                   scn="123456", 
                   flag='FLAG{Insecure_Direct_øbject_Reference}')


regular_user = Users(username='user1', 
                     password='user1', 
                     age=25, profession="Student", 
                     profilepic="https://i.imgur.com/wvxPV9S.png", 
                     scn=54321, 
                     flag="Flag is for admins")

try:
    db.session.add(admin_user)
    db.session.add(regular_user)
    db.session.commit()
except:
    print('Duplicated users')


@app.route('/broken_access', methods=['GET', 'POST'])
def broken_access():
    user = Users.query.filter_by(username='user1', password='user1').first()
    if user:
        login_user(user)

    if str(request.form.get('hint')) == 'hint':
        flash('URL Tampering')

    req = request.args.get('id')   # gets value of get request
    if request.args.get('id'):
        try:
            ids = db.engine.execute('SELECT username, age, profession, profilepic, scn, flag FROM users WHERE id = {}'.format(req)) # req is key value of the get request, and is placed into sql query
            for info in ids:
                username = info[0]
                age = info[1]
                profession = info[2]
                profilepic = info[3]
                scn = info[4]
                flag = info[5]
            return render_template('profile_id.html', username=username, age=age, profession=profession, profilepic=profilepic, scn=scn, flag=flag)
        except Exception:
            pass
    return render_template('frontpage_broken.html')


#########################################BROKEN ACCESS END########################################################

#########################################CRYPTOGRAPHIC FAILURES START########################################################
"""
Cryptographic failures
"""

class User(db.Model, UserMixin):
    __bind_key__ = 'User'                                                                                               # references the db bind
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

def addusers():
    admin = User(username='admin', password=hashlib.md5('changepw123'.encode('utf-8')).hexdigest())
    regular = User(username='user1', password=hashlib.md5('user1'.encode('utf-8')).hexdigest())
    employee1 = User(username='employee1', password=hashlib.md5('employee1'.encode('utf-8')).hexdigest())
    employee2 = User(username='employee2', password=hashlib.md5('employee2'.encode('utf-8')).hexdigest())
    try: 
        db.session.add(admin)
        db.session.add(regular)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
    except Exception:
        pass

class Password(FlaskForm):
    password = PasswordField('password')
    submit = SubmitField()

@app.route('/cryptographic_failures', methods=['GET', 'POST'])
def crypto_fail():
    password = Password()
    addusers() 

    if str(request.form.get('hint')) == 'hint':
        flash("Convert the password hash to clear-text")

    elif str(request.form.get('download')) == 'download':
        return send_file('db.db')

    elif str(request.form.get('password')) == 'changepw123':
        flash('FLAG{CryptØgraph1c_F4ilurez}')

    else:
        flash('Wrong password')
    return render_template('cryptographic_failures.html', form=password)



#########################################CRYPTOGRAPHIC FAILURES END########################################################


##########################################INJECTION START###################################################
"""
INJECTION
"""
class Comment(FlaskForm):
    style={'style': 'font-size: 25px'}
    comment = StringField('comment', render_kw=style, widget=TextArea())
    submit = SubmitField()

@app.route('/injection', methods=['GET', 'POST'])
def injection():
    form = Comment()
    time = date.today()                                                                     #adds time to post
    time = time.strftime("%B %d, %Y")
    user = Users.query.filter_by(username='user1', password='user1').first()                #logs in user
    if user:
        login_user(user)

        if request.method == 'POST':
            result = str(form.comment.data)
            output = render_template_string(result)
        else:
            output = render_template_string("")

    if str(request.form.get('hint')) == 'hint':                                             # display hint message (gets value from hint button and flashes the hint message)
        flash("Use Jinja2 syntax and call upon the flask config object")
    return render_template('injection.html', form=form, output=output, time=time)

#########################################INJECTION END####################################################


#####################################Insecure Design Start########################################

"""
Insecure design
"""

@login_manager.user_loader
def load_user(user_id):
    return Userdesign.query.get(int(user_id))
class Userdesign(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    fav_subject = db.Column(db.String(100), nullable=False)
    fav_color = db.Column(db.String(100), nullable=False)

db.create_all()
musk = Userdesign(username='elonmusk', password='s1f3faf43fdsFS2qDgGGwsxXS', fav_subject='science', fav_color='blue')
try:
    db.session.add(musk)
    db.session.commit()
except:
    print('Duplicated users')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired()], render_kw={"placeholder": "Username = elonmusk"})
    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

class ResetForm(FlaskForm):
    username = StringField(validators=[InputRequired()], render_kw={"placeholder": "Username"})
    favsubject = StringField(validators=[InputRequired()], render_kw={"placeholder": "Subject"})
    favcolor = StringField(validators=[InputRequired()], render_kw={"placeholder": "Color"})
    newpw = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField("Reset")

@login_required
@app.route('/insecure_design', methods=['GET', 'POST'])
def insecure_design():
    form = LoginForm()
    if form.validate_on_submit():
        user = Userdesign.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                return redirect('/insecure_design/elonmusk')
            else:
                flash("Wrong username or password")
                return redirect('/insecure_design')
        if not user: 
            flash("Wrong username or password")
            return redirect('/insecure_design')
    
    if str(request.form.get('hint')) == 'hint':
        flash("Do some research on Elon Musk and recover his password")
    return render_template('/insecure_design.html', form=form)

@app.route('/insecure_design/pwreset', methods=['GET', 'POST'])
def pwreset():
    form = ResetForm()
    user =  Userdesign.query.filter_by(username=form.username.data).first()
    if request.method == 'POST':                                                                                                                                                        #checks if control questions exists in db and updates to new password
        if user:
            if user.username == form.username.data:
                if user.fav_subject == form.favsubject.data:
                    if user.fav_color == form.favcolor.data:
                        db.session.execute(update(Userdesign).where(Userdesign.username =='{}'.format(form.username.data)).values(password='{}'.format(form.newpw.data)))
                        db.session.commit()
                        flash("Password has successfully been changed")
                        return redirect('/insecure_design/pwreset')
        else:
            flash('Username does not exist')
            return redirect('/insecure_design/pwreset')    
    return render_template('pwreset.html', form=form)

@login_required
@app.route('/insecure_design/elonmusk', methods=['GET', 'POST'])
def elon_profile():
    return render_template('elonmusk.html')


#####################################INSECURE DESIGN END############################################

#####################################SECURITY MISCONFIGURATION START########################################

class WP_loginForm(FlaskForm):
    username = StringField([InputRequired()])
    password = PasswordField([InputRequired()])
    submit = SubmitField("Login")

"""
Security misconfiguration
"""
@app.route('/security_misconfiguration/wp-login.php', methods=['GET', 'POST'])
def security_misconfiguration():
    form = WP_loginForm()
    if request.form.get('username') == "admin":
        if request.form.get('password') == "password":
            flash('FLAG{s3c_miscønf}')
    return render_template('security_misconfiguration.html', form=form)


#####################################SECURITY MISCONFIGURATION END########################################


"""
Vulnerable and outdated components (Plone CMS)
"""

@app.route('/vulncomponent', methods=['GET', 'POST'])
def vulncomponent():
    
    return render_template('vulncomponent.html')


"""
Identitification and authentication failures
"""
@app.route('/authentication_failure', methods=['GET', 'POST'])
def auth_fail():
    return render_template('authentication_failure.html')



"""
Software and Data Integrity Failures
"""
@app.route('/software_data_integrity_failure', methods=['GET', 'POST'])
def integrity_fail():
    return render_template('software_data_integrity_failure.html')




"""
Security Logging and Monitoring Failures
"""
@app.route('/log_and_monitor_failure', methods=['GET', 'POST'])
def log_and_monitor_fail():
    return render_template('log_and_monitor_failure.html')




"""
Server-Side Request Forgery
"""
@app.route('/ssrf', methods=['GET', 'POST'])
def ssrf():
    return render_template('ssrf.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)