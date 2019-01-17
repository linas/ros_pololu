#!/usr/bin/env python
# Copyright (c) 2013-2018 Hanson Robotics, Ltd. 

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['ros_pololu'],
    package_dir={'': 'src'},
    )

setup(**d)
