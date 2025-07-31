from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/update-section", methods=["POST"])
def log_edit():
    try:
        data = request.get_json()
        component = data.get("component")
        field = data.get("field")
        new_value = data.get("value")
        print("FRONTEND EDIT DETECTED")
        print(f"Component: {component}")
        print(f"Field: {field}")
        print("New Value:")
        print(new_value)
        print("-" * 50)
        return jsonify({"message": "Edit logged successfully"}), 200
    except Exception as e:
        print("Error logging edit:", str(e))
        return jsonify({"error": str(e)}), 500

# This is required for Vercel to recognize the app
# Do NOT include app.run()
# Expose it as a callable
handler = app
