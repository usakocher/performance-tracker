from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="performance-tracker",
    version="1.0.0",
    author="Adam Kocher",
    description="A lightweight Python performance monitoring library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usakocher/performance-tracker",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        # No external dependencies - uses only standard library
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "flake8>=4.0",
            "isort>=5.0",
        ],
    },
    keywords="performance monitoring profiling decorator timing memory",
    project_urls={
        "Bug Reports": ("https://github.com/usakocher/performance-tracker/issues"),
        "Source": "https://github.com/usakocher/performance-tracker",
        "Documentation": (
            "https://github.com/usakocher/performance-tracker/blob/main/docs/"
        ),
    },
)
