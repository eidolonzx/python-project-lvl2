import json
import yaml


def parse_json(path):
    return json.load(open(path, 'r'))


def parse_yaml(path):
    return yaml.safe_load(open(path, 'r'))
