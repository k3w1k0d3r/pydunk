from setuptools import setup

setup(
    name="pyDunk",
    version="0.1.0",
    author="k3w1k0d3r",
    author_email="juliengrijalva@gmail.com",
    packages=["pydunk"],
    scripts=[],
    url="https://github.com/k3w1k0d3r/pydunk",
    license="LICENSE.txt",
    description="dunkin donuts with python",
    long_description=open("README.md").read(),
    install_requires=[
        "geopy",
        "requests",
    ],
)
