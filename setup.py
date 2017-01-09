"""Setuptools packaging module."""
from os import path
from setuptools import setup, find_packages

CWD = path.abspath(path.dirname(__file__))
with open(path.join(CWD, "README.rst"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="hello",
    version="0.0.1",
    description="just python boilerplate",
    long_description=LONG_DESCRIPTION,

    author="Simon Poirier",
    author_email="simpoir@gmail.com",

    license="MIT",

    classifiers=[
        "Development Status :: 3 - Alpha",

        "Programming Language :: Python :: 3.5",
    ],

    packages=find_packages(where="src", exclude=["docs", "tests"]),
    package_dir={"": "src"},

    install_requires=[
        "bottle",
    ],

    setup_requires={
        "nose2",
        "cov-core",
        "WebTest",
    },
    test_suite="nose2.collector.collector",

    entry_points={
        "console_scripts": [
            "hellopy=hello.server:main",
        ],
    },

)
