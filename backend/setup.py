# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Mosaic API",
    author_email="apiteam@mosaic.com",
    url="",
    keywords=["Swagger", "Mosaic API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Mosaic will be a social media platform designed for individuals to engage in discussions and share content in a community-driven environment. Similar to Reddit, Mosaic will allow users to create and join communities that are focused on specific topics of interest. As the name suggests, our aim is to bring together a diverse community made up of different pieces that come together to create a beautiful and meaningful whole.
    """
)
