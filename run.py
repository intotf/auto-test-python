from flask import Flask, render_template, request, Response, stream_with_context, jsonify

app = Flask(__name__)


# 包含页面
# #左侧导航菜单
@app.route('/include-nav.html')
def includeNav():
    return render_template('include-nav.html')


# #底部版权信息
@app.route('/include-footer.html')
def includeFooter():
    return render_template('include-footer.html')


# 主页
@app.route('/')
def index():
    return render_template('index.html')


# 登录页
@app.route('/login')
def login():
    return render_template('login.html')


# 接口列表页
@app.route('/interface-list')
def interfaceList():
    return render_template('interface-list.html')


# 添加接口页
@app.route('/interface')
def interface():
    return render_template('interface.html')


# 接口信息页
@app.route('/interface-info')
def interfaceInfo():
    return render_template('interface-info.html')


# 数据库配置列表页
@app.route('/database-config-list')
def databaseConfigList():
    return render_template('database-config-list.html')


# 主机配置列表页
@app.route('/host-config-list')
def hostConfigList():
    return render_template('host-config-list.html')


# 添加任务页
@app.route('/task-add')
def taskAdd():
    return render_template('task-add.html')


# 任务列表页
@app.route('/task-list')
def taskList():
    return render_template('task-list.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5585, debug=True, threaded=True)
