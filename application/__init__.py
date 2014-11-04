from __future__ import absolute_import, print_function

from .flask import ContinuumFlask


def create_app():
    return ContinuumFlask(
        __name__,

        # Register any further blue prints here as well
        blueprints=[
            'application.simple.views',
        ]
    )
