import os
from flask import Flask as BaseFlask, Config as BaseConfig


class Config(BaseConfig):

    def from_dict(self, dict_config):
        env = os.environ.get('FLASK_ENV', 'development')
        self['Environment'] = env.lower()
        if dict_config:
            for key in dict_config.keys():
                if key.isupper():
                    self[key] = dict_config[key]


class Flask(BaseFlask):

    def make_config(self, instance_relative=False):
        root_path = self.root_path
        if instance_relative:
            root_path = self.instance_path
        return Config(root_path, self.default_config)
