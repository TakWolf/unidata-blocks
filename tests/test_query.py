import unidata_blocks


def test_0():
    assert unidata_blocks.get_block_by_code_point(-1) is None
    assert unidata_blocks.get_block_by_code_point(0x999999) is None


def test_1():
    block = unidata_blocks.get_block_by_code_point(30)
    assert block.code_start == 0x0000
    assert block.code_end == 0x007F
    assert block.name == 'Basic Latin'
    assert block.capacity == 128
    assert block.printable_count == 95


def test_2():
    block = unidata_blocks.get_block_by_code_point(130)
    assert block.code_start == 0x0080
    assert block.code_end == 0xFF
    assert block.name == 'Latin-1 Supplement'
    assert block.capacity == 128
    assert block.printable_count == 94


def test_3():
    block = unidata_blocks.get_block_by_name('CJK Unified Ideographs')
    assert block.code_start == 0x4E00
    assert block.code_end == 0x9FFF
    assert block.name == 'CJK Unified Ideographs'
    assert block == unidata_blocks.get_block_by_name('CJK-Unified-Ideographs')
    assert block == unidata_blocks.get_block_by_name('CJK_Unified_Ideographs')
    assert block == unidata_blocks.get_block_by_name('cjk unified ideographs')
    assert block == unidata_blocks.get_block_by_name('CJK UNIFIED IDEOGRAPHS')


def test_4():
    block = unidata_blocks.get_block_by_chr('A')
    assert block.code_start == 0x0000
    assert block.code_end == 0x007F
    assert block.name == 'Basic Latin'
    assert block == unidata_blocks.get_block_by_chr('B')


def test_5():
    block = unidata_blocks.get_block_by_chr('汉')
    assert block.code_start == 0x4E00
    assert block.code_end == 0x9FFF
    assert block.name == 'CJK Unified Ideographs'
    assert block == unidata_blocks.get_block_by_chr('字')


def test_6():
    blocks = unidata_blocks.get_blocks()
    assert len(blocks) > 0
    assert blocks[0].name == 'Basic Latin'
