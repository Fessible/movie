from . import home
from flask import render_template, redirect, url_for


@home.route("/")
def index():
    return render_template('home/index.html')


@home.route("/animate")
def animate():
    return render_template('home/animation.html')


@home.route("/login")
def login():
    return render_template('home/login.html')


@home.route("/logout")
def logout():
    return redirect(url_for("home.login"))


@home.route("/register")
def register():
    return render_template('home/register.html')


# 会员中心
@home.route("/user")
def user():
    return render_template('home/user.html')


# 修改密码
@home.route('/pwd')
def password():
    return render_template('home/password.html')


# 评论记录
@home.route('/comments')
def comments():
    return render_template('home/comments.html')


# 登陆日志
@home.route('/loginlog')
def login_log():
    return render_template('home/login_log.html')


# 收藏电影
@home.route('/moviecol')
def movie_collection():
    return render_template('home/movie_col.html')


# 搜索
@home.route('/search')
def search():
    return render_template('home/search.html')


# 电影播放界面
@home.route('/play')
def play():
    return render_template('home/play.html')

