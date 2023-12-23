import pkgutil
import re
from typing import Final

import langcodes


def _load_data_text(resource: str) -> str:
    return pkgutil.get_data(__package__, resource).decode(encoding='utf-8')


def _parse_blocks(text: str) -> tuple[str, list['UnicodeBlock']]:
    blocks = []
    lines = re.split(r'\r\n|\r|\n', text)
    version = lines[0].removeprefix('# Blocks-').removesuffix('.txt')
    for line in lines:
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue
        tokens = re.split(r'\.\.|;\s', line)
        code_start = int(tokens[0], 16)
        code_end = int(tokens[1], 16)
        name = tokens[2]
        blocks.append(UnicodeBlock(code_start, code_end, name))
    return version, blocks


def _parse_languages(text: str) -> list[str]:
    languages = []
    lines = re.split(r'\r\n|\r|\n', text)
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        languages.append(line)
    return languages


def _parse_translation(text: str) -> dict[str, str]:
    translation = {}
    lines = re.split(r'\r\n|\r|\n', text)
    for line in lines:
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue
        tokens = line.split(':')
        if len(tokens) == 2:
            translation[tokens[0].strip()] = tokens[1].strip()
    return translation


class UnicodeBlock:
    _supported_languages: Final[list[str]] = _parse_languages(_load_data_text('unidata/languages.txt'))
    _translation_registry: Final[dict[str, dict[str, str]]] = {}

    def __init__(self, code_start: int, code_end: int, name: str):
        self.code_start = code_start
        self.code_end = code_end
        self.name = name
        self.capacity = code_end - code_start + 1
        self.printable_count = 0
        for code_point in range(code_start, code_end + 1):
            c = chr(code_point)
            if c.isprintable():
                self.printable_count += 1

    def __str__(self):
        return f'{self.code_start:04X}..{self.code_end:04X}; {self.name}'

    def name_localized(self, language: str, __default: str = None) -> str | None:
        closest_language = langcodes.closest_supported_match(language, UnicodeBlock._supported_languages)
        if closest_language is None:
            return __default
        if closest_language == 'en':
            return self.name
        if closest_language in UnicodeBlock._translation_registry:
            translation = UnicodeBlock._translation_registry[closest_language]
        else:
            translation = _parse_translation(_load_data_text(f'unidata/translations/{closest_language}.txt'))
            UnicodeBlock._translation_registry[closest_language] = translation
        return translation.get(self.name, __default)


def _standardize_block_name(name: str) -> str:
    return name.strip().lower().replace('-', ' ').replace('_', ' ')


unicode_version, _blocks = _parse_blocks(_load_data_text('unidata/Blocks.txt'))
_name_to_block = {_standardize_block_name(block.name): block for block in _blocks}


def get_block_by_code_point(code_point: int) -> UnicodeBlock | None:
    if _blocks[0].code_start <= code_point <= _blocks[-1].code_end:
        for block in _blocks:
            if block.code_start <= code_point <= block.code_end:
                return block
    return None


def get_block_by_name(name: str) -> UnicodeBlock | None:
    return _name_to_block.get(_standardize_block_name(name), None)


def get_block_by_chr(c: str) -> UnicodeBlock | None:
    return get_block_by_code_point(ord(c))


def get_blocks() -> list[UnicodeBlock]:
    return list(_blocks)
