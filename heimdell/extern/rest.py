from flask import Flask, request, jsonify
from heimdell.core.pipeline.run import run
from heimdell.core.utils.exceptions import *

app = Flask(__name__)


@app.route('/', methods=["POST"])
def build():
    config = request.form.to_dict()  # data not received well
    try:
        response = run(config)
        return jsonify(response)
    except ConsumerNotSupported:
        return 'Consumer not supported', 403
    except ProducerNotSupported:
        return 'Producer not supported', 403
    except KeyMissing:
        return 'Key missing', 403


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
