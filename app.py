from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

# 注册
@app.route('/register')
def register():
    pass
# 登录
@app.route('/login')
def login():
    pass
# 注销
@app.route('/logout')
def logout():
    pass

# 创建科目
@app.route('/subject/add')
def subject_add():
    pass

# 编辑科目
@app.route('/subject/<int:id>')
def subject_edit(id = None):
    pass

# 删除科目
@app.route('/subject/<int:id>')
def subject_remove(id = None):
    pass

# 创建题目
@app.route('/question/add')
def question_add():
    pass

# 编辑题目
@app.route('/question/<int:id>')
def question_edit(id = None):
    pass

# 删除题目
@app.route('/question/<int:id>')
def question_remove(id = None):
    pass

if __name__ == '__main__':
    app.run()
