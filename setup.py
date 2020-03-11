# setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Ray_lambda_ds12",
    version="1.0",
    author="Ray huggins",
    author_email="@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Elswayre/Ray_lambda_ds12",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)