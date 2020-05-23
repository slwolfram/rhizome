import os

from server import app
from server.lib.reverse_proxied import ReverseProxied

PREFIX = ("" if os.environ.get('CONTEXT_PATH') is None else
          os.environ.get('CONTEXT_PATH'))

if __name__ == '__main__':
    app.wsgi_app = ReverseProxied(app.wsgi_app, PREFIX)
    app.run(debug=True, host='0.0.0.0', port='5000')
