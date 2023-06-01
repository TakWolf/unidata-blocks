import pkgutil
import re

_locale_to_localized_names: dict[str, dict[str, str]] = {}


def _get_localized_names(locale: str) -> dict[str, str]:
    if locale in _locale_to_localized_names:
        return _locale_to_localized_names[locale]
    localized_names = {}
    try:
        data = pkgutil.get_data(__package__, f'unidata/i18n/{locale}.txt')
    except FileNotFoundError:
        data = None
    if data is not None:
        lines = data.decode(encoding='utf-8').split('\n')
        for line in lines:
            line = line.split('#', 1)[0].strip()
            if line == '':
                continue
            tokens = re.split(r':\s', line)
            if len(tokens) >= 2:
                localized_names[tokens[0]] = tokens[1]
    _locale_to_localized_names[locale] = localized_names
    return localized_names


class UnicodeBlock:
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

    def name_localized(self, locale: str) -> str | None:
        locale = locale.lower().replace('_', '-')
        if locale == 'en':
            return self.name
        return _get_localized_names(locale).get(self.name, None)


def _load_blocks() -> tuple[str, list[UnicodeBlock]]:
    blocks = []
    lines = pkgutil.get_data(__package__, 'unidata/Blocks.txt').decode(encoding='utf-8').split('\n')
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


def _normalize_block_name(name: str) -> str:
    return name.lower().replace('-', ' ').replace('_', ' ')


unicode_version, _blocks = _load_blocks()
_name_to_block: dict[str, UnicodeBlock] = {_normalize_block_name(block.name): block for block in _blocks}


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
