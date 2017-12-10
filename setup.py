"""setup"""
from typing import List

from setuptools import setup, find_packages

with open("requirements.txt") as file:
    requirements: List[str] = file.read().splitlines()

setup(
    name="goolsbee_bot",
    description="Goolsbee Bot",
    version="0.1.1",
    python_requires='>=3',
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "goolsbot = goolsbee_bot.main:main"
        ]
    },
    include_package_data=True,
    packages=find_packages(),
    package_data={
        "goolsbee_bot": ["data/responses.json"]
    },
    # metadata
    author="Abhi Agarwal",
    author_email="abhi@neoliber.al",
    url="https://github.com/neoliberal/goolsbee_bot",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: No Input/Output (Daemon)",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords="reddit neoliberal goolsbee",
)
