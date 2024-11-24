from flask import Blueprint, request
from app.controllers.auth_controller import logout_user, register_user, login_user

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return "<h1>welcome to login form</h1>"
    else:
        data = request.json
        return login_user(data["username"], data["password"])


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    return register_user(data["username"], data["email"], data["password"])


@auth_bp.route("/logout", methods=["POST"])
def logout():
    return logout_user()