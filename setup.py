import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mutovis-tools",
    version="0.0.1",
    author="Grey Christoforo",
    author_email="grey@mutovis.com",
    description="Mutovis tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mutovis/tools",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['h52csv = h52csv'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
)
