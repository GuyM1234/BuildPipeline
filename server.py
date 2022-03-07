from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=["POST"])
def build():
    response = build_pipeline(request.form.to_dict())
    return jsonify(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
