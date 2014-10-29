from __future__ import absolute_import

from . import app
from flask import render_template

@app.route('/')
@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html', num_images=30)

@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/compare')
def compare():
    return render_template('compare.html', num_images=10)

@app.route('/uploads')
def uploads():
    return render_template('uploads.html')

@app.route('/a_new_theme')
def a_new_theme():
    return render_template('bootstrap_theme.html')

