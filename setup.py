from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alhoda/__init__.py
from alhoda import __version__ as version

setup(
	name="alhoda",
	version=version,
	description="App for Alhoda Company",
	author="Syed Malik Ali",
	author_email="syedmalikali@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
