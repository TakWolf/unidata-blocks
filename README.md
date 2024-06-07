# Unidata Blocks

[![Python](https://img.shields.io/badge/python-3.10-brightgreen)](https://www.python.org)
[![PyPI](https://img.shields.io/pypi/v/unidata-blocks)](https://pypi.org/project/unidata-blocks/)

A library that helps query unicode blocks by [Blocks.txt](https://www.unicode.org/Public/UNIDATA/Blocks.txt).

## Installation

```shell
pip install unidata-blocks
```

## Usage

```python
import unidata_blocks

block = unidata_blocks.get_block_by_chr('A')
assert block.code_start == 0x0000
assert block.code_end == 0x007F
assert block.name == 'Basic Latin'
```

## Dependencies

- [Langcodes](https://github.com/rspeer/langcodes)

## License

Under the [MIT license](LICENSE).
