from setuptools import setup, find_packages

setup(
    name='scientific-colormaps',
    author='Gregory Werbin',
    author_email='outthere@me.gregwerbin.com',
    version='1.0b0',
    packages=find_packages('.', exclude=['tests', 'tests.*']),
    install_requires=['matplotlib', 'setuptools']
)
