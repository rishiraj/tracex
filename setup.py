from setuptools import find_packages, setup


with open("README.md") as f:
    long_description = f.read()

INSTALL_REQUIRES = [
    "graphviz==0.10.1"
]

if __name__ == "__main__":
    setup(
        name="tracex",
        description="tracex: tracing / visualization",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Rishiraj Acharya",
        author_email="heyrishiraj@gmail.com",
        url="https://github.com/rishiraj/tracex",
        license="Apache 2.0",
        package_dir={"": "src"},
        packages=find_packages("src"),
        include_package_data=True,
        install_requires=INSTALL_REQUIRES,
        platforms=["linux", "unix"],
        python_requires=">=3.6",
    )