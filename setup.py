"""Setup file for easy installation"""

from os.path import dirname, join

from setuptools import setup


def long_description():
    return open(join(dirname(__file__), "README.md")).read()


def load_requirements():
    return open(join(dirname(__file__), "requirements.txt")).readlines()


setup(
    name="social-auth-storage-mongoengine",
    version=__import__("social_mongoengine").__version__,
    author="Matias Aguirre",
    author_email="matiasaguirre@gmail.com",
    description="Python Social Authentication, Mongoengine storage.",
    license="BSD",
    keywords="mongoengine, social auth",
    url="https://github.com/python-social-auth/social-storage-mongoengine",
    packages=["social_mongoengine"],
    long_description=long_description(),
    install_requires=load_requirements(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Internet",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
)
