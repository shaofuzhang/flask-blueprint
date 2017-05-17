#!/usr/bin/env python2
# Copyright (C) 2014, Cameron Brandon White
# -*- coding: utf-8 -*-

import setuptools
import textwrap
from setuptools import find_packages

if __name__ == "__main__":
    setuptools.setup(
        name="zsf-test",
        version="1.0.0",
        description="zsf-test",
        author="zsf",
        author_email="zsfbest@gmail.com",
        long_description=textwrap.dedent("""zsf-test"""),
        packages=find_packages(),
        install_requires=[
            "Flask",
            "xmltodict",
        ],
        include_package_data=True,
        zip_safe=False,
    )
