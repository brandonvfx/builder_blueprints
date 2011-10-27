from distutils.core import setup

setup(
    name='Builder Blueprints',
    version='0.1.0',
    author='Brandon Ashworth',
    author_email='brandon@brandonashworth.com',
    packages=['blueprints', 'blueprints.python'],
    url='',
    license='LICENSE.txt',
    description='Blueprint plugins for Builder',
    long_description='',
    install_requires=[
        "jinja2",
    ],
)