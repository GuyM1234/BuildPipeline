from flask import Flask, request, jsonify
from heimdell.core.setup_pipeline.setup_pipeline import setup_pipeline

app = Flask(__name__)


@app.route('/', methods=["POST"])
def build():
    config = request.form.to_dict()
    print(config)
    # missing_keys = get_missing_keys(config)
    # if len(missing_keys) > 0:
    #     return jsonify("missing_keys", missing_keys), 403
    # try:
    #     validate_values(config)
    # except Exception:
    #     return jsonify("M", missing_keys), 403

    # enrich(config)
    # response = build_pipeline(config)
    return jsonify(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
