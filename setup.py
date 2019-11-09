#!python
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


def get_requirements():
    requirements = [
        'colorama==0.4.1',
        'paho-mqtt==1.4.0',
        'peewee==3.11.2',
        'requests==2.22.0',
        'PyJWT==1.7.1',
        'python-dotenv==0.10.3',
        'simple-chalk==0.1.0',
        'readchar==2.0.1'
    ]
    return requirements


setup(
    name='tmessage',
    version="0.0.2",
    author="Haider Ali",
    author_email="haider.lee23@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Haider8/tmessage",
    license="GPL-3.0",
    entry_points={
        'console_scripts': ['tmessage=tmessage.cli:main'],
    },
    description="""
      This is a lightweight and low bandwidth
      CLI tool which can be used for group
      communication right from your terminal.
      """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    packages=['tmessage'],
    install_requires=get_requirements(),
    zip_safe=False,
)
