Python使用flask框架与html页面和MySQL数据库进行交互的方法如下：

- 首先，您需要安装flask和flask_mysqldb模块，可以使用pip命令³：

```python
pip install flask
pip install flask_mysqldb
```

- 然后，您需要在app.py文件中导入flask和MySQL相关的模块，并创建一个Flask对象²³：

```python
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
```

- 接着，您需要配置MySQL数据库的连接信息，并创建一个MySQL对象²³：

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)
```

- 然后，您需要定义路由函数，用来处理不同的请求，并渲染相应的html页面²³。例如，以下代码定义了一个注册页面的路由函数：

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 获取表单数据
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # 连接数据库并执行SQL语句
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email, password) VALUES (%s,%s,%s)", (name,email,password))
        mysql.connection.commit()
        cur.close()
        # 重定向到登录页面
        return redirect(url_for('login'))
```

- 最后，您需要在templates文件夹中创建相应的html页面，并使用jinja2模板引擎来动态显示数据¹²。例如，以下代码是一个简单的注册页面：

```html
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="post" action="/register">
        <p>Name: <input type="text" name="name"></p>
        <p>Email: <input type="email" name="email"></p>
        <p>Password: <input type="password" name="password"></p>
        <p><input type="submit" value="Register"></p>
    </form>
</body>
</html>
```

以上是一个简单的示例代码，您可以参考²和³了解更多细节和功能。

源: 与必应的对话， 2023/2/27(1) Setting up a Flask and MySQL Database Connection .... https://www.askpython.com/python-modules/flask/flask-mysql-database 访问时间 2023/2/27.
(2) Profile Application using Python Flask and MySQL. https://www.geeksforgeeks.org/profile-application-using-python-flask-and-mysql/ 访问时间 2023/2/27.
(3) Python and Flask, display data out of mysql DB on html page. https://stackoverflow.com/questions/66212883/python-and-flask-display-data-out-of-mysql-db-on-html-page 访问时间 2023/2/27.
