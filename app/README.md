* teacher 表格：存储教师信息，包括 id（主键），name（姓名），password（密码）。
* student 表格：存储学生信息，包括 id（主键），name（姓名），password（密码）。
* homework 表格：存储作业信息，包括 id（主键），title（标题），content（内容），file（文件名）。
* score 表格：存储成绩信息，包括 id（主键），student_id（外键，关联 student 表的 id），homework_id（外键，关联 homework 表的 id），score（分数）。
  ```sql
  CREATE TABLE teacher (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    crt_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    upd_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
  );

  CREATE TABLE student (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    crt_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    upd_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
  );

  CREATE TABLE homework (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    file VARCHAR(50),
    crt_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    upd_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
  );

  CREATE TABLE score (
    id INT NOT NULL AUTO_INCREMENT,
    student_id INT NOT NULL REFERENCES student(id),
    homework_id INT NOT NULL REFERENCES homework(id),
    score DECIMAL(5,2) CHECK(score BETWEEN 0 AND 100),
    crt_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     upd_time DATETIME
      ON UPDATE
      current_timestamp() 
      COMMENT '更新时间'
      DEFAULT current_timestamp() 
      COMMENT '创建时间',
    
      PRIMARY KEY (id)
  );

  ```

```python
SQLALCHEMY_DATABASE_URI = 'dialect+driver://username:password@host:port/database'
```

* 其中，dialect 是数据库类型（如 mysql），driver 是数据库驱动（如 pymysql），username 和 password 是数据库的登录凭证，host 和 port 是数据库的地址和端口，database 是要连接的数据库名称。

```python
# code block
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/mydb'
```

[使用flask_mysqldb中的MySQL应该写mysqlclient作为数据驱动。您需要先安装flask-mysqldb和mysqlclient模块，然后在您的代码中添加一个MySQL实例](https://github.com/alexferl/flask-mysqldb)
