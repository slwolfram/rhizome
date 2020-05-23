import yaml


def config_from_yaml(fp):
    with open(fp) as f:
        yaml_file = f.read()
        config = yaml.safe_load(yaml_file)
    return config
