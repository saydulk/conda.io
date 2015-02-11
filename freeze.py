import re

from flask_frozen import Freezer

from application import create_app

app = create_app()
app.config.update({
    'FREEZER_DESTINATION': '../public',
    'FREEZER_RELATIVE_URLS': True,
})


class MyFreezer(Freezer):
    """
    Custom Freezer class to handle patching URLs

    continuum_flask's Flask object adds some helpers that are missed by the
    relative url settings of Frozen Flask.  This is a rudimentary way of making
    some of those URLs relative.

    All pages that end with .html are parsed and any pages
    """
    def _build_one(self, url):
        filename = super(MyFreezer, self)._build_one(url)

        # Skip any non HTML pages
        if not filename.endswith(".html"):
            return filename

        with open(filename, "r") as f:
            contents = f.read()
        contents = re.sub(r"(href|src)=([\"'])/",
                          r"\1=\2./",
                          contents)
        # contents = contents.replace('href="/', 'href="./')
        # contents = contents.replace('src="/', 'src="./')
        #
        with open(filename, "w") as f:
            f.write(contents)
        return filename


freezer = MyFreezer(app)


@freezer.register_generator
def urls():
    yield 'application.index', {'page': 'index'}


if __name__ == '__main__':
    freezer.freeze()
