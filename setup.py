# -*- coding:utf-8 -*-

__author__ = 'gojuukaze'

from setuptools import setup, find_packages

setup(
    name="DeerU",
    version="0.0.1",
    description="DeerU is a content management system(DeerU 是一个开源博客系统)",
    long_description=open("COMMAND_README.md").read(),
    license="GUN V3.0",

    url="https://github.com/gojuukaze/DeerU",
    author="gojuukaze",
    author_email="i@ikaze.uu.me",
    packages=find_packages(include=['deeru_cmd*', ]),

    entry_points={
        'console_scripts': [
            'deeru-admin = deeru_cmd.bin.deeru_admin:run'
        ]
    },

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: DeerU',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    project_urls={
        'Documentation': 'https://deeru.readthedocs.io',
        'Source': 'https://github.com/gojuukaze/DeerU',
    },

)
