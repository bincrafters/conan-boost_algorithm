#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostAlgorithmConan(base.BoostBaseConan):
    name = "boost_algorithm"
    url = "https://github.com/bincrafters/conan-boost_algorithm"
    lib_short_names = ["algorithm"]
    header_only_libs = ["algorithm"]
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_bind",
        "boost_concept_check",
        "boost_config",
        "boost_core",
        "boost_exception",
        "boost_function",
        "boost_iterator",
        "boost_mpl",
        "boost_range",
        "boost_regex",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_tuple",
        "boost_type_traits",
        "boost_unordered"
    ]


