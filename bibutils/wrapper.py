"""Functions to aid the calling of bibutils command line programs."""

import collections
import re

import sarge

_BIBUTILS_CONVERTERS = set([
    'bib2xml',
    'biblatex2xml',
    'copac2xml',
    'ebi2xml',
    'end2xml',
    'endx2xml',
    'isi2xml',
    'med2xml',
    'ris2xml',
    'wordbib2xml',
    'xml2ads',
    'xml2bib',
    'xml2end',
    'xml2isi',
    'xml2ris',
    'xml2wordbib',
])
_BIBUTILS_CONVERTER_PAIRS = [name.split('2') for name in _BIBUTILS_CONVERTERS]

_BIBUTILS_CONVERTER_MAP = collections.defaultdict(list)

for from_format, to_format in _BIBUTILS_CONVERTER_PAIRS:
    _BIBUTILS_CONVERTER_MAP[from_format].append(to_format)

_BIBUTILS_FORMATS = set(_BIBUTILS_CONVERTER_MAP.keys()) | set(['ads'])

_cleaners = set([
    'mods',
])

_version_result = None


def _normalise_format_name(format_name):
    if format_name == 'xml':
        return 'mods'
    return format_name


def _bibutils_format_name(format_name):
    if format_name == 'mods':
        return 'xml'
    return format_name


def _check_bibutils_conversion(from_format, to_format):
    command = from_format + '2' + to_format
    assert command in _BIBUTILS_CONVERTERS, 'No converter %s' % command


def _pipe(command, data_in, encoding='utf8'):
    p = sarge.capture_stdout(command, input=data_in.encode(encoding))
    return p.stdout.read().decode(encoding)


def convert(data, from_format, to_format, encoding='utf8'):
    from_format = _bibutils_format_name(from_format)
    to_format = _bibutils_format_name(to_format)

    _check_bibutils_conversion(from_format, to_format)
    command = from_format + '2' + to_format

    return _pipe(command, data, encoding)


def clean(data, data_format, encoding='utf8'):
    if data_format in _cleaners:
        command = data_format + 'clean'
    else:
        data_format = _bibutils_format_name(data_format)
        _check_bibutils_conversion(data_format, 'xml')
        _check_bibutils_conversion('xml', data_format)

        command = data_format + '2xml | xml2' + data_format

    return _pipe(command, data, encoding)


def _get_version():
    global _version_result

    if _version_result:
        return _version_result

    p = sarge.capture_stderr('bib2xml --version')
    output = p.stderr.text
    version_regex = re.compile('bibutils suite version (.*) date',
                               re.MULTILINE)
    matches = version_regex.search(output)
    assert matches

    _version_result = matches.group(1)

    return _version_result
