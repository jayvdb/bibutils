# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from bibutils.wrapper import clean, convert

from tests import _load_sample, _save_file


class TestBibTexDatabase(unittest.TestCase):

    def setUp(self):
        self.data = _load_sample('taalman', 'database.bib')

    @unittest.expectedFailure
    def test_clean(self):
        cleaned = clean(self.data, 'bib')
        _save_file('taalman_database_cleaned.bib', cleaned)
        assert cleaned == self.data

    def test_mods(self):
        mods = convert(self.data, 'bib', 'mods')
        _save_file('taalman_database_mods.xml', mods)
        assert mods.startswith('﻿<?xml version="1.0" encoding="UTF-8"?>')
        assert mods.endswith('</modsCollection>\n')
        assert '<modsCollection xmlns="http://www.loc.gov/mods/v3">' in mods
        assert '<mods ID="Ful83">' in mods
        assert '<identifier type="citekey">Ful83</identifier>' in mods
        assert 'MacPherson’s graph construction' in mods
        assert '<namePart type="family">Sertöz</namePart>' in mods

    @unittest.expectedFailure
    def test_mods_conference(self):
        mods = convert(self.data, 'bib', 'mods')
        bib = convert(mods, 'mods', 'bib')
        assert '@InProceedings{Ful83' not in bib
