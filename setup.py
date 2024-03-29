from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


# Setting up
setup(
    name='TheAmino',
    version='0.0.1',
    description="An API for bot amino based on Slimakoi's work",
    author= 'Codex',
    url = 'https://github.com/NotCyberCodex/TheAmino',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires = [
        'amino.fix',
        'schedule',
        'reportlab',
        'argparse'

    ],
    keywords=['python', 'bot'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
