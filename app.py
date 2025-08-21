from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)  # <--- allow all origins for now

def random_name(length=5):
    return ''.join(random.choices(string.ascii_letters, k=length))

@app.get("/api/random-data")
def random_data():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except ValueError:
        return jsonify({"error": "Parameters 'a' and 'b' must be integers"}), 400

    n_rows = max(0, a + b)  # ensure non-negative
    rows = []
    for _ in range(n_rows):
        rows.append({
            "Name": random_name(random.randint(3, 8)),
            "Age": random.randint(0, 100),
            "Year": random.randint(1700, 2100),
        })

    return jsonify({
        "columns": ["Name", "Age", "Year"],
        "rows": rows,
        "count": n_rows
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
