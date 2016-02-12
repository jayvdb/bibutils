# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from distutils.version import LooseVersion

from bibutils.wrapper import _get_version


class TestVersion(unittest.TestCase):

    def test_version(self):
        version = _get_version()
        assert LooseVersion(version) > LooseVersion('4.0')
