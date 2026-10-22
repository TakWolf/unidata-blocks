import bisect

from unidata_blocks.meta import *


def _normalize_block_name(name: str) -> str:
    name = name.lower()
    name = name.replace('-', ' ')
    name = name.replace('_', ' ')
    name = name.strip()
    return name


_BLOCK_CODE_STARTS = [block.code_start for block in BLOCKS]
_NAME_TO_BLOCK = {_normalize_block_name(block.name): block for block in BLOCKS}


def get_block_by_code_point(code_point: int) -> UnicodeBlock | None:
    pos = bisect.bisect_right(_BLOCK_CODE_STARTS, code_point) - 1
    if pos >= 0 and BLOCKS[pos].code_end >= code_point:
        return BLOCKS[pos]
    return None


def get_block_by_chr(c: str) -> UnicodeBlock | None:
    return get_block_by_code_point(ord(c))


def get_block_by_name(name: str) -> UnicodeBlock | None:
    return _NAME_TO_BLOCK.get(_normalize_block_name(name), None)
