from setuptools import setup

AUTHOR = 'Vsevolod Novikov'
AUTHOR_EMAIL = 'nnseva@gmail.com'
URL = 'https://github.com/nnseva/django-jsoneditor'
DESCRIPTION = 'Django JSON Editor'

with open('README.rst') as f:
    LONG_DESCRIPTION = f.read().strip()


with open('VERSION') as f:
    VERSION = f.read().strip()


setup(
    name = 'django-jsoneditor',
    version = VERSION,
    description = DESCRIPTION,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    long_description = LONG_DESCRIPTION,
    packages = [
        'jsoneditor',
        'jsoneditor.fields'
    ],
    package_data = {
        'jsoneditor': [
            'static/jsoneditor/*.js',
            'static/jsoneditor/*.css',
            'static/jsoneditor/img/*',
            'static/django-jsoneditor/*.js',
        ]
    },
    include_package_data = True,
    zip_safe = False,
    install_requires=['packaging']
)
