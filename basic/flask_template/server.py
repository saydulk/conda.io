from __future__ import absolute_import

import os

# handle both python server.py and setup.py install calling
try:
    from .flask_app import app
except ValueError:
    from flask_app import app

basedir = os.path.abspath(os.path.dirname(__file__))
CONFIG = os.path.join(basedir, 'flask_app', 'config.py')
app.config.from_pyfile(CONFIG)

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
