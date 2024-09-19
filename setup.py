from setuptools import setup, find_packages


setup(
    name="word_finder",
    version="0.1.0",
    author="Dipanjal Maitra",
    author_email="dipanjalmaitra@gmail.com",
    description="A python package to find words from combination",
    url="https://github.com/dipanjal/word-finder",
    install_requires=[
        "nltk==3.8.1"
    ],
    python_requires='>=3.6',
)
