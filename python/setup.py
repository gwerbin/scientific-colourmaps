from setuptools import setup, find_packages

setup(
    name='scientific-colourmaps',
    author='Gregory Werbin',
    author_email='outthere@me.gregwerbin.com',
    description='Fabio Crameri\'s scientific colourmaps',
    url='https://github.com/gwerbin/scientific-colourmaps',
    license='MIT',
    version='1.0b0',
    packages=find_packages('.', exclude=['test', 'test.*', 'tests', 'tests.*']),
    python_requires='>= 3',
    install_requires=['matplotlib', 'setuptools'],
    include_package_data=True,
    project_urls={
        'Bug Tracker': 'https://github.com/gwerbin/scientific-colourmaps/issues',
        'Documentation': 'https://github.com/gwerbin/scientific-colourmaps/blob/master/python/README.md',
        'Source Code': 'https://github.com/gwerbin/scientific-colourmaps',
    }
)
