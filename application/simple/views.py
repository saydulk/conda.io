import logging

from flask import Blueprint, render_template

logger = logging.getLogger(__name__)
blueprint = Blueprint('application', __name__, template_folder='templates')


@blueprint.route('/', defaults={'page': 'index'})
@blueprint.route('/<page>/')
def index(page):
    if page == "favicon.ico":
        return ""

    return render_template('{}.html'.format(page))
