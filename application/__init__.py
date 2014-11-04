from __future__ import absolute_import, print_function

from .flask import ContinuumFlask


def create_app():
    from .simple import views as simple_views
    return ContinuumFlask(
        __name__,
        # Change to the name of your settings module
        #
        # Note: This is implied to be `{{ __name__ }}.settings` if it is
        #       not explicitly provided.
        # settings='application.settings',

        # Register any further blue prints here as well
        blueprints=[
            simple_views.blueprint,
        ]
    )
