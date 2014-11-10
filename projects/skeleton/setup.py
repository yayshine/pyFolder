try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Yay Shin',
	'url': 'https://www.facebook.com/yehoon.shin',
	'download_url': 'URL to download',
	'author_email': 'ys2657@columbia.edu',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)