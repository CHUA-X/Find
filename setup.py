import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Finds",
    version="0.0.1",
    author="CHUA某人",
    author_email="chua-x@outlook.com",
    description="find ——在电脑浩如烟海的文件中寻找你想要的文件。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CHUA-X/Finds",
    packages=setuptools.find_packages(where='./src'),
    package_dir={"": "src"},
    keyword=['Python', 'python', 'Search'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)
