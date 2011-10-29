import os
import sys
from distutils.core import setup
from distutils.command.install_data import install_data


data_files = []
packages = []

class osx_install_data(install_data):
    def finalize_options(self):
        self.set_undefined_options('install', ('install_lib', 'install_dir'))
        install_data.finalize_options(self
    # end def finalize_options
# end class osx_install_data

if sys.platform == 'darwin':
    cmdclasses = {'install_data': osx_install_data}
else:
    cmdclasses = {'install_data': install_data}
# end if

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
      result = []
    head, tail = os.path.split(path)
    if head == '':
      return [tail] + result
    if head == path:
      return result
    return fullsplit(head, [tail] + result)
# end def fullsplit

for dirpath, dirnames, filenames in os.walk('blueprints'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    # end for
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])
    # end if
# end for

setup(
    name='Builder Blueprints',
    version='0.1.0',
    author='Brandon Ashworth',
    author_email='brandon@brandonashworth.com',
    packages=packages,
    url='',
    license='LICENSE.txt',
    description='Blueprint plugins for Builder',
    long_description='',
    install_requires=[
        "jinja2",
    ],
    data_files = data_files,
    cmdclass = cmdclasses
)