from flask import render_template
from app import app, db
from flask import render_template, request


@app.errorhandler(400)
def bad_request(error):
    return render_template("error/400.html"), 400


@app.errorhandler(401)
def not_authorized(error):
    return render_template("error/401.html"), 401


@app.errorhandler(403)
def forbidden(error):
    return render_template("error/403.html"), 403


@app.errorhandler(404)
def not_found(error):
    return render_template("error/404.html"), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("error/405.html", method=request.method), 405


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("error/500.html"), 500