from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required

app = Flask(__name__)
app.secret_key = "secret"

login_manager = LoginManager()
login_manager.init_app(app)

# 模拟一个用户类
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# 模拟一个用户数据库
users = {"user1": User("user1"), "user2": User("user2")}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route("/login", methods=["GET", "POST"])
def login():
    # 处理登录表单的逻辑
    # 如果用户名和密码正确，调用login_user函数登录用户
    user = users.get("user1") # 假设用户是user1
    login_user(user)
    return redirect(url_for("home"))

@app.route("/")
@login_required # 保护主页需要登录才能访问
def home():
    # 渲染主页的逻辑
    return render_template("home.html")