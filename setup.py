from io import open
import os
import re

from setuptools import setup

def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.

    Returns:
        list: Requirements file relative path strings
    """
    requirements = set()
    for path in requirements_paths:
        with open(path) as reqs:
            requirements.update(
                line.split('#')[0].strip() for line in reqs
                if is_requirement(line.strip())
            )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement.

    Returns:
        bool: True if the line is not blank, a comment, a URL, or an included file
    """
    return line and not line.startswith(('-r', '#', '-e', 'git+', '-c'))

setup(
    name='django-lang-pref-middleware',
    version='0.1.0',
    packages=['lang_pref_middleware'],
    author='edX',
    author_email='oscm@edx.org',
    url='https://github.com/edx/django-lang-pref-middleware',
    description="Django middleware for setting the user's language preference at request time.",
    long_description=open('README.md').read(),
    install_requires=load_requirements('requirements/base.in'),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)
