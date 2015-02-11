from flask_frozen import Freezer

from application import create_app

app = create_app()
app.config.update({
    'FREEZER_DESTINATION': '../public',
    'FREEZER_RELATIVE_URLS': True,
})

freezer = Freezer(app)


@freezer.register_generator
def urls():
    yield 'application.index', {'page': 'index'}
    yield 'application.index', {'page': 'style-guide'}


if __name__ == '__main__':
    freezer.freeze()
