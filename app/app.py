from flask import Flask, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False

@app.route("/")
def home():
    return jsonify(message="API DevOps rodando 🚀")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
