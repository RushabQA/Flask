from flask import render_template, url_for, redirect
from application import app, db, bcrypt
from application.models import Posts, Users
from application.forms import PostForm, RegistrationForm


@app.route('/home')
@app.route('/')
def home():
    all_posts = Posts.query.all()
    return render_template('home.html', title='Home', posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About", desc="This is about blogs")

@app.route('/login')
def login():
    return render_template('login.html', tiltle="Login")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        new_user = Users(
                    email=form.email.data,
                    password=hash_pw
                     )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('post'))
    return render_template('register.html', title="Register", form=form)

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Posts(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            title = form.title.data,
            content = form.content.data
        )


        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('post.html', title='Post', form=form)
