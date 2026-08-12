import pytest

import unidata_blocks


def test_unicode_version():
    assert unidata_blocks.unicode_version == '17.0.0'


def test_no_block():
    assert unidata_blocks.get_block_by_code_point(-1) is None
    assert unidata_blocks.get_block_by_code_point(0x999999) is None


def test_code_point_query():
    block = unidata_blocks.get_block_by_code_point(30)
    assert block is not None
    assert block.code_start == 0x0000
    assert block.code_end == 0x007F
    assert block.name == 'Basic Latin'
    assert block.capacity == 128

    block = unidata_blocks.get_block_by_code_point(130)
    assert block is not None
    assert block.code_start == 0x0080
    assert block.code_end == 0xFF
    assert block.name == 'Latin-1 Supplement'
    assert block.capacity == 128


def test_chr_query():
    block = unidata_blocks.get_block_by_chr('A')
    assert block is not None
    assert block.code_start == 0x0000
    assert block.code_end == 0x007F
    assert block.name == 'Basic Latin'
    assert block == unidata_blocks.get_block_by_chr('B')

    block = unidata_blocks.get_block_by_chr('汉')
    assert block is not None
    assert block.code_start == 0x4E00
    assert block.code_end == 0x9FFF
    assert block.name == 'CJK Unified Ideographs'
    assert block == unidata_blocks.get_block_by_chr('字')


def test_name_query():
    block = unidata_blocks.get_block_by_name('CJK Unified Ideographs')
    assert block is not None
    assert block.code_start == 0x4E00
    assert block.code_end == 0x9FFF
    assert block.name == 'CJK Unified Ideographs'
    assert block == unidata_blocks.get_block_by_name('CJK-Unified-Ideographs')
    assert block == unidata_blocks.get_block_by_name('CJK_Unified_Ideographs')
    assert block == unidata_blocks.get_block_by_name('cjk unified ideographs')
    assert block == unidata_blocks.get_block_by_name('CJK UNIFIED IDEOGRAPHS')


def test_all_query():
    blocks = unidata_blocks.get_blocks()
    assert len(blocks) > 0
    assert blocks[0].name == 'Basic Latin'


def test_to_str():
    block = unidata_blocks.get_block_by_code_point(0x0000)
    assert block is not None
    assert str(block) == '0000..007F; Basic Latin'

    block = unidata_blocks.get_block_by_code_point(0x4E00)
    assert block is not None
    assert str(block) == '4E00..9FFF; CJK Unified Ideographs'

    block = unidata_blocks.get_block_by_code_point(0xF0000)
    assert block is not None
    assert str(block) == 'F0000..FFFFF; Supplementary Private Use Area-A'

    block = unidata_blocks.get_block_by_code_point(0x100000)
    assert block is not None
    assert str(block) == '100000..10FFFF; Supplementary Private Use Area-B'


def test_contains():
    block = unidata_blocks.get_block_by_code_point(0x4E00)
    assert block is not None
    assert 0x4E00 in block
    assert 0x9FFF in block
    assert 0x5000 in block
    assert 0x1000 not in block
    assert 0xFFFF not in block
    assert '0x5000' not in block


def test_i18n():
    block = unidata_blocks.get_block_by_code_point(0x0000)
    assert block is not None
    assert block.name_localized('en') == 'Basic Latin'
    assert block.name_localized('EN') == 'Basic Latin'
    assert block.name_localized('zh') == '基本拉丁字母'
    assert block.name_localized('ZH') == '基本拉丁字母'
    assert block.name_localized('zh-hans') == '基本拉丁字母'
    assert block.name_localized('zh-chs') == '基本拉丁字母'
    assert block.name_localized('zh-cn') == '基本拉丁字母'
    assert block.name_localized('zh-sg') == '基本拉丁字母'
    assert block.name_localized('zh-hant') == '基本拉丁字母'
    assert block.name_localized('zh-hk') == '基本拉丁字母'
    assert block.name_localized('zh-mo') == '基本拉丁字母'
    assert block.name_localized('zh-tw') == '基本拉丁字母'
    assert block.name_localized('no-language') is None
    assert block.name_localized('no-language', 'abc') == 'abc'


@pytest.mark.parametrize(
    'block_name, zh_cn_name, zh_hk_name, zh_tw_name',
    [
        ('Lao', '老挝文', '老撾文', '寮文'),
        ('Georgian', '格鲁吉亚字母', '格魯吉亞字母', '喬治亞字母'),
        ('Optical Character Recognition', '光学字符识别', '光學字元辨識', '光學字元辨識'),
        ('High Surrogates', '高位代理项', '高代理區', '高代理區'),
        ('Playing Cards', '纸牌', '紙牌', '紙牌'),
        ('Basic Latin', '基本拉丁字母', '基本拉丁字母', '基本拉丁字母'),
        ('Cyrillic Extended-A', '西里尔字母扩充-A', '西里爾字母擴充-A', '西里爾字母擴充-A'),
        ('Arabic Extended-A', '阿拉伯文扩充-A', '阿拉伯文擴充-A', '阿拉伯文擴充-A'),
        ('Myanmar Extended-A', '缅甸文扩充-A', '緬甸文擴充-A', '緬甸文擴充-A'),
        ('Tangut Components', '西夏文构件', '西夏文構件', '西夏文構件'),
        ('Linear A', '线形文字 A', '線形文字 A', '線形文字 A'),
    ],
)
def test_i18n_regional_terms(block_name: str, zh_cn_name: str, zh_hk_name: str, zh_tw_name: str):
    block = unidata_blocks.get_block_by_name(block_name)
    assert block is not None
    assert block.name_localized('zh') == zh_cn_name
    assert block.name_localized('zh-cn') == zh_cn_name
    assert block.name_localized('zh-hk') == zh_hk_name
    assert block.name_localized('zh-tw') == zh_tw_name
