#!/usr/bin/env python3

'''Setup script for the package.'''

# import os
from setuptools import setup

# Get version from environment variable defined during the GitHub Action
# print ('new vesion', version)

setup(
    name='literatureSurvey',
    # version=str(version),
    # read the version from the file release-version.txt
    version=open('release_version.txt', encoding='utf-8').read().strip(),
    packages=['app'],
    author='Singh, Gurdeep',
    author_email='gsingh@bio.mx',
    description='A template to develop a repo on literature survey',
    url='https://bio.mx/research-teams/artificial-intelligence/team-vpe/',
    license='MIT',
)
