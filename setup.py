# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ManagePosts',
    version='0.1.0',
    description='Library for linking SermonBrowser posts to audio files',
    long_description=readme,
    author='Aaron Dillow',
    author_email='aarond@cpcissaquah.org',
    url='https://github.com/cpcissaquah/ManagePosts',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

