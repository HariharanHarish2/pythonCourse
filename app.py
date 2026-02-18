from flask import Flask, request, jsonify, abort

app = Flask(__name__)
users = []
current_id = 1


def find_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


# Root route
@app.route("/")
def home():
    return {"message": "User API is running"}


# GET all
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


# GET one
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = find_user(user_id)
    if not user:
        abort(404, description="User not found")
    return jsonify(user)


# POST
@app.route("/users", methods=["POST"])
def add_user():
    global current_id

    data = request.get_json()

    if not data:
        return {"error": "JSON body required"}, 400   # fixed status code

    required_fields = ["name", "age", "email"]
    for field in required_fields:
        if field not in data:
            return {"error": f"{field} is required"}, 400  # fixed status code

    new_user = {
        "id": current_id,
        "name": data["name"],
        "age": data["age"],
        "email": data["email"]
    }

    users.append(new_user)
    current_id += 1

    return jsonify(new_user), 201


# PUT — full update (replace fields provided)
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = find_user(user_id)
    if not user:
        abort(404, description="User not found")

    data = request.get_json()
    if not data:
        return {"error": "JSON body required"}, 400

    if "name" in data:
        user["name"] = data["name"]
    if "age" in data:
        user["age"] = data["age"]
    if "email" in data:
        user["email"] = data["email"]

    return jsonify(user)


# ✅ PATCH — partial update
@app.route("/users/<int:user_id>", methods=["PATCH"])
def patch_user(user_id):
    user = find_user(user_id)
    if not user:
        abort(404, description="User not found")

    data = request.get_json()
    if not data:
        return {"error": "JSON body required"}, 400

    allowed_fields = ["name", "age", "email"]
    updated = False

    for field in allowed_fields:
        if field in data:
            user[field] = data[field]
            updated = True

    if not updated:
        return {"error": "No valid fields provided"}, 400

    return jsonify(user)


# DELETE
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = find_user(user_id)
    if not user:
        abort(404, description="User not found")

    users.remove(user)
    return {"message": "User deleted"}


# Run server
if __name__ == "__main__":
    app.run(debug=True)
