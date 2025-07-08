from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="VersaLog",
    version="1.2.5",
    description="Versatile logging library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="",
    license="MIT",
    packages=find_packages(include=["VersaLog", "VersaLog.*"]),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.8, <3.14",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
