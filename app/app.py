from flask import Flask, request, render_template, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, login_required
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = '1'
app.config['UPLOAD_FOLDER'] = 'work'

# 配置数据库连接参数
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "993646057."
app.config["MYSQL_DB"] = "work"

# 创建MySQL对象
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registe_stu_now", methods=["GET", "POST"])
def registe_stu_now():
    # 处理注册表单的逻辑
    # 如果注册成功，跳转到主页
    return render_template("register_stu.html")

@app.route("/registe_tea_now", methods=["GET", "POST"])
def registe_tea_now():
    # 处理注册表单的逻辑
    # 如果注册成功，跳转到主页
    return render_template("register_tea.html")

@app.route("/redirect", methods=["POST", "GET"])
def redirect_page():
    identity = request.form.get("identity")
    if identity == "student":
        return redirect("/login_stu")
    elif identity == "teacher":
        return redirect("/login_tea")

@app.route("/register_stu", methods=["POST", "GET"])
def register_stu():
    # 处理注册表单的逻辑
    # 如果用户名和密码有效，将其插入到数据库中
    if request.method == 'POST':
        name = request.form.get("username", type(str))
        password = request.form.get("password", type(str))
        password_again = request.form.get("password_again", type(str))
        # 创建游标并执行查询语句
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM student WHERE name=%s", [name])
        
        # 判断是否有匹配的用户信息
        if result > 0:
          return '用户名已存在或用户名不合法,请返回重新注册'

        if len(name) < 5 or len(name) > 20:
          return render_template("register_stu.html", error="账号长度错误")
        if password != password_again:
          return "密码不一致，请返回重新注册"
        else:
            cur.execute("INSERT INTO student(name, password) VALUES(%s, %s)", (name, password))
            mysql.connection.commit()
            cur.close()
            return '注册成功'
            # 获取数据库的游标对象
            cursor = mysql.connection.cursor()
            # 执行SQL语句插入用户信息
            cursor.execute("INSERT INTO student(name, password) VALUES (%s, %s)", (name, password))
            # 提交事务
            mysql.connection.commit()
            # 关闭游标对象
            cursor.close()
    return render_template('login.html')
  
@app.route("/register_tea", methods=["POST", "GET"])
def register_tea():
    # 处理注册表单的逻辑
    # 如果用户名和密码有效，将其插入到数据库中
    if request.method == 'POST':
        name = request.form.get("username", type(str))
        password = request.form.get("password", type(str))
        password_again = request.form.get("password_again", type(str))
        # 创建游标并执行查询语句
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM teacher WHERE name=%s", [name])
        
        # 判断是否有匹配的用户信息
        if result > 0:
          return '用户名已存在或用户名不合法,请返回重新注册'

        if len(name) < 5 or len(name) > 20:
          return render_template("register_tea.html", error="账号长度错误")
        if password != password_again:
          return "密码不一致，请返回重新注册"
        else:
            cur.execute("INSERT INTO teacher(name, password) VALUES(%s, %s)", (name, password))
            mysql.connection.commit()
            cur.close()
            return '注册成功，请返回登录'
            # 获取数据库的游标对象
            cursor = mysql.connection.cursor()
            # 执行SQL语句插入用户信息
            cursor.execute("INSERT INTO teacher(name, password) VALUES (%s, %s)", (name, password))
            # 提交事务
            mysql.connection.commit()
            # 关闭游标对象
            cursor.close()
    return render_template('login_tea.html')


@app.route('/login_stu', methods=['GET', 'POST'])
def login_stu():
    # 如果是GET请求，返回登录界面模板
    if request.method == 'GET':
        return render_template('login_stu.html')
    # 如果是POST请求，获取表单中的账号和密码
    elif request.method == 'POST':
        username = request.form.get('username', type(str))
        password = request.form.get('password', type(str))
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM student WHERE name=%s AND password=%s", (username, password))        
        # 判断是否有匹配的用户信息
        if result > 0:
            session["username"] = username
            session.permanent = True
            return redirect(url_for("index_stu"))
        else:
            return "用户不存在"

@app.route("/index_stu", methods=["GET", "POST"])
def index_stu():
    if 'username' in session:
        username = session.get("username")
        # 在这里执行数据库查询并检索用户数据
        # cur = mysql.connection.cursor()
        # cur.execute("SELECT score, times FROM student WHERE name=%s", (username,))
        # data = cur.fetchall()
        # cur.close()
        return render_template('index_stu.html', username=username)  
    return redirect(url_for('login_stu'))

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    username = session.get("username")
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = secure_filename(f'{username}_{timestamp}')
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # 通过算法计算score
    # .....
    score = 90
    # 数据库写入数据
    cur = mysql.connection.cursor()

    cur.execute("CREATE TEMPORARY TABLE tmp (times INT);")
    cur.execute("INSERT INTO tmp SELECT count(*) + 1 FROM works WHERE name = %s;", (username,))
    cur.execute("INSERT INTO works(name, homework, score, times) VALUES (%s, %s, 90,\
                (SELECT times FROM tmp));", (username, filename))
    cur.execute("DROP TEMPORARY TABLE tmp;")
    mysql.connection.commit()
    cur.close()
    return "上传成功"

@app.route("/grade_stu", methods=["GET", "POST"])
def grade_stu():
    if request.method == "GET":
        if 'username' in session:
            username = session.get("username")
            cur = mysql.connection.cursor()
            cur.execute("SELECT name, score, times from works where name=%s", (username,))
            data = cur.fetchall()
            cur.close()
            name = "姓名"
            grade = "成绩"
            times = "提交次数"
            return render_template("index_stu.html", username=username, name=name, grade=grade, times=times, data=data)
        return "请先登录"


@app.route('/login_tea', methods=["GET", "POST"])
def login_tea():
    # 如果是GET请求，返回登录界面模板
    if request.method == 'GET':
        return render_template('login_tea.html')
    # 如果是POST请求，获取表单中的账号和密码
    elif request.method == 'POST':
        username = request.form.get('username', type(str))
        password = request.form.get('password', type(str))
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM teacher WHERE name=%s AND password=%s", (username, password))        
        # 判断是否有匹配的用户信息
        if result > 0:
            session["username"] = username
            session.permanent = True
            return redirect(url_for("index_tea"))
        else:
            return "用户不存在"

@app.route("/index_tea", methods=["GET", "POST"])
def index_tea():
    if 'username' in session:
        username = session.get("username")
        # 在这里执行数据库查询并检索用户数据
        cur = mysql.connection.cursor()
        cur.execute("SELECT name, score, times FROM works")
        data = cur.fetchall()
        cur.close()
        return render_template('index_tea.html', data=data, username=username)
    return redirect(url_for('login_tea'))

@app.route("/re_login_stu", methods=["POST", "GET"])
def re_login_stu():
    # 渲染主页的逻辑
    return render_template("login_stu.html")

@app.route("/re_login_tea", methods=["POST", "GET"])
def re_login_tea():
    # 渲染主页的逻辑
    return render_template("login_tea.html")

@app.route("/exit_login", methods=["GET", "POST"])
def exit_login():
    session.pop('username') # 删除session中的用户名键值对
    return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True)