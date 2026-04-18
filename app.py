from flask import Flask, render_template, make_response, redirect, url_for,request 
from config import Config 
from flask_bootstrap import Bootstrap5 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from forms import PostForm 
from models import db, Post 
from flask import session
from models import db, Post, User

app = Flask(__name__)
app.config.from_object(Config)
app.config['SESSION_PERMANENT'] = False
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)

# DB setup



# HOME PAGE
@app.route("/")
def index():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template("index.html", posts=posts)


# LOGIN
from models import db, Post, User

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session.clear()
            session['user'] = username
            session['logged_in'] = True
            return redirect(url_for("index"))
        return "Invalid credentials"
    return render_template("login.html")


# LOGOUT
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))


# CREATE POST

@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        content = request.form.get("content")
        tags = request.form.get("tags", "")
        post = Post(
            title=title,
            description=description,
            content=content,
            tags=tags
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("index"))
    form = PostForm()
    return render_template("create_post.html", form=form)
@app.route("/posts")
def posts():
    all_posts = Post.query.order_by(Post.date.desc()).all()
    return render_template("posts.html", posts=all_posts)

@app.route("/post/<int:id>")
def post(id):
    post = Post.query.get_or_404(id)
    return render_template("post.html", post=post)
@app.route('/googlea22de48551bc6f6f.html')
def google_verify():
    return open('/home/leoosiemo/unfiltered/googlea22de48551bc6f6f.html').read()
if __name__ == "__main__":
    app.run(debug=True)