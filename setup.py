import sys
import os

if 'develop' in sys.argv:
    from setuptools import setup
else:
  from distutils.core import setup

if sys.platform == 'win32':
    dir_sep = '\\'
else:
    dir_sep = '/'

suffix_list = ('.db', '.css', '.map', '.html', '.eot',
               '.svg', '.tff', '.woff', '.png', '.ico',
               '.js', '.scss', '.csv', '.tsv', '.json',
               '.ipynb',)

def get_run_files():
    data_files = []

    root = os.path.join("flask_template",)

    ##scan catalog for files with the above extensions and add to pkg_data_dirs
    for path, dirs, files in os.walk(root):
        for fs in files:
            if fs.endswith(suffix_list):

                #remove estuarial from path name
                install_path = dir_sep.join(path.split(dir_sep)[1:])
                data_files.append(os.path.join(install_path,fs))

    return data_files


package_data = dict(flask_template=get_run_files())

print(package_data)

version = "0.0.1"
setup(name='flask_template',
      version=version,
      author='Continuum Analytics',
      author_email='info@continuum.io',
      url='http://github.com/ContinuumIO/memex-jpl',
      description='Basic Flask Template',
      packages=['flask_template',
                'flask_template/flask_app'],
      package_data=package_data,
      zip_safe=False,
)
