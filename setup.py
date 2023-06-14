from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="get_alt_branches",
    version="0.0.1",
    author="Alexander Seropyan",
    author_email="aliksandrion@gmail.com",
    description="A lightweight library for getting branches from public REST API",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/aliksandrion/get_alt_branches",
    packages=find_packages(),
    install_requires='requirements_dev.txt',
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
