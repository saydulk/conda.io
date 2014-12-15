# continuum-skeleton
Skeleton site for generating a Flask or static website


## Getting Started

### Quick Start

```bash
conda env create -n design --file environment.yml
# or if you don't have conda-env installed
conda create -c javascript -n design "python<3" flask bower gulp
source activate design
npm install
bower install
gulp
```

Note, [gulp][] will run the [Flask][] server via `server.py` after it has
compiled all of the required assets.




[gulp]: http://gulpjs.com
[Flask]: http://flask.pocoo.org/
