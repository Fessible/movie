from . import admin


@admin.route("/")
def index():
    return '<h1 style="color:red">This is Admin</h1>'
