from . import admin
from flask import render_template, url_for, redirect


@admin.route("/")
def index():
    return render_template('admin/index.html')


@admin.route('/login')
def login():
    return render_template('admin/login.html')


@admin.route('/logout')
def logout():
    return redirect(url_for('admin.login'))


@admin.route('/pwd')
def password():
    return render_template('admin/pwd.html')


@admin.route('/tagadd')
def add_tag():
    return render_template('admin/tag_add.html')


@admin.route('/taglist')
def tag_list():
    return render_template('admin/tag_list.html')


@admin.route('/movieadd')
def movie_add():
    return render_template('admin/movie_add.html')


@admin.route('/movielist')
def movie_list():
    return render_template('admin/movie_list.html')


@admin.route('/previewadd')
def preview_add():
    return render_template('admin/preview_add.html')


@admin.route('/previewlist')
def preview_list():
    return render_template('admin/preview_list.html')


@admin.route('/userlist')
def user_list():
    return render_template('admin/user_list.html')


@admin.route('/userview')
def user_view():
    return render_template('admin/user_view.html')


@admin.route('/comments')
def comments():
    return render_template('admin/comment.html')


@admin.route('/moviecol')
def movie_col():
    return render_template('admin/moviecol_list.html')


# 操作日志
@admin.route('/optlog')
def optlog():
    return render_template('admin/opt_log.html')


# 管理员登录日志
@admin.route('/adminloginlog')
def admin_login_log():
    return render_template('admin/admin_login_log.html')


# 用户登录日志
@admin.route('/userloginlog')
def user_login_log():
    return render_template('admin/user_login_log.html')


# 添加权限
@admin.route('/authadd')
def auth_add():
    return render_template('admin/auth_add.html')


@admin.route('/authlist')
def auth_list():
    return render_template('admin/auth_list.html')


@admin.route('/roleadd')
def role_add():
    return render_template('admin/role_add.html')


@admin.route('/rolelist')
def role_list():
    return render_template('admin/role_list.html')


@admin.route('/adminadd')
def admin_add():
    return render_template('admin/admin_add.html')


@admin.route('adminlist')
def admin_list():
    return render_template('admin/admin_list.html')
