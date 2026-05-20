"""The python wrapper for IQ Option API package setup."""
from setuptools import setup, find_packages
from iqoptionapi.version_control import api_version

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="iqoptionapi",
    version=api_version,
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "websocket-client>=1.6.0,<2.0",
    ],
    include_package_data=True,
    description="Unofficial IQ Option API for Python — community maintained",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NabiBukhsh-AI/iqoptionapi",
    author="NabiBukhsh-AI",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)
