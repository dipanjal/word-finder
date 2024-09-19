from setuptools import setup, find_packages

setup(
    name="word_finder",
    version="0.1.0",
    author="Dipanjal Maitra",
    author_email="dipanjalmaitra@gmail.com",
    description="A python package to find words from combination",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dipanjal/word-finder",
    packages=find_packages(),  # Ensures your package is included
    install_requires=[
        "nltk==3.8.1"  # Your dependency here
    ],
    python_requires='>=3.6',
)
