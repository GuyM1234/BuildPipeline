from heimdell.core.pipeline.setup.setup import setup
from heimdell.core.pipeline.build.build import build


def run(config: dict):
    config = setup(config)
    response = build(config)
    return config, response
