from setuptools import setup

setup(
    name='rtstocks',
    version='0.1',
    py_modules=['rtstocks'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        rtstocks=rtstocks.cli:stocks
    ''',
)
