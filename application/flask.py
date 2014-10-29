from __future__ import absolute_import
from os.path import join

from flask import Flask

from . import helpers
from . import settings


# TODO create separate package for this
class ContinuumFlask(Flask):
    def __init__(self, *args, **kwargs):
        if not 'static_folder' in kwargs:
            kwargs.update({
                'static_folder': join(settings.ROOT_PATH, 'build'),
                'static_url_path': '/static',
            })
        blueprints = kwargs.pop('blueprints', None)
        super(ContinuumFlask, self).__init__(*args, **kwargs)
        self.setup_jinja_context_variables()

        self.setup_blueprints(blueprints)

    def setup_blueprints(self, blueprints):
        if blueprints is None:
            return
        for b in blueprints:
            self.register_blueprint(b)

    def setup_jinja_context_variables(self):
        self.jinja_env.globals.update({
            'static': helpers.static_helper
        })
