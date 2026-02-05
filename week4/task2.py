from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
next_id = 1

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({
        "status": "ok",
        "data": users,
        "message": "Список користувачів"
    })

@app.route("/users", methods=["POST"])
def create_user():
    global next_id
    data = request.json
    user = {
        "id": next_id,
        "name": data.get("name")
    }
    users.append(user)
    next_id += 1
    return jsonify({
        "status": "ok",
        "data": user,
        "message": "Користувача створено"
    })

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify({
                "status": "ok",
                "data": user,
                "message": "Користувача знайдено"
            })
    return jsonify({
        "status": "error",
        "data": None,
        "message": "Користувача не знайдено"
    })

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name")
            return jsonify({
                "status": "ok",
                "data": user,
                "message": "Користувача оновлено"
            })
    return jsonify({
        "status": "error",
        "data": None,
        "message": "Користувача не знайдено"
    })

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({
                "status": "ok",
                "data": user,
                "message": "Користувача видалено"
            })
    return jsonify({
        "status": "error",
        "data": None,
        "message": "Користувача не знайдено"
    })

if __name__ == "__main__":
    app.run(debug=True)
