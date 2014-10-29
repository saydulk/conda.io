flask-template
==============

## Development

You can run the app with the following: `python server.py` or after installing with
`python setup.py install` you can test with gunicorn:

```
gunicorn flask_template.server:app -b 0.0.0.0:5000 -w4 -k gevent --log-level=debug  --log-file=-
```

## Setup Scripts

- supervisor (montior and restart process)
- gunicorn (workers)
- vagrant (reproducible VMs -- virtualbox)
- fabric (bash on remote machine)
