# conda.io
Flask site used for generating the http://conda.io which is hosted on gh-pages.

You should only need to work with this if you want to modify the existing site.

## Quick Start

```bash
conda env create
# or if you don't have conda-env installed
source activate conda.io
npm install
bower install
gulp
```

Note, [gulp][] will run the [Flask][] server via `server.py` after it has
compiled all of the required assets.


## Build Static Site

You can build a static version of this site using the `freeze.py` script.  You
need to modify that to pick up any additional pages that you add.

```bash
ptyhon freeze.py
```

That drops a pre-built version of the site into the `./public/` directory.  Note
that the site is meant to be at the root of a web server, so you must start a
simple web server if you wish to view it.

```bash
python -m SimpleHTTPServer
```

## Deploying to GitHub
There is a `gh-pages` task in the `Makefile` for handling deployment.  With
everything committed to the `master` branch, run the following:

```bash
make gh-pages
```

That builds and deploys your changes.


[gulp]: http://gulpjs.com
[Flask]: http://flask.pocoo.org/
