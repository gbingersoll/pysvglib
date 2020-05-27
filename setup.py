from setuptools import setup
from os import path

# Read the contents of the README file
cwd = path.abspath(path.dirname(__file__))
with open(path.join(cwd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pysvglib",
    version="0.3.2",
    description="SVG drawing library",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Multimedia :: Graphics',
    ],
    keywords='svg graphics',
    url='https://github.com/gbingersoll/pysvglib',
    author='Greg Ingersoll',
    author_email='greg.ingersoll@convolutionresearch.com',
    license='MIT',
    packages=['svg'],
    extras_require={
        'dev': ['pytest', 'pycodestyle', 'setuptools', 'wheel']
    }
)
