import os 

from setuptools import setup, find_packages

name = "httpdemo"
__version__ = "0.0.1"

scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)

setup(
        name=name,
        version=__version__,
        url="",
        author="fzxiehui",
        author_email="1059248139@qq.com",
        description="",
        long_description=open("README.md").read(),  # 从 README.md 中读取描述
        long_description_content_type="text/markdown",
        packages=find_packages(),
        test_suite="tests",
        include_package_data=True,
        install_requires=[
            ],
        )
