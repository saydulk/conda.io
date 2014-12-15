from __future__ import absolute_import, print_function

from continuum_flask import Flask


def create_app():
    return Flask(
        __name__,
        # Change to the name of your settings module
        #
        # Note: This is implied to be `{{ __name__ }}.settings` if it is
        #       not explicitly provided.
        # settings='application.settings',

        # Register any further blue prints here as well
        blueprints=[
            'application.simple.views',
        ]
    )
