from setuptools import setup

setup(
    name="svg",
    version="0.0.1",
    description="SVG drawing library",
    packages=['svg'],
    extras_require={
        'dev': ['pytest', 'pycodestyle']
    }
)
