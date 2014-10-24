import logging

from flask import Blueprint, render_template

logger = logging.getLogger(__name__)
blueprint = Blueprint('application', __name__, template_folder='templates')


@blueprint.route('/')
def index():
    return render_template('index.html')
