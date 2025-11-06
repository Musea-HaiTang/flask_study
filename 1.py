from flask import Flask  # 修正拼写错误

app = Flask(__name__)    # 修正变量名

@app.route("/index")
def index():
    return "成功"

@app.route("/home")      # 修正括号为英文
def home():              # 修正冒号为英文
    return "失败"        # 修正引号为英文

if __name__ == '__main__':  # 添加冒号
    app.run(host="127.8.8.1", port=5000)