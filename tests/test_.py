import unidata_blocks


def test_unicode_version():
    assert unidata_blocks.unicode_version == '15.0.0'


def test_no_block():
    assert unidata_blocks.get_block_by_code_point(-1) is None
    assert unidata_blocks.get_block_by_code_point(0x999999) is None


def test_code_point_query():
    block = unidata_blocks.get_block_by_code_point(30)
    assert block.code_start == 0x0000
    assert block.code_end == 0x007F
    assert block.name == 'Basic Latin'
    assert block.capacity == 128
    assert block.printable_count == 95

    block = unidata_blocks.get_block_by_code_point(130)
    assert block.code_start == 0x0080
    assert block.code_end == 0xFF
    assert block.name == 'Latin-1 Supplement'
    assert block.capacity == 128
    assert block.printable_count == 94


def test_name_query():
    block = unidata_blocks.get_block_by_name('CJK Unified Ideographs')
    assert block.code_start == 0x4E00
    assert block.code_end == 0x9FFF
    assert block.name == 'CJK Unified Ideographs'
    assert block == unidata_blocks.get_block_by_name('CJK-Unified-Ideographs')
    assert block == unidata_blocks.get_block_by_name('CJK_Unified_Ideographs')
    assert block == unidata_blocks.get_block_by_name('cjk unified ideographs')
    assert block == unidata_blocks.get_block_by_name('CJK UNIFIED IDEOGRAPHS')


def test_chr_query():
    block = unidata_blocks.get_block_by_chr('A')
    assert block.code_start == 0x0000
    assert block.code_end == 0x007F
    assert block.name == 'Basic Latin'
    assert block == unidata_blocks.get_block_by_chr('B')

    block = unidata_blocks.get_block_by_chr('汉')
    assert block.code_start == 0x4E00
    assert block.code_end == 0x9FFF
    assert block.name == 'CJK Unified Ideographs'
    assert block == unidata_blocks.get_block_by_chr('字')


def test_all_query():
    blocks = unidata_blocks.get_blocks()
    assert len(blocks) > 0
    assert blocks[0].name == 'Basic Latin'


def test_to_str():
    block = unidata_blocks.get_block_by_code_point(0x0000)
    assert str(block) == '0000..007F; Basic Latin'

    block = unidata_blocks.get_block_by_code_point(0x4E00)
    assert str(block) == '4E00..9FFF; CJK Unified Ideographs'

    block = unidata_blocks.get_block_by_code_point(0xF0000)
    assert str(block) == 'F0000..FFFFF; Supplementary Private Use Area-A'

    block = unidata_blocks.get_block_by_code_point(0x100000)
    assert str(block) == '100000..10FFFF; Supplementary Private Use Area-B'


def test_i18n():
    block = unidata_blocks.get_block_by_code_point(0x0000)
    assert block.name_localized('en') == 'Basic Latin'
    assert block.name_localized('EN') == 'Basic Latin'
    assert block.name_localized('zh') == '基本拉丁'
    assert block.name_localized('ZH') == '基本拉丁'
    assert block.name_localized('zh-hans') == '基本拉丁'
    assert block.name_localized('zh-chs') == '基本拉丁'
    assert block.name_localized('zh-cn') == '基本拉丁'
    assert block.name_localized('no-language') is None
    assert block.name_localized('no-language', 'abc') == 'abc'
