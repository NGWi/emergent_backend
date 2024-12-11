from db import db
from flask import Flask, request, jsonify
from analysis import analyze_biometric_data

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


# your routes here
@app.route('/analyze', methods=['POST'])
def analyze():
    """
    API endpoint to analyze biometric data.
    Expects JSON data with 'heart_rate' and 'blood_pressure'.
    """
    data = request.json

    # Validate input
    if 'heart_rate' not in data or 'blood_pressure' not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Analyze the data
    analysis_results = analyze_biometric_data(data)

    return jsonify(analysis_results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
