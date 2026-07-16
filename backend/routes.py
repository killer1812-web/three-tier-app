from flask import Blueprint, jsonify, request


api = Blueprint("api", __name__)


users = []


# Create User API
@api.route("/users", methods=["POST"])
def create_user():

    data = request.json

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(new_user)

    return jsonify({
        "message": "User created successfully",
        "user": new_user
    })


# Get Users API
@api.route("/users", methods=["GET"])
def get_users():

    return jsonify(users)


# Update User API
@api.route("/users/<int:id>", methods=["PUT"])
def update_user(id):

    data = request.json

    for user in users:

        if user["id"] == id:

            user["name"] = data["name"]
            user["email"] = data["email"]

            return jsonify({
                "message": "User updated successfully",
                "user": user
            })

    return jsonify({
        "message": "User not found"
    }), 404



# Delete User API
@api.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):

    for user in users:

        if user["id"] == id:

            users.remove(user)

            return jsonify({
                "message": "User deleted successfully"
            })


    return jsonify({
        "message": "User not found"
    }), 404
