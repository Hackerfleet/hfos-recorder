#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# HFOS - Hackerfleet Operating System
# ===================================
# Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

from setuptools import setup, find_packages

setup(
    name="hfos-recorder",
    version="0.0.1",
    description="hfos-recorder",
    author="Hackerfleet Community",
    author_email="riot@c-base.org",
    url="https://github.com/hackerfleet/hfos-recorder",
    license="GNU Affero General Public License v3",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        # 'Framework :: Isomer :: 1',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    packages=find_packages(),
    package_data={'hfos-recorder': ['../docs/*', '../frontend/*']},
    include_package_data=True,
    long_description="""HFOS - Recorder
===============

A navigational-data recorder with InfluxDB support (others planned, but not
recommended) 

This plugin listens for HFOS navdata messages and records them to a configured
InfluxDB server.

This software package is a plugin module for HFOS.
""",
    dependency_links=[],
    install_requires=[
        'hfos-navdata>=0.0.1',
        'influxdb>=5.0.0',
    ],
    entry_points="""[isomer.components]
    recorder=isomer.recorder.recorder:Recorder
    """,
    test_suite="tests.main.main",
)


