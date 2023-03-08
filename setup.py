from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bbc/__init__.py
from bbc import __version__ as version

setup(
	name="bbc",
	version=version,
	description="british broadcast corperation",
	author="mlaynimes",
	author_email="kelvinmlay",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
