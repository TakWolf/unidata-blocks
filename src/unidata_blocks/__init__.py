import pkgutil
import re


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


unicode_version, _blocks = _load_blocks()
_name_to_block = {block.name.lower().replace(' ', '_').replace('-', '_'): block for block in _blocks}


def get_block_by_code_point(code_point: int) -> UnicodeBlock | None:
    if _blocks[0].code_start <= code_point <= _blocks[-1].code_end:
        for block in _blocks:
            if block.code_start <= code_point <= block.code_end:
                return block
    return None


def get_block_by_name(name: str) -> UnicodeBlock | None:
    return _name_to_block.get(name.lower().replace(' ', '_').replace('-', '_'), None)


def get_block_by_chr(c: str) -> UnicodeBlock | None:
    return get_block_by_code_point(ord(c))


def get_blocks() -> list[UnicodeBlock]:
    return list(_blocks)
