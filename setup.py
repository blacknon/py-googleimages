import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="googleimages",
    version="0.0.2",
    author="Akmal",
    author_email="akmal@depia.wiki",
    description="Unofficial packages to find images from Google",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Wikidepia/py-googleimages",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "httpx==0.17.1",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
