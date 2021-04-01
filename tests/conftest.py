import pytest
import yaml
import os
import json


@pytest.fixture
def config(config_path="params.yaml"):
    with open(config_path) as params_yaml:
        config = yaml.safe_load(params_yaml)
    return config


@pytest.fixture
def schema_in(schema_path="schema_in.json"):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema
