from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="warning-parser",
    version="1.0.0",
    url="https://github.com/qdewaghe/warning-parser",
    author="Quentin Dewaghe",
    author_email="q.dewaghe@gmail.com",
    description="Parses compilers' outputs to retrieve warnings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: English"
    ],
    python_requires=">=3.6",
    py_modules=["warning_parser"],
    package_dir={"": "src"},
    extras_require={
        "dev": [
            "pytest>=3.7"
        ],
    }
)
