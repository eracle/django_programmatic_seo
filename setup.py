#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Antonio Ercole De Luca",
    author_email='eracle@posteo.eu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Django app thatreate additional pages using a technique called Programmatic SEO.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='django_programmatic_seo',
    name='django_programmatic_seo',
    packages=find_packages(include=['django_programmatic_seo', 'django_programmatic_seo.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/eracle/django_programmatic_seo',
    version='0.1.0',
    zip_safe=False,
)