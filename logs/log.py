import logging.config
import yaml

def logs():

    with open('logs/config.yaml', 'rt') as f:
        conf = yaml.safe_load(f.read())

        logging.config.dictConfig(conf)

