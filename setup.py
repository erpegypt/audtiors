from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in auditors/__init__.py
from auditors import __version__ as version

setup(
	name='auditors',
	version=version,
	description='customizations',
	author='connect4systems',
	author_email='info@connect4systems.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
