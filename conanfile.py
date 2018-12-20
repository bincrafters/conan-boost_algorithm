#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostAlgorithmConan(base.BoostBaseConan):
    name = "boost_algorithm"
    url = "https://github.com/bincrafters/conan-boost_algorithm"
    lib_short_names = ["algorithm"]
    header_only_libs = ["algorithm"]
    cycle_group = "boost_cycle_group_a"
    b2_requires = ["boost_cycle_group_a"]
