from __future__ import absolute_import, print_function
from os.path import abspath, basename, join

from flask import Flask, url_for

ROOT_PATH = abspath(join(basename(__file__), '..'))


def static_helper(filename):
    # TODO support CDNs
    return url_for('static', filename=filename)


class ContinuumApp(Flask):
    def __init__(self, *args, **kwargs):
        if not 'static_folder' in kwargs:
            kwargs.update({
                'static_folder': join(ROOT_PATH, 'build'),
                'static_url_path': '/static',
            })
        super(ContinuumApp, self).__init__(*args, **kwargs)
        self.setup_jinja_context_variables()

    def setup_jinja_context_variables(self):
        self.jinja_env.globals.update({
            'static': static_helper
        })


def create_app():
    app = ContinuumApp(__name__)

    # Register any and all blueprints here
    from .simple import views
    app.register_blueprint(views.blueprint)

    return app
