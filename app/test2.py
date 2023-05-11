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


# 定义查询数据的路由函数
@app.route("/")
def index():
    # 查询所有用户数据
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, score, times FROM works")
    data = cur.fetchall()
    cur.close()
    # 渲染index.html模板文件，并传入users参数
    return render_template("test2.html", data=data)

# 定义修改数据的路由函数（接收GET和POST请求）
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    # 根据id查询用户数据
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, score, times FROM works where id=%s", (id,))
    data = cur.fetchall()
    cur.close()
    # 如果请求方式是GET，则渲染edit.html模板文件，并传入user参数
    if request.method == "GET":
        return render_template("edit.html", user=data)
    # 如果请求方式是POST，则获取表单提交的name和age参数，并更新用户数据
    else:
        cur = mysql.connection.cursor()
        name = request.form.get("name")
        score = request.form.get("score")
        cur.execute("UPDATE works SET score=%s WHERE id=%s", (score, id))
        # 提交数据库会话（保存更改）
        mysql.connection.commit()
        cur.close()
        # 重定向到查询页面（首页）
        return redirect("/")

# 定义删除数据的路由函数（接收GET请求）
@app.route("/delete/<int:id>")
def delete(id):
    # 根据id查询用户数据
    id = int(id)
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM works WHERE id=%s", (id,))
    # 提交数据库会话（保存更改）
    mysql.connection.commit()
    cur.close()
    # 重定向到查询页面（首页）
    return redirect("/")

# 运行app对象（启动服务器）
if __name__ == "__main__":
   app.run(debug=True)