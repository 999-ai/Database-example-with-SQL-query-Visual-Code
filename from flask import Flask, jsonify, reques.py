from flask import Flask, jsonify, request
app = Flask(__name__)

users = [
    {"id": 1, "name": "Sibel", "email": "ssssss@yahoo.com"},
    {"id": 2, "name": "Ali", "email": "aaaaa@yahoo.commm"},
    {"id": 3, "name": "Selin", "email": "sssss@yahoo.com"}
]

@app.route('/users', methods=["GET"])
def list_users():
    return jsonify(users)

#if __name__ == '__main__':

# app.run(debug=True) 
@app.route('/users', methods=['POST'])

def add_user():
    new_user = request.json  
    if "id" not in new_user or "name" not in new_user or "email" not in new_user:
        return jsonify({"error": "missing value"}), 400  
    users.append(new_user)
    return jsonify(new_user), 201  
@app.route('/users/<int:user_id>', methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    
    if user is None:  
        return jsonify({"error": "user not found"}), 404

    updated_data = request.json  
    user.update(updated_data) 
    return jsonify(user) 

if __name__ == '__main__':
    app.run(debug=True)
