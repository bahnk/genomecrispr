"""
Packaging for GenomeCRISPR library.
"""

from setuptools import setup, find_packages

setup(
    name="genomecrispr",
    version="0.0.0",
    description="GenomeCRISPR library",
    author="Nourdine Bah",
    author_email="nourdinebah@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click"],
    entry_points={"console_scripts": ["screen = genomecrispr.scripts.screen:main"]},
)
