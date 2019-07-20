import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="get_nic",
    version="0.0.1",
    author="tech-novic",
    author_email="pradish.purushottaman@outlook.com",
    description="Get Network Interface details",
    long_description="Small package to list all NIC and also get NIC details such as MAC addr, IP addr, etc",
    long_description_content_type="text/markdown",
    url="https://github.com/tech-novic/get-nic-details",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
