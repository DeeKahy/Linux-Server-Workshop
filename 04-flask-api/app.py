from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple in-memory list — resets every time you restart the server
messages = []

@app.route("/")
def index():
    return jsonify({"message": "API is running!", "endpoints": ["/messages", "/ping"]})

@app.route("/ping")
def ping():
    return jsonify({"response": "pong"})

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

@app.route("/messages", methods=["POST"])
def post_message():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Send JSON with a 'text' field"}), 400

    messages.append({"id": len(messages) + 1, "text": data["text"]})
    return jsonify({"ok": True, "total": len(messages)}), 201


if __name__ == "__main__":
    print("API running on http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
