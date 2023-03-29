from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a127d489fd2aae39ec24098525cbc426'

posts = [
    {
        'author': 'Bob Smith',
        'title': 'Post 1',
        'content': 'Lorem Ipsum Bacon Sandwich',
        'date_posted': 'April 20, 2030'
    },
    {
        'author': 'Jane Smith',
        'title': 'Post 2',
        'content': 'Lorem Ipsum Hummus Pizza',
        'date_posted': 'April 21, 2030'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect( url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       if form.email.data == 'admin@blog.com' and form.password.data == 'password':
           flash(f'You have been logged in!', 'success')
           return redirect(url_for('home'))
       else:
           flash('Login Unsuccessful. Plese check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__': # only runs if this file is called directly
    app.run(debug=True, port=8000)