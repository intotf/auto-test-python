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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5585, debug=True, threaded=True)
