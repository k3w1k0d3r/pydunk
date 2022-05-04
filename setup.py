from setuptools import setup

setup(
	name="pyDunk",
	version="0.0.1",
	author="k3w1k0d3r",
	author_email="juliengrijalva@gmail.com",
	packages=["pydunk"],
	scripts=[],
	url="",
	license='LICENSE.txt',
	description="dunkin donuts with python",
	long_description=open("README.md").read(),
	install_requires=[
		"geopy",
		"requests",
	],
)
