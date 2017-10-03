import os.path
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, "README.rst")).read()
    CHANGES = open(os.path.join(here, "CHANGES.txt")).read()
except IOError:
    README = CHANGES = ""

setup(
    name="trac-mattermost", version="0.4.0",
    description="Trac notifications in Mattermost (SM Version)",
    long_description="Original Project at: https://github.com/truveris/trac-mattermost.git. README" + "\n\n" + CHANGES,
    author="Truveris Inc., SharpMind GbR",
    author_email="marco@sharpmind.de",
    url="https://github.com/sharpmind-de/trac-mattermost.git",
    packages=find_packages(exclude=["*.tests*"]),
    license="ISC License",
    install_requires=[
        "requests",
    ],
    classifiers=[
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Framework :: Trac",
        "Topic :: Software Development :: Bug Tracking",
    ],
    entry_points = {
        "trac.plugins": [
            "trac_mattermost = trac_mattermost",
        ],
    },
)
