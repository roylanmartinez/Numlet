import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Paquete-nlt-roylanmartinez",
    version="1.1.2",
    author="Roylan Martinez Vargas",
    author_email="roylanmartinez97@gmail.com",
    description="Convierte a letras más de 10^600 números",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roylanmartinez/Numlet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
