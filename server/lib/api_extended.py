from flask_restplus import Api as BaseApi
from flask import url_for


class Api(BaseApi):
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        scheme = 'http' if 'localhost' in self.base_url else 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)
