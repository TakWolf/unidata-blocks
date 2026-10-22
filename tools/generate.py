import re

from tools import ASSETS_DIR, SRC_DIR


def _parse_blocks() -> tuple[str, list[tuple[int, int, str, str]]]:
    lines = ASSETS_DIR.joinpath('Blocks.txt').read_text('utf-8').splitlines()

    unicode_version = lines[0].removeprefix('# Blocks-').removesuffix('.txt')

    blocks = []
    regex = re.compile(r'\.\.|;\s')
    for line in lines:
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue

        parts = regex.split(line)
        code_start = int(parts[0], 16)
        code_end = int(parts[1], 16)
        block_name = parts[2]
        id_name = block_name.replace(' ', '_').replace('-', '_').upper()
        blocks.append((code_start, code_end, block_name, id_name))

    return unicode_version, blocks


def main() -> None:
    unicode_version, blocks = _parse_blocks()

    meta_lines = []
    meta_lines.append('from typing import Final')
    meta_lines.append('')
    meta_lines.append('from unidata_blocks.block import UnicodeBlock')
    meta_lines.append('')
    meta_lines.append('__all__ = [')
    meta_lines.append("    'UNICODE_VERSION',")
    for code_start, code_end, block_name, id_name in blocks:
        meta_lines.append(f"    'BLOCK_{id_name}',")
    meta_lines.append("    'BLOCKS',")
    meta_lines.append(']')
    meta_lines.append('')
    meta_lines.append(f'UNICODE_VERSION: Final = {unicode_version!r}')
    meta_lines.append('')
    for code_start, code_end, block_name, id_name in blocks:
        meta_lines.append(f'BLOCK_{id_name}: Final = UnicodeBlock(0x{code_start:04X}, 0x{code_end:04X}, {block_name!r})')
    meta_lines.append('')
    meta_lines.append('BLOCKS: Final = (')
    for _, _, _, id_name in blocks:
        meta_lines.append(f'    BLOCK_{id_name},')
    meta_lines.append(')')
    meta_lines.append('')

    SRC_DIR.mkdir(parents=True, exist_ok=True)
    SRC_DIR.joinpath('meta.py').write_text('\n'.join(meta_lines), 'utf-8')


if __name__ == '__main__':
    main()
