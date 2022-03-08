from flask import Flask, request, jsonify
from api.buildPipeline import build_pipeline

app = Flask(__name__)


@app.route('/', methods=["POST"])
def build():
    response = build_pipeline(request.form.to_dict())
    return jsonify(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
