# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs
import os.path

from os import makedirs

from bibutils.wrapper import _get_version

_version = _get_version()

_test_dir = os.path.split(__file__)[0]
_data_dir = os.path.join(_test_dir, 'data')
_samples_dir = os.path.join(_data_dir, 'samples')
_output_dir = os.path.join(_data_dir, 'output', _version)

if not os.path.exists(_output_dir):
    makedirs(_output_dir)


def _load_file(directory, filename, encoding='utf8'):
    path = os.path.join(directory, filename)
    with codecs.open(path, 'r', encoding) as f:
        return f.read()


def _load_sample(name, filename, encoding='utf8'):
    path = os.path.join(_samples_dir, name, filename)
    with codecs.open(path, 'r', encoding) as f:
        return f.read()


def _save_file(filename, data, encoding='utf8'):
    path = os.path.join(_output_dir, filename)
    with codecs.open(path, 'w', encoding) as f:
        f.write(data)
