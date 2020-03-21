from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(400)
def bad_request(error):
    return render_template("error/400.html"), 400


@bp.app_errorhandler(401)
def not_authorized(error):
    return render_template("error/401.html"), 401


@bp.app_errorhandler(403)
def forbidden(error):
    return render_template("error/403.html"), 403


@bp.app_errorhandler(404)
def not_found(error):
    return render_template("error/404.html"), 404

@bp.app_errorhandler(405)
def method_not_allowed(error):
    return render_template("error/405.html", method=request.method), 405


@bp.app_errorhandler(500)
def internal_server_error(error):
    return render_template("error/500.html"), 500