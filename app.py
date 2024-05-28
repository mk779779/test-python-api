from flask import Flask, jsonify

app = Flask(__name__)
# test
# branch test


@app.route("/api/data", methods=["GET"])
def get_data():
    data = {"message": "Hello, World!"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
