from setuptools import setup, find_packages

setup(
    name = 'pytree',
    version = '0.1',
    author = 'Mar Bocatcat',
    author_email = 'mar.bocatcat@gmail.com',
    description = 'a python integration of the popular UNIX "Tree" command',
    license = 'MIT',
    url = 'https://github.com/Marbocatcat/pytree.git',
    packages = find_packages(),
    entry_points = '''
        [console_scripts]
        pytree = pytree.pytree:main
    '''
)
