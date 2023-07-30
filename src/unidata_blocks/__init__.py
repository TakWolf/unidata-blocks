import pkgutil
import re
from typing import Final

import langcodes


def _load_data_text(resource: str) -> str:
    return pkgutil.get_data(__package__, resource).decode(encoding='utf-8')


def _parse_blocks(text: str) -> tuple[str, list['UnicodeBlock']]:
    blocks = []
    lines = text.split('\n')
    version = lines[0].removeprefix('# Blocks-').removesuffix('.txt')
    for line in lines:
        line = line.split('#', 1)[0].strip()
        if line == '':
            continue
        tokens = re.split(r'\.\.|;\s', line)
        code_start = int(tokens[0], 16)
        code_end = int(tokens[1], 16)
        name = tokens[2]
        blocks.append(UnicodeBlock(code_start, code_end, name))
    return version, blocks


def _parse_lang_codes(text: str) -> list[str]:
    lang_codes = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        lang_codes.append(line)
    return lang_codes


def _parse_translations(text: str) -> dict[str, str]:
    translations = {}
    lines = text.split('\n')
    for line in lines:
        line = line.split('#', 1)[0].strip()
        if line == '':
            continue
        tokens = line.split(':')
        if len(tokens) == 2:
            translations[tokens[0].strip()] = tokens[1].strip()
    return translations


class UnicodeBlock:
    _supported_languages: Final[list[str]] = _parse_lang_codes(_load_data_text('unidata/lang-codes.txt'))
    _translations_registry: Final[dict[str, dict[str, str]]] = {}

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

    def name_localized(self, lang_code: str, __default: str = None) -> str | None:
        closest_language = langcodes.closest_supported_match(lang_code, UnicodeBlock._supported_languages)
        if closest_language is None:
            return __default
        if closest_language == 'en':
            return self.name
        if closest_language in UnicodeBlock._translations_registry:
            translations = UnicodeBlock._translations_registry[closest_language]
        else:
            translations = _parse_translations(_load_data_text(f'unidata/translations/{closest_language.lower()}.txt'))
            UnicodeBlock._translations_registry[closest_language] = translations
        return translations.get(self.name, __default)


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
