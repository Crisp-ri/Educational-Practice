from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"

users = {
    "admin": generate_password_hash("1234")
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"status": "error", "data": None, "message": "Токен відсутній"}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except:
            return jsonify({"status": "error", "data": None, "message": "Невалідний токен"}), 401
        return f(data["user"], *args, **kwargs)
    return decorated

@app.route("/login", methods=["POST"])
def login():
    auth = request.json
    username = auth.get("username")
    password = auth.get("password")

    if username in users and check_password_hash(users[username], password):
        token = jwt.encode({
            "user": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config["SECRET_KEY"], algorithm="HS256")

        return jsonify({
            "status": "ok",
            "data": {"token": token},
            "message": "Успішний вхід"
        })

    return jsonify({
        "status": "error",
        "data": None,
        "message": "Невірні дані"
    }), 401

@app.route("/profile", methods=["GET"])
@token_required
def profile(user):
    return jsonify({
        "status": "ok",
        "data": {"username": user},
        "message": "Доступ дозволено"
    })

if __name__ == "__main__":
    app.run(debug=True)
