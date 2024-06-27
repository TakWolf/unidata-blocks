import re
from importlib import resources
from typing import Any

import langcodes

_unidata_dir = resources.files(__package__).joinpath('unidata')
_translations_dir = _unidata_dir.joinpath('translations')


def _parse_blocks(text: str) -> tuple[str, list['UnicodeBlock']]:
    blocks = []
    lines = text.splitlines()
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


def _parse_translation(text: str) -> dict[str, str]:
    translation = {}
    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue
        tokens = line.split(':')
        if len(tokens) == 2:
            translation[tokens[0].strip()] = tokens[1].strip()
    return translation


def _get_supported_languages() -> list[str]:
    languages = ['en']
    for file_path in _translations_dir.iterdir():
        if file_path.name.endswith('.txt'):
            language = file_path.name.removesuffix('.txt')
            languages.append(language)
    return languages


_supported_languages = _get_supported_languages()
_translations = {}


class UnicodeBlock:
    code_start: int
    code_end: int
    name: str
    capacity: int
    printable_count: int

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

    def __repr__(self) -> str:
        return f'{self.code_start:04X}..{self.code_end:04X}; {self.name}'

    def __contains__(self, item: Any) -> bool:
        if not isinstance(item, int):
            return False
        return self.code_start <= item <= self.code_end

    def name_localized(self, language: str, __default: str | None = None) -> str | None:
        closest_language = langcodes.closest_supported_match(language, _supported_languages)
        if closest_language is None:
            return __default
        if closest_language == 'en':
            return self.name
        if closest_language in _translations:
            translation = _translations[closest_language]
        else:
            translation = _parse_translation(_translations_dir.joinpath(f'{closest_language}.txt').read_text('utf-8'))
            _translations[closest_language] = translation
        return translation.get(self.name, __default)


def _normalize_block_name(name: str) -> str:
    name = name.lower()
    name = name.replace('-', ' ')
    name = name.replace('_', ' ')
    name = name.strip()
    return name


unicode_version, _blocks = _parse_blocks(_unidata_dir.joinpath('Blocks.txt').read_text('utf-8'))
_name_to_block = {_normalize_block_name(block.name): block for block in _blocks}


def get_block_by_code_point(code_point: int) -> UnicodeBlock | None:
    if _blocks[0].code_start <= code_point <= _blocks[-1].code_end:
        for block in _blocks:
            if block.code_start <= code_point <= block.code_end:
                return block
    return None


def get_block_by_name(name: str) -> UnicodeBlock | None:
    return _name_to_block.get(_normalize_block_name(name), None)


def get_block_by_chr(c: str) -> UnicodeBlock | None:
    return get_block_by_code_point(ord(c))


def get_blocks() -> list[UnicodeBlock]:
    return list(_blocks)
