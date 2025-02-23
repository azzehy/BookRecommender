from setuptools import setup, find_packages

setup(
    name="book_recommendation_system",
    version="0.1",
    author="Younes Az",
    author_email="yazzzeh04@gmail.com",
    description="A book recommendation system using KNN-based collaborative filtering",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/azzehy/BookRecommender.git",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "jupyter",
        "scipy",
        "pickle-mixin"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
