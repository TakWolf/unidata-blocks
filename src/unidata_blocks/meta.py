from typing import Final

from unidata_blocks.block import UnicodeBlock

__all__ = [
    'UNICODE_VERSION',
    'BLOCK_BASIC_LATIN',
    'BLOCK_LATIN_1_SUPPLEMENT',
    'BLOCK_LATIN_EXTENDED_A',
    'BLOCK_LATIN_EXTENDED_B',
    'BLOCK_IPA_EXTENSIONS',
    'BLOCK_SPACING_MODIFIER_LETTERS',
    'BLOCK_COMBINING_DIACRITICAL_MARKS',
    'BLOCK_GREEK_AND_COPTIC',
    'BLOCK_CYRILLIC',
    'BLOCK_CYRILLIC_SUPPLEMENT',
    'BLOCK_ARMENIAN',
    'BLOCK_HEBREW',
    'BLOCK_ARABIC',
    'BLOCK_SYRIAC',
    'BLOCK_ARABIC_SUPPLEMENT',
    'BLOCK_THAANA',
    'BLOCK_NKO',
    'BLOCK_SAMARITAN',
    'BLOCK_MANDAIC',
    'BLOCK_SYRIAC_SUPPLEMENT',
    'BLOCK_ARABIC_EXTENDED_B',
    'BLOCK_ARABIC_EXTENDED_A',
    'BLOCK_DEVANAGARI',
    'BLOCK_BENGALI',
    'BLOCK_GURMUKHI',
    'BLOCK_GUJARATI',
    'BLOCK_ORIYA',
    'BLOCK_TAMIL',
    'BLOCK_TELUGU',
    'BLOCK_KANNADA',
    'BLOCK_MALAYALAM',
    'BLOCK_SINHALA',
    'BLOCK_THAI',
    'BLOCK_LAO',
    'BLOCK_TIBETAN',
    'BLOCK_MYANMAR',
    'BLOCK_GEORGIAN',
    'BLOCK_HANGUL_JAMO',
    'BLOCK_ETHIOPIC',
    'BLOCK_ETHIOPIC_SUPPLEMENT',
    'BLOCK_CHEROKEE',
    'BLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS',
    'BLOCK_OGHAM',
    'BLOCK_RUNIC',
    'BLOCK_TAGALOG',
    'BLOCK_HANUNOO',
    'BLOCK_BUHID',
    'BLOCK_TAGBANWA',
    'BLOCK_KHMER',
    'BLOCK_MONGOLIAN',
    'BLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED',
    'BLOCK_LIMBU',
    'BLOCK_TAI_LE',
    'BLOCK_NEW_TAI_LUE',
    'BLOCK_KHMER_SYMBOLS',
    'BLOCK_BUGINESE',
    'BLOCK_TAI_THAM',
    'BLOCK_COMBINING_DIACRITICAL_MARKS_EXTENDED',
    'BLOCK_BALINESE',
    'BLOCK_SUNDANESE',
    'BLOCK_BATAK',
    'BLOCK_LEPCHA',
    'BLOCK_OL_CHIKI',
    'BLOCK_CYRILLIC_EXTENDED_C',
    'BLOCK_GEORGIAN_EXTENDED',
    'BLOCK_SUNDANESE_SUPPLEMENT',
    'BLOCK_VEDIC_EXTENSIONS',
    'BLOCK_PHONETIC_EXTENSIONS',
    'BLOCK_PHONETIC_EXTENSIONS_SUPPLEMENT',
    'BLOCK_COMBINING_DIACRITICAL_MARKS_SUPPLEMENT',
    'BLOCK_LATIN_EXTENDED_ADDITIONAL',
    'BLOCK_GREEK_EXTENDED',
    'BLOCK_GENERAL_PUNCTUATION',
    'BLOCK_SUPERSCRIPTS_AND_SUBSCRIPTS',
    'BLOCK_CURRENCY_SYMBOLS',
    'BLOCK_COMBINING_DIACRITICAL_MARKS_FOR_SYMBOLS',
    'BLOCK_LETTERLIKE_SYMBOLS',
    'BLOCK_NUMBER_FORMS',
    'BLOCK_ARROWS',
    'BLOCK_MATHEMATICAL_OPERATORS',
    'BLOCK_MISCELLANEOUS_TECHNICAL',
    'BLOCK_CONTROL_PICTURES',
    'BLOCK_OPTICAL_CHARACTER_RECOGNITION',
    'BLOCK_ENCLOSED_ALPHANUMERICS',
    'BLOCK_BOX_DRAWING',
    'BLOCK_BLOCK_ELEMENTS',
    'BLOCK_GEOMETRIC_SHAPES',
    'BLOCK_MISCELLANEOUS_SYMBOLS',
    'BLOCK_DINGBATS',
    'BLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A',
    'BLOCK_SUPPLEMENTAL_ARROWS_A',
    'BLOCK_BRAILLE_PATTERNS',
    'BLOCK_SUPPLEMENTAL_ARROWS_B',
    'BLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B',
    'BLOCK_SUPPLEMENTAL_MATHEMATICAL_OPERATORS',
    'BLOCK_MISCELLANEOUS_SYMBOLS_AND_ARROWS',
    'BLOCK_GLAGOLITIC',
    'BLOCK_LATIN_EXTENDED_C',
    'BLOCK_COPTIC',
    'BLOCK_GEORGIAN_SUPPLEMENT',
    'BLOCK_TIFINAGH',
    'BLOCK_ETHIOPIC_EXTENDED',
    'BLOCK_CYRILLIC_EXTENDED_A',
    'BLOCK_SUPPLEMENTAL_PUNCTUATION',
    'BLOCK_CJK_RADICALS_SUPPLEMENT',
    'BLOCK_KANGXI_RADICALS',
    'BLOCK_IDEOGRAPHIC_DESCRIPTION_CHARACTERS',
    'BLOCK_CJK_SYMBOLS_AND_PUNCTUATION',
    'BLOCK_HIRAGANA',
    'BLOCK_KATAKANA',
    'BLOCK_BOPOMOFO',
    'BLOCK_HANGUL_COMPATIBILITY_JAMO',
    'BLOCK_KANBUN',
    'BLOCK_BOPOMOFO_EXTENDED',
    'BLOCK_CJK_STROKES',
    'BLOCK_KATAKANA_PHONETIC_EXTENSIONS',
    'BLOCK_ENCLOSED_CJK_LETTERS_AND_MONTHS',
    'BLOCK_CJK_COMPATIBILITY',
    'BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A',
    'BLOCK_YIJING_HEXAGRAM_SYMBOLS',
    'BLOCK_CJK_UNIFIED_IDEOGRAPHS',
    'BLOCK_YI_SYLLABLES',
    'BLOCK_YI_RADICALS',
    'BLOCK_LISU',
    'BLOCK_VAI',
    'BLOCK_CYRILLIC_EXTENDED_B',
    'BLOCK_BAMUM',
    'BLOCK_MODIFIER_TONE_LETTERS',
    'BLOCK_LATIN_EXTENDED_D',
    'BLOCK_SYLOTI_NAGRI',
    'BLOCK_COMMON_INDIC_NUMBER_FORMS',
    'BLOCK_PHAGS_PA',
    'BLOCK_SAURASHTRA',
    'BLOCK_DEVANAGARI_EXTENDED',
    'BLOCK_KAYAH_LI',
    'BLOCK_REJANG',
    'BLOCK_HANGUL_JAMO_EXTENDED_A',
    'BLOCK_JAVANESE',
    'BLOCK_MYANMAR_EXTENDED_B',
    'BLOCK_CHAM',
    'BLOCK_MYANMAR_EXTENDED_A',
    'BLOCK_TAI_VIET',
    'BLOCK_MEETEI_MAYEK_EXTENSIONS',
    'BLOCK_ETHIOPIC_EXTENDED_A',
    'BLOCK_LATIN_EXTENDED_E',
    'BLOCK_CHEROKEE_SUPPLEMENT',
    'BLOCK_MEETEI_MAYEK',
    'BLOCK_HANGUL_SYLLABLES',
    'BLOCK_HANGUL_JAMO_EXTENDED_B',
    'BLOCK_HIGH_SURROGATES',
    'BLOCK_HIGH_PRIVATE_USE_SURROGATES',
    'BLOCK_LOW_SURROGATES',
    'BLOCK_PRIVATE_USE_AREA',
    'BLOCK_CJK_COMPATIBILITY_IDEOGRAPHS',
    'BLOCK_ALPHABETIC_PRESENTATION_FORMS',
    'BLOCK_ARABIC_PRESENTATION_FORMS_A',
    'BLOCK_VARIATION_SELECTORS',
    'BLOCK_VERTICAL_FORMS',
    'BLOCK_COMBINING_HALF_MARKS',
    'BLOCK_CJK_COMPATIBILITY_FORMS',
    'BLOCK_SMALL_FORM_VARIANTS',
    'BLOCK_ARABIC_PRESENTATION_FORMS_B',
    'BLOCK_HALFWIDTH_AND_FULLWIDTH_FORMS',
    'BLOCK_SPECIALS',
    'BLOCK_LINEAR_B_SYLLABARY',
    'BLOCK_LINEAR_B_IDEOGRAMS',
    'BLOCK_AEGEAN_NUMBERS',
    'BLOCK_ANCIENT_GREEK_NUMBERS',
    'BLOCK_ANCIENT_SYMBOLS',
    'BLOCK_PHAISTOS_DISC',
    'BLOCK_LYCIAN',
    'BLOCK_CARIAN',
    'BLOCK_COPTIC_EPACT_NUMBERS',
    'BLOCK_OLD_ITALIC',
    'BLOCK_GOTHIC',
    'BLOCK_OLD_PERMIC',
    'BLOCK_UGARITIC',
    'BLOCK_OLD_PERSIAN',
    'BLOCK_DESERET',
    'BLOCK_SHAVIAN',
    'BLOCK_OSMANYA',
    'BLOCK_OSAGE',
    'BLOCK_ELBASAN',
    'BLOCK_CAUCASIAN_ALBANIAN',
    'BLOCK_VITHKUQI',
    'BLOCK_TODHRI',
    'BLOCK_LINEAR_A',
    'BLOCK_LATIN_EXTENDED_F',
    'BLOCK_CYPRIOT_SYLLABARY',
    'BLOCK_IMPERIAL_ARAMAIC',
    'BLOCK_PALMYRENE',
    'BLOCK_NABATAEAN',
    'BLOCK_HATRAN',
    'BLOCK_PHOENICIAN',
    'BLOCK_LYDIAN',
    'BLOCK_SIDETIC',
    'BLOCK_MEROITIC_HIEROGLYPHS',
    'BLOCK_MEROITIC_CURSIVE',
    'BLOCK_KHAROSHTHI',
    'BLOCK_OLD_SOUTH_ARABIAN',
    'BLOCK_OLD_NORTH_ARABIAN',
    'BLOCK_MANICHAEAN',
    'BLOCK_AVESTAN',
    'BLOCK_INSCRIPTIONAL_PARTHIAN',
    'BLOCK_INSCRIPTIONAL_PAHLAVI',
    'BLOCK_PSALTER_PAHLAVI',
    'BLOCK_OLD_TURKIC',
    'BLOCK_OLD_HUNGARIAN',
    'BLOCK_HANIFI_ROHINGYA',
    'BLOCK_GARAY',
    'BLOCK_RUMI_NUMERAL_SYMBOLS',
    'BLOCK_YEZIDI',
    'BLOCK_ARABIC_EXTENDED_C',
    'BLOCK_OLD_SOGDIAN',
    'BLOCK_SOGDIAN',
    'BLOCK_OLD_UYGHUR',
    'BLOCK_CHORASMIAN',
    'BLOCK_ELYMAIC',
    'BLOCK_BRAHMI',
    'BLOCK_KAITHI',
    'BLOCK_SORA_SOMPENG',
    'BLOCK_CHAKMA',
    'BLOCK_MAHAJANI',
    'BLOCK_SHARADA',
    'BLOCK_SINHALA_ARCHAIC_NUMBERS',
    'BLOCK_KHOJKI',
    'BLOCK_MULTANI',
    'BLOCK_KHUDAWADI',
    'BLOCK_GRANTHA',
    'BLOCK_TULU_TIGALARI',
    'BLOCK_NEWA',
    'BLOCK_TIRHUTA',
    'BLOCK_SIDDHAM',
    'BLOCK_MODI',
    'BLOCK_MONGOLIAN_SUPPLEMENT',
    'BLOCK_TAKRI',
    'BLOCK_MYANMAR_EXTENDED_C',
    'BLOCK_AHOM',
    'BLOCK_DOGRA',
    'BLOCK_WARANG_CITI',
    'BLOCK_DIVES_AKURU',
    'BLOCK_NANDINAGARI',
    'BLOCK_ZANABAZAR_SQUARE',
    'BLOCK_SOYOMBO',
    'BLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED_A',
    'BLOCK_PAU_CIN_HAU',
    'BLOCK_DEVANAGARI_EXTENDED_A',
    'BLOCK_SHARADA_SUPPLEMENT',
    'BLOCK_SUNUWAR',
    'BLOCK_BHAIKSUKI',
    'BLOCK_MARCHEN',
    'BLOCK_MASARAM_GONDI',
    'BLOCK_GUNJALA_GONDI',
    'BLOCK_TOLONG_SIKI',
    'BLOCK_BENGALI_SUPPLEMENT',
    'BLOCK_MAKASAR',
    'BLOCK_KAWI',
    'BLOCK_LISU_SUPPLEMENT',
    'BLOCK_TAMIL_SUPPLEMENT',
    'BLOCK_CUNEIFORM',
    'BLOCK_CUNEIFORM_NUMBERS_AND_PUNCTUATION',
    'BLOCK_EARLY_DYNASTIC_CUNEIFORM',
    'BLOCK_ARCHAIC_CUNEIFORM_NUMERALS',
    'BLOCK_CYPRO_MINOAN',
    'BLOCK_EGYPTIAN_HIEROGLYPHS',
    'BLOCK_EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS',
    'BLOCK_EGYPTIAN_HIEROGLYPHS_EXTENDED_A',
    'BLOCK_ANATOLIAN_HIEROGLYPHS',
    'BLOCK_GURUNG_KHEMA',
    'BLOCK_BAMUM_SUPPLEMENT',
    'BLOCK_MRO',
    'BLOCK_TANGSA',
    'BLOCK_BASSA_VAH',
    'BLOCK_PAHAWH_HMONG',
    'BLOCK_KIRAT_RAI',
    'BLOCK_MEDEFAIDRIN',
    'BLOCK_BERIA_ERFE',
    'BLOCK_MIAO',
    'BLOCK_IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION',
    'BLOCK_TANGUT',
    'BLOCK_TANGUT_COMPONENTS',
    'BLOCK_KHITAN_SMALL_SCRIPT',
    'BLOCK_TANGUT_SUPPLEMENT',
    'BLOCK_TANGUT_COMPONENTS_SUPPLEMENT',
    'BLOCK_JURCHEN',
    'BLOCK_JURCHEN_RADICALS',
    'BLOCK_KANA_EXTENDED_B',
    'BLOCK_KANA_SUPPLEMENT',
    'BLOCK_KANA_EXTENDED_A',
    'BLOCK_SMALL_KANA_EXTENSION',
    'BLOCK_NUSHU',
    'BLOCK_DUPLOYAN',
    'BLOCK_SHORTHAND_FORMAT_CONTROLS',
    'BLOCK_SYMBOLS_FOR_LEGACY_COMPUTING_SUPPLEMENT',
    'BLOCK_MISCELLANEOUS_SYMBOLS_SUPPLEMENT',
    'BLOCK_ZNAMENNY_MUSICAL_NOTATION',
    'BLOCK_BYZANTINE_MUSICAL_SYMBOLS',
    'BLOCK_MUSICAL_SYMBOLS',
    'BLOCK_ANCIENT_GREEK_MUSICAL_NOTATION',
    'BLOCK_MUSICAL_SYMBOLS_SUPPLEMENT',
    'BLOCK_KAKTOVIK_NUMERALS',
    'BLOCK_MAYAN_NUMERALS',
    'BLOCK_TAI_XUAN_JING_SYMBOLS',
    'BLOCK_COUNTING_ROD_NUMERALS',
    'BLOCK_MATHEMATICAL_ALPHANUMERIC_SYMBOLS',
    'BLOCK_SUTTON_SIGNWRITING',
    'BLOCK_MISCELLANEOUS_SYMBOLS_AND_ARROWS_EXTENDED',
    'BLOCK_LATIN_EXTENDED_G',
    'BLOCK_GLAGOLITIC_SUPPLEMENT',
    'BLOCK_CYRILLIC_EXTENDED_D',
    'BLOCK_NYIAKENG_PUACHUE_HMONG',
    'BLOCK_TOTO',
    'BLOCK_WANCHO',
    'BLOCK_NAG_MUNDARI',
    'BLOCK_OL_ONAL',
    'BLOCK_TAI_YO',
    'BLOCK_ETHIOPIC_EXTENDED_B',
    'BLOCK_MENDE_KIKAKUI',
    'BLOCK_ADLAM',
    'BLOCK_INDIC_SIYAQ_NUMBERS',
    'BLOCK_OTTOMAN_SIYAQ_NUMBERS',
    'BLOCK_ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS',
    'BLOCK_MAHJONG_TILES',
    'BLOCK_DOMINO_TILES',
    'BLOCK_PLAYING_CARDS',
    'BLOCK_ENCLOSED_ALPHANUMERIC_SUPPLEMENT',
    'BLOCK_ENCLOSED_IDEOGRAPHIC_SUPPLEMENT',
    'BLOCK_MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS',
    'BLOCK_EMOTICONS',
    'BLOCK_ORNAMENTAL_DINGBATS',
    'BLOCK_TRANSPORT_AND_MAP_SYMBOLS',
    'BLOCK_ALCHEMICAL_SYMBOLS',
    'BLOCK_GEOMETRIC_SHAPES_EXTENDED',
    'BLOCK_SUPPLEMENTAL_ARROWS_C',
    'BLOCK_SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS',
    'BLOCK_CHESS_SYMBOLS',
    'BLOCK_SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A',
    'BLOCK_SYMBOLS_FOR_LEGACY_COMPUTING',
    'BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B',
    'BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C',
    'BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D',
    'BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E',
    'BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F',
    'BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_I',
    'BLOCK_CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT',
    'BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G',
    'BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_H',
    'BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_J',
    'BLOCK_SEAL',
    'BLOCK_TAGS',
    'BLOCK_VARIATION_SELECTORS_SUPPLEMENT',
    'BLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_A',
    'BLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_B',
    'BLOCKS',
]

UNICODE_VERSION: Final = '18.0.0'

BLOCK_BASIC_LATIN: Final = UnicodeBlock(0x0000, 0x007F, 'Basic Latin')
BLOCK_LATIN_1_SUPPLEMENT: Final = UnicodeBlock(0x0080, 0x00FF, 'Latin-1 Supplement')
BLOCK_LATIN_EXTENDED_A: Final = UnicodeBlock(0x0100, 0x017F, 'Latin Extended-A')
BLOCK_LATIN_EXTENDED_B: Final = UnicodeBlock(0x0180, 0x024F, 'Latin Extended-B')
BLOCK_IPA_EXTENSIONS: Final = UnicodeBlock(0x0250, 0x02AF, 'IPA Extensions')
BLOCK_SPACING_MODIFIER_LETTERS: Final = UnicodeBlock(0x02B0, 0x02FF, 'Spacing Modifier Letters')
BLOCK_COMBINING_DIACRITICAL_MARKS: Final = UnicodeBlock(0x0300, 0x036F, 'Combining Diacritical Marks')
BLOCK_GREEK_AND_COPTIC: Final = UnicodeBlock(0x0370, 0x03FF, 'Greek and Coptic')
BLOCK_CYRILLIC: Final = UnicodeBlock(0x0400, 0x04FF, 'Cyrillic')
BLOCK_CYRILLIC_SUPPLEMENT: Final = UnicodeBlock(0x0500, 0x052F, 'Cyrillic Supplement')
BLOCK_ARMENIAN: Final = UnicodeBlock(0x0530, 0x058F, 'Armenian')
BLOCK_HEBREW: Final = UnicodeBlock(0x0590, 0x05FF, 'Hebrew')
BLOCK_ARABIC: Final = UnicodeBlock(0x0600, 0x06FF, 'Arabic')
BLOCK_SYRIAC: Final = UnicodeBlock(0x0700, 0x074F, 'Syriac')
BLOCK_ARABIC_SUPPLEMENT: Final = UnicodeBlock(0x0750, 0x077F, 'Arabic Supplement')
BLOCK_THAANA: Final = UnicodeBlock(0x0780, 0x07BF, 'Thaana')
BLOCK_NKO: Final = UnicodeBlock(0x07C0, 0x07FF, 'NKo')
BLOCK_SAMARITAN: Final = UnicodeBlock(0x0800, 0x083F, 'Samaritan')
BLOCK_MANDAIC: Final = UnicodeBlock(0x0840, 0x085F, 'Mandaic')
BLOCK_SYRIAC_SUPPLEMENT: Final = UnicodeBlock(0x0860, 0x086F, 'Syriac Supplement')
BLOCK_ARABIC_EXTENDED_B: Final = UnicodeBlock(0x0870, 0x089F, 'Arabic Extended-B')
BLOCK_ARABIC_EXTENDED_A: Final = UnicodeBlock(0x08A0, 0x08FF, 'Arabic Extended-A')
BLOCK_DEVANAGARI: Final = UnicodeBlock(0x0900, 0x097F, 'Devanagari')
BLOCK_BENGALI: Final = UnicodeBlock(0x0980, 0x09FF, 'Bengali')
BLOCK_GURMUKHI: Final = UnicodeBlock(0x0A00, 0x0A7F, 'Gurmukhi')
BLOCK_GUJARATI: Final = UnicodeBlock(0x0A80, 0x0AFF, 'Gujarati')
BLOCK_ORIYA: Final = UnicodeBlock(0x0B00, 0x0B7F, 'Oriya')
BLOCK_TAMIL: Final = UnicodeBlock(0x0B80, 0x0BFF, 'Tamil')
BLOCK_TELUGU: Final = UnicodeBlock(0x0C00, 0x0C7F, 'Telugu')
BLOCK_KANNADA: Final = UnicodeBlock(0x0C80, 0x0CFF, 'Kannada')
BLOCK_MALAYALAM: Final = UnicodeBlock(0x0D00, 0x0D7F, 'Malayalam')
BLOCK_SINHALA: Final = UnicodeBlock(0x0D80, 0x0DFF, 'Sinhala')
BLOCK_THAI: Final = UnicodeBlock(0x0E00, 0x0E7F, 'Thai')
BLOCK_LAO: Final = UnicodeBlock(0x0E80, 0x0EFF, 'Lao')
BLOCK_TIBETAN: Final = UnicodeBlock(0x0F00, 0x0FFF, 'Tibetan')
BLOCK_MYANMAR: Final = UnicodeBlock(0x1000, 0x109F, 'Myanmar')
BLOCK_GEORGIAN: Final = UnicodeBlock(0x10A0, 0x10FF, 'Georgian')
BLOCK_HANGUL_JAMO: Final = UnicodeBlock(0x1100, 0x11FF, 'Hangul Jamo')
BLOCK_ETHIOPIC: Final = UnicodeBlock(0x1200, 0x137F, 'Ethiopic')
BLOCK_ETHIOPIC_SUPPLEMENT: Final = UnicodeBlock(0x1380, 0x139F, 'Ethiopic Supplement')
BLOCK_CHEROKEE: Final = UnicodeBlock(0x13A0, 0x13FF, 'Cherokee')
BLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS: Final = UnicodeBlock(0x1400, 0x167F, 'Unified Canadian Aboriginal Syllabics')
BLOCK_OGHAM: Final = UnicodeBlock(0x1680, 0x169F, 'Ogham')
BLOCK_RUNIC: Final = UnicodeBlock(0x16A0, 0x16FF, 'Runic')
BLOCK_TAGALOG: Final = UnicodeBlock(0x1700, 0x171F, 'Tagalog')
BLOCK_HANUNOO: Final = UnicodeBlock(0x1720, 0x173F, 'Hanunoo')
BLOCK_BUHID: Final = UnicodeBlock(0x1740, 0x175F, 'Buhid')
BLOCK_TAGBANWA: Final = UnicodeBlock(0x1760, 0x177F, 'Tagbanwa')
BLOCK_KHMER: Final = UnicodeBlock(0x1780, 0x17FF, 'Khmer')
BLOCK_MONGOLIAN: Final = UnicodeBlock(0x1800, 0x18AF, 'Mongolian')
BLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED: Final = UnicodeBlock(0x18B0, 0x18FF, 'Unified Canadian Aboriginal Syllabics Extended')
BLOCK_LIMBU: Final = UnicodeBlock(0x1900, 0x194F, 'Limbu')
BLOCK_TAI_LE: Final = UnicodeBlock(0x1950, 0x197F, 'Tai Le')
BLOCK_NEW_TAI_LUE: Final = UnicodeBlock(0x1980, 0x19DF, 'New Tai Lue')
BLOCK_KHMER_SYMBOLS: Final = UnicodeBlock(0x19E0, 0x19FF, 'Khmer Symbols')
BLOCK_BUGINESE: Final = UnicodeBlock(0x1A00, 0x1A1F, 'Buginese')
BLOCK_TAI_THAM: Final = UnicodeBlock(0x1A20, 0x1AAF, 'Tai Tham')
BLOCK_COMBINING_DIACRITICAL_MARKS_EXTENDED: Final = UnicodeBlock(0x1AB0, 0x1AFF, 'Combining Diacritical Marks Extended')
BLOCK_BALINESE: Final = UnicodeBlock(0x1B00, 0x1B7F, 'Balinese')
BLOCK_SUNDANESE: Final = UnicodeBlock(0x1B80, 0x1BBF, 'Sundanese')
BLOCK_BATAK: Final = UnicodeBlock(0x1BC0, 0x1BFF, 'Batak')
BLOCK_LEPCHA: Final = UnicodeBlock(0x1C00, 0x1C4F, 'Lepcha')
BLOCK_OL_CHIKI: Final = UnicodeBlock(0x1C50, 0x1C7F, 'Ol Chiki')
BLOCK_CYRILLIC_EXTENDED_C: Final = UnicodeBlock(0x1C80, 0x1C8F, 'Cyrillic Extended-C')
BLOCK_GEORGIAN_EXTENDED: Final = UnicodeBlock(0x1C90, 0x1CBF, 'Georgian Extended')
BLOCK_SUNDANESE_SUPPLEMENT: Final = UnicodeBlock(0x1CC0, 0x1CCF, 'Sundanese Supplement')
BLOCK_VEDIC_EXTENSIONS: Final = UnicodeBlock(0x1CD0, 0x1CFF, 'Vedic Extensions')
BLOCK_PHONETIC_EXTENSIONS: Final = UnicodeBlock(0x1D00, 0x1D7F, 'Phonetic Extensions')
BLOCK_PHONETIC_EXTENSIONS_SUPPLEMENT: Final = UnicodeBlock(0x1D80, 0x1DBF, 'Phonetic Extensions Supplement')
BLOCK_COMBINING_DIACRITICAL_MARKS_SUPPLEMENT: Final = UnicodeBlock(0x1DC0, 0x1DFF, 'Combining Diacritical Marks Supplement')
BLOCK_LATIN_EXTENDED_ADDITIONAL: Final = UnicodeBlock(0x1E00, 0x1EFF, 'Latin Extended Additional')
BLOCK_GREEK_EXTENDED: Final = UnicodeBlock(0x1F00, 0x1FFF, 'Greek Extended')
BLOCK_GENERAL_PUNCTUATION: Final = UnicodeBlock(0x2000, 0x206F, 'General Punctuation')
BLOCK_SUPERSCRIPTS_AND_SUBSCRIPTS: Final = UnicodeBlock(0x2070, 0x209F, 'Superscripts and Subscripts')
BLOCK_CURRENCY_SYMBOLS: Final = UnicodeBlock(0x20A0, 0x20CF, 'Currency Symbols')
BLOCK_COMBINING_DIACRITICAL_MARKS_FOR_SYMBOLS: Final = UnicodeBlock(0x20D0, 0x20FF, 'Combining Diacritical Marks for Symbols')
BLOCK_LETTERLIKE_SYMBOLS: Final = UnicodeBlock(0x2100, 0x214F, 'Letterlike Symbols')
BLOCK_NUMBER_FORMS: Final = UnicodeBlock(0x2150, 0x218F, 'Number Forms')
BLOCK_ARROWS: Final = UnicodeBlock(0x2190, 0x21FF, 'Arrows')
BLOCK_MATHEMATICAL_OPERATORS: Final = UnicodeBlock(0x2200, 0x22FF, 'Mathematical Operators')
BLOCK_MISCELLANEOUS_TECHNICAL: Final = UnicodeBlock(0x2300, 0x23FF, 'Miscellaneous Technical')
BLOCK_CONTROL_PICTURES: Final = UnicodeBlock(0x2400, 0x243F, 'Control Pictures')
BLOCK_OPTICAL_CHARACTER_RECOGNITION: Final = UnicodeBlock(0x2440, 0x245F, 'Optical Character Recognition')
BLOCK_ENCLOSED_ALPHANUMERICS: Final = UnicodeBlock(0x2460, 0x24FF, 'Enclosed Alphanumerics')
BLOCK_BOX_DRAWING: Final = UnicodeBlock(0x2500, 0x257F, 'Box Drawing')
BLOCK_BLOCK_ELEMENTS: Final = UnicodeBlock(0x2580, 0x259F, 'Block Elements')
BLOCK_GEOMETRIC_SHAPES: Final = UnicodeBlock(0x25A0, 0x25FF, 'Geometric Shapes')
BLOCK_MISCELLANEOUS_SYMBOLS: Final = UnicodeBlock(0x2600, 0x26FF, 'Miscellaneous Symbols')
BLOCK_DINGBATS: Final = UnicodeBlock(0x2700, 0x27BF, 'Dingbats')
BLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A: Final = UnicodeBlock(0x27C0, 0x27EF, 'Miscellaneous Mathematical Symbols-A')
BLOCK_SUPPLEMENTAL_ARROWS_A: Final = UnicodeBlock(0x27F0, 0x27FF, 'Supplemental Arrows-A')
BLOCK_BRAILLE_PATTERNS: Final = UnicodeBlock(0x2800, 0x28FF, 'Braille Patterns')
BLOCK_SUPPLEMENTAL_ARROWS_B: Final = UnicodeBlock(0x2900, 0x297F, 'Supplemental Arrows-B')
BLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B: Final = UnicodeBlock(0x2980, 0x29FF, 'Miscellaneous Mathematical Symbols-B')
BLOCK_SUPPLEMENTAL_MATHEMATICAL_OPERATORS: Final = UnicodeBlock(0x2A00, 0x2AFF, 'Supplemental Mathematical Operators')
BLOCK_MISCELLANEOUS_SYMBOLS_AND_ARROWS: Final = UnicodeBlock(0x2B00, 0x2BFF, 'Miscellaneous Symbols and Arrows')
BLOCK_GLAGOLITIC: Final = UnicodeBlock(0x2C00, 0x2C5F, 'Glagolitic')
BLOCK_LATIN_EXTENDED_C: Final = UnicodeBlock(0x2C60, 0x2C7F, 'Latin Extended-C')
BLOCK_COPTIC: Final = UnicodeBlock(0x2C80, 0x2CFF, 'Coptic')
BLOCK_GEORGIAN_SUPPLEMENT: Final = UnicodeBlock(0x2D00, 0x2D2F, 'Georgian Supplement')
BLOCK_TIFINAGH: Final = UnicodeBlock(0x2D30, 0x2D7F, 'Tifinagh')
BLOCK_ETHIOPIC_EXTENDED: Final = UnicodeBlock(0x2D80, 0x2DDF, 'Ethiopic Extended')
BLOCK_CYRILLIC_EXTENDED_A: Final = UnicodeBlock(0x2DE0, 0x2DFF, 'Cyrillic Extended-A')
BLOCK_SUPPLEMENTAL_PUNCTUATION: Final = UnicodeBlock(0x2E00, 0x2E7F, 'Supplemental Punctuation')
BLOCK_CJK_RADICALS_SUPPLEMENT: Final = UnicodeBlock(0x2E80, 0x2EFF, 'CJK Radicals Supplement')
BLOCK_KANGXI_RADICALS: Final = UnicodeBlock(0x2F00, 0x2FDF, 'Kangxi Radicals')
BLOCK_IDEOGRAPHIC_DESCRIPTION_CHARACTERS: Final = UnicodeBlock(0x2FF0, 0x2FFF, 'Ideographic Description Characters')
BLOCK_CJK_SYMBOLS_AND_PUNCTUATION: Final = UnicodeBlock(0x3000, 0x303F, 'CJK Symbols and Punctuation')
BLOCK_HIRAGANA: Final = UnicodeBlock(0x3040, 0x309F, 'Hiragana')
BLOCK_KATAKANA: Final = UnicodeBlock(0x30A0, 0x30FF, 'Katakana')
BLOCK_BOPOMOFO: Final = UnicodeBlock(0x3100, 0x312F, 'Bopomofo')
BLOCK_HANGUL_COMPATIBILITY_JAMO: Final = UnicodeBlock(0x3130, 0x318F, 'Hangul Compatibility Jamo')
BLOCK_KANBUN: Final = UnicodeBlock(0x3190, 0x319F, 'Kanbun')
BLOCK_BOPOMOFO_EXTENDED: Final = UnicodeBlock(0x31A0, 0x31BF, 'Bopomofo Extended')
BLOCK_CJK_STROKES: Final = UnicodeBlock(0x31C0, 0x31EF, 'CJK Strokes')
BLOCK_KATAKANA_PHONETIC_EXTENSIONS: Final = UnicodeBlock(0x31F0, 0x31FF, 'Katakana Phonetic Extensions')
BLOCK_ENCLOSED_CJK_LETTERS_AND_MONTHS: Final = UnicodeBlock(0x3200, 0x32FF, 'Enclosed CJK Letters and Months')
BLOCK_CJK_COMPATIBILITY: Final = UnicodeBlock(0x3300, 0x33FF, 'CJK Compatibility')
BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A: Final = UnicodeBlock(0x3400, 0x4DBF, 'CJK Unified Ideographs Extension A')
BLOCK_YIJING_HEXAGRAM_SYMBOLS: Final = UnicodeBlock(0x4DC0, 0x4DFF, 'Yijing Hexagram Symbols')
BLOCK_CJK_UNIFIED_IDEOGRAPHS: Final = UnicodeBlock(0x4E00, 0x9FFF, 'CJK Unified Ideographs')
BLOCK_YI_SYLLABLES: Final = UnicodeBlock(0xA000, 0xA48F, 'Yi Syllables')
BLOCK_YI_RADICALS: Final = UnicodeBlock(0xA490, 0xA4CF, 'Yi Radicals')
BLOCK_LISU: Final = UnicodeBlock(0xA4D0, 0xA4FF, 'Lisu')
BLOCK_VAI: Final = UnicodeBlock(0xA500, 0xA63F, 'Vai')
BLOCK_CYRILLIC_EXTENDED_B: Final = UnicodeBlock(0xA640, 0xA69F, 'Cyrillic Extended-B')
BLOCK_BAMUM: Final = UnicodeBlock(0xA6A0, 0xA6FF, 'Bamum')
BLOCK_MODIFIER_TONE_LETTERS: Final = UnicodeBlock(0xA700, 0xA71F, 'Modifier Tone Letters')
BLOCK_LATIN_EXTENDED_D: Final = UnicodeBlock(0xA720, 0xA7FF, 'Latin Extended-D')
BLOCK_SYLOTI_NAGRI: Final = UnicodeBlock(0xA800, 0xA82F, 'Syloti Nagri')
BLOCK_COMMON_INDIC_NUMBER_FORMS: Final = UnicodeBlock(0xA830, 0xA83F, 'Common Indic Number Forms')
BLOCK_PHAGS_PA: Final = UnicodeBlock(0xA840, 0xA87F, 'Phags-pa')
BLOCK_SAURASHTRA: Final = UnicodeBlock(0xA880, 0xA8DF, 'Saurashtra')
BLOCK_DEVANAGARI_EXTENDED: Final = UnicodeBlock(0xA8E0, 0xA8FF, 'Devanagari Extended')
BLOCK_KAYAH_LI: Final = UnicodeBlock(0xA900, 0xA92F, 'Kayah Li')
BLOCK_REJANG: Final = UnicodeBlock(0xA930, 0xA95F, 'Rejang')
BLOCK_HANGUL_JAMO_EXTENDED_A: Final = UnicodeBlock(0xA960, 0xA97F, 'Hangul Jamo Extended-A')
BLOCK_JAVANESE: Final = UnicodeBlock(0xA980, 0xA9DF, 'Javanese')
BLOCK_MYANMAR_EXTENDED_B: Final = UnicodeBlock(0xA9E0, 0xA9FF, 'Myanmar Extended-B')
BLOCK_CHAM: Final = UnicodeBlock(0xAA00, 0xAA5F, 'Cham')
BLOCK_MYANMAR_EXTENDED_A: Final = UnicodeBlock(0xAA60, 0xAA7F, 'Myanmar Extended-A')
BLOCK_TAI_VIET: Final = UnicodeBlock(0xAA80, 0xAADF, 'Tai Viet')
BLOCK_MEETEI_MAYEK_EXTENSIONS: Final = UnicodeBlock(0xAAE0, 0xAAFF, 'Meetei Mayek Extensions')
BLOCK_ETHIOPIC_EXTENDED_A: Final = UnicodeBlock(0xAB00, 0xAB2F, 'Ethiopic Extended-A')
BLOCK_LATIN_EXTENDED_E: Final = UnicodeBlock(0xAB30, 0xAB6F, 'Latin Extended-E')
BLOCK_CHEROKEE_SUPPLEMENT: Final = UnicodeBlock(0xAB70, 0xABBF, 'Cherokee Supplement')
BLOCK_MEETEI_MAYEK: Final = UnicodeBlock(0xABC0, 0xABFF, 'Meetei Mayek')
BLOCK_HANGUL_SYLLABLES: Final = UnicodeBlock(0xAC00, 0xD7AF, 'Hangul Syllables')
BLOCK_HANGUL_JAMO_EXTENDED_B: Final = UnicodeBlock(0xD7B0, 0xD7FF, 'Hangul Jamo Extended-B')
BLOCK_HIGH_SURROGATES: Final = UnicodeBlock(0xD800, 0xDB7F, 'High Surrogates')
BLOCK_HIGH_PRIVATE_USE_SURROGATES: Final = UnicodeBlock(0xDB80, 0xDBFF, 'High Private Use Surrogates')
BLOCK_LOW_SURROGATES: Final = UnicodeBlock(0xDC00, 0xDFFF, 'Low Surrogates')
BLOCK_PRIVATE_USE_AREA: Final = UnicodeBlock(0xE000, 0xF8FF, 'Private Use Area')
BLOCK_CJK_COMPATIBILITY_IDEOGRAPHS: Final = UnicodeBlock(0xF900, 0xFAFF, 'CJK Compatibility Ideographs')
BLOCK_ALPHABETIC_PRESENTATION_FORMS: Final = UnicodeBlock(0xFB00, 0xFB4F, 'Alphabetic Presentation Forms')
BLOCK_ARABIC_PRESENTATION_FORMS_A: Final = UnicodeBlock(0xFB50, 0xFDFF, 'Arabic Presentation Forms-A')
BLOCK_VARIATION_SELECTORS: Final = UnicodeBlock(0xFE00, 0xFE0F, 'Variation Selectors')
BLOCK_VERTICAL_FORMS: Final = UnicodeBlock(0xFE10, 0xFE1F, 'Vertical Forms')
BLOCK_COMBINING_HALF_MARKS: Final = UnicodeBlock(0xFE20, 0xFE2F, 'Combining Half Marks')
BLOCK_CJK_COMPATIBILITY_FORMS: Final = UnicodeBlock(0xFE30, 0xFE4F, 'CJK Compatibility Forms')
BLOCK_SMALL_FORM_VARIANTS: Final = UnicodeBlock(0xFE50, 0xFE6F, 'Small Form Variants')
BLOCK_ARABIC_PRESENTATION_FORMS_B: Final = UnicodeBlock(0xFE70, 0xFEFF, 'Arabic Presentation Forms-B')
BLOCK_HALFWIDTH_AND_FULLWIDTH_FORMS: Final = UnicodeBlock(0xFF00, 0xFFEF, 'Halfwidth and Fullwidth Forms')
BLOCK_SPECIALS: Final = UnicodeBlock(0xFFF0, 0xFFFF, 'Specials')
BLOCK_LINEAR_B_SYLLABARY: Final = UnicodeBlock(0x10000, 0x1007F, 'Linear B Syllabary')
BLOCK_LINEAR_B_IDEOGRAMS: Final = UnicodeBlock(0x10080, 0x100FF, 'Linear B Ideograms')
BLOCK_AEGEAN_NUMBERS: Final = UnicodeBlock(0x10100, 0x1013F, 'Aegean Numbers')
BLOCK_ANCIENT_GREEK_NUMBERS: Final = UnicodeBlock(0x10140, 0x1018F, 'Ancient Greek Numbers')
BLOCK_ANCIENT_SYMBOLS: Final = UnicodeBlock(0x10190, 0x101CF, 'Ancient Symbols')
BLOCK_PHAISTOS_DISC: Final = UnicodeBlock(0x101D0, 0x101FF, 'Phaistos Disc')
BLOCK_LYCIAN: Final = UnicodeBlock(0x10280, 0x1029F, 'Lycian')
BLOCK_CARIAN: Final = UnicodeBlock(0x102A0, 0x102DF, 'Carian')
BLOCK_COPTIC_EPACT_NUMBERS: Final = UnicodeBlock(0x102E0, 0x102FF, 'Coptic Epact Numbers')
BLOCK_OLD_ITALIC: Final = UnicodeBlock(0x10300, 0x1032F, 'Old Italic')
BLOCK_GOTHIC: Final = UnicodeBlock(0x10330, 0x1034F, 'Gothic')
BLOCK_OLD_PERMIC: Final = UnicodeBlock(0x10350, 0x1037F, 'Old Permic')
BLOCK_UGARITIC: Final = UnicodeBlock(0x10380, 0x1039F, 'Ugaritic')
BLOCK_OLD_PERSIAN: Final = UnicodeBlock(0x103A0, 0x103DF, 'Old Persian')
BLOCK_DESERET: Final = UnicodeBlock(0x10400, 0x1044F, 'Deseret')
BLOCK_SHAVIAN: Final = UnicodeBlock(0x10450, 0x1047F, 'Shavian')
BLOCK_OSMANYA: Final = UnicodeBlock(0x10480, 0x104AF, 'Osmanya')
BLOCK_OSAGE: Final = UnicodeBlock(0x104B0, 0x104FF, 'Osage')
BLOCK_ELBASAN: Final = UnicodeBlock(0x10500, 0x1052F, 'Elbasan')
BLOCK_CAUCASIAN_ALBANIAN: Final = UnicodeBlock(0x10530, 0x1056F, 'Caucasian Albanian')
BLOCK_VITHKUQI: Final = UnicodeBlock(0x10570, 0x105BF, 'Vithkuqi')
BLOCK_TODHRI: Final = UnicodeBlock(0x105C0, 0x105FF, 'Todhri')
BLOCK_LINEAR_A: Final = UnicodeBlock(0x10600, 0x1077F, 'Linear A')
BLOCK_LATIN_EXTENDED_F: Final = UnicodeBlock(0x10780, 0x107BF, 'Latin Extended-F')
BLOCK_CYPRIOT_SYLLABARY: Final = UnicodeBlock(0x10800, 0x1083F, 'Cypriot Syllabary')
BLOCK_IMPERIAL_ARAMAIC: Final = UnicodeBlock(0x10840, 0x1085F, 'Imperial Aramaic')
BLOCK_PALMYRENE: Final = UnicodeBlock(0x10860, 0x1087F, 'Palmyrene')
BLOCK_NABATAEAN: Final = UnicodeBlock(0x10880, 0x108AF, 'Nabataean')
BLOCK_HATRAN: Final = UnicodeBlock(0x108E0, 0x108FF, 'Hatran')
BLOCK_PHOENICIAN: Final = UnicodeBlock(0x10900, 0x1091F, 'Phoenician')
BLOCK_LYDIAN: Final = UnicodeBlock(0x10920, 0x1093F, 'Lydian')
BLOCK_SIDETIC: Final = UnicodeBlock(0x10940, 0x1095F, 'Sidetic')
BLOCK_MEROITIC_HIEROGLYPHS: Final = UnicodeBlock(0x10980, 0x1099F, 'Meroitic Hieroglyphs')
BLOCK_MEROITIC_CURSIVE: Final = UnicodeBlock(0x109A0, 0x109FF, 'Meroitic Cursive')
BLOCK_KHAROSHTHI: Final = UnicodeBlock(0x10A00, 0x10A5F, 'Kharoshthi')
BLOCK_OLD_SOUTH_ARABIAN: Final = UnicodeBlock(0x10A60, 0x10A7F, 'Old South Arabian')
BLOCK_OLD_NORTH_ARABIAN: Final = UnicodeBlock(0x10A80, 0x10A9F, 'Old North Arabian')
BLOCK_MANICHAEAN: Final = UnicodeBlock(0x10AC0, 0x10AFF, 'Manichaean')
BLOCK_AVESTAN: Final = UnicodeBlock(0x10B00, 0x10B3F, 'Avestan')
BLOCK_INSCRIPTIONAL_PARTHIAN: Final = UnicodeBlock(0x10B40, 0x10B5F, 'Inscriptional Parthian')
BLOCK_INSCRIPTIONAL_PAHLAVI: Final = UnicodeBlock(0x10B60, 0x10B7F, 'Inscriptional Pahlavi')
BLOCK_PSALTER_PAHLAVI: Final = UnicodeBlock(0x10B80, 0x10BAF, 'Psalter Pahlavi')
BLOCK_OLD_TURKIC: Final = UnicodeBlock(0x10C00, 0x10C4F, 'Old Turkic')
BLOCK_OLD_HUNGARIAN: Final = UnicodeBlock(0x10C80, 0x10CFF, 'Old Hungarian')
BLOCK_HANIFI_ROHINGYA: Final = UnicodeBlock(0x10D00, 0x10D3F, 'Hanifi Rohingya')
BLOCK_GARAY: Final = UnicodeBlock(0x10D40, 0x10D8F, 'Garay')
BLOCK_RUMI_NUMERAL_SYMBOLS: Final = UnicodeBlock(0x10E60, 0x10E7F, 'Rumi Numeral Symbols')
BLOCK_YEZIDI: Final = UnicodeBlock(0x10E80, 0x10EBF, 'Yezidi')
BLOCK_ARABIC_EXTENDED_C: Final = UnicodeBlock(0x10EC0, 0x10EFF, 'Arabic Extended-C')
BLOCK_OLD_SOGDIAN: Final = UnicodeBlock(0x10F00, 0x10F2F, 'Old Sogdian')
BLOCK_SOGDIAN: Final = UnicodeBlock(0x10F30, 0x10F6F, 'Sogdian')
BLOCK_OLD_UYGHUR: Final = UnicodeBlock(0x10F70, 0x10FAF, 'Old Uyghur')
BLOCK_CHORASMIAN: Final = UnicodeBlock(0x10FB0, 0x10FDF, 'Chorasmian')
BLOCK_ELYMAIC: Final = UnicodeBlock(0x10FE0, 0x10FFF, 'Elymaic')
BLOCK_BRAHMI: Final = UnicodeBlock(0x11000, 0x1107F, 'Brahmi')
BLOCK_KAITHI: Final = UnicodeBlock(0x11080, 0x110CF, 'Kaithi')
BLOCK_SORA_SOMPENG: Final = UnicodeBlock(0x110D0, 0x110FF, 'Sora Sompeng')
BLOCK_CHAKMA: Final = UnicodeBlock(0x11100, 0x1114F, 'Chakma')
BLOCK_MAHAJANI: Final = UnicodeBlock(0x11150, 0x1117F, 'Mahajani')
BLOCK_SHARADA: Final = UnicodeBlock(0x11180, 0x111DF, 'Sharada')
BLOCK_SINHALA_ARCHAIC_NUMBERS: Final = UnicodeBlock(0x111E0, 0x111FF, 'Sinhala Archaic Numbers')
BLOCK_KHOJKI: Final = UnicodeBlock(0x11200, 0x1124F, 'Khojki')
BLOCK_MULTANI: Final = UnicodeBlock(0x11280, 0x112AF, 'Multani')
BLOCK_KHUDAWADI: Final = UnicodeBlock(0x112B0, 0x112FF, 'Khudawadi')
BLOCK_GRANTHA: Final = UnicodeBlock(0x11300, 0x1137F, 'Grantha')
BLOCK_TULU_TIGALARI: Final = UnicodeBlock(0x11380, 0x113FF, 'Tulu-Tigalari')
BLOCK_NEWA: Final = UnicodeBlock(0x11400, 0x1147F, 'Newa')
BLOCK_TIRHUTA: Final = UnicodeBlock(0x11480, 0x114DF, 'Tirhuta')
BLOCK_SIDDHAM: Final = UnicodeBlock(0x11580, 0x115FF, 'Siddham')
BLOCK_MODI: Final = UnicodeBlock(0x11600, 0x1165F, 'Modi')
BLOCK_MONGOLIAN_SUPPLEMENT: Final = UnicodeBlock(0x11660, 0x1167F, 'Mongolian Supplement')
BLOCK_TAKRI: Final = UnicodeBlock(0x11680, 0x116CF, 'Takri')
BLOCK_MYANMAR_EXTENDED_C: Final = UnicodeBlock(0x116D0, 0x116FF, 'Myanmar Extended-C')
BLOCK_AHOM: Final = UnicodeBlock(0x11700, 0x1174F, 'Ahom')
BLOCK_DOGRA: Final = UnicodeBlock(0x11800, 0x1184F, 'Dogra')
BLOCK_WARANG_CITI: Final = UnicodeBlock(0x118A0, 0x118FF, 'Warang Citi')
BLOCK_DIVES_AKURU: Final = UnicodeBlock(0x11900, 0x1195F, 'Dives Akuru')
BLOCK_NANDINAGARI: Final = UnicodeBlock(0x119A0, 0x119FF, 'Nandinagari')
BLOCK_ZANABAZAR_SQUARE: Final = UnicodeBlock(0x11A00, 0x11A4F, 'Zanabazar Square')
BLOCK_SOYOMBO: Final = UnicodeBlock(0x11A50, 0x11AAF, 'Soyombo')
BLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED_A: Final = UnicodeBlock(0x11AB0, 0x11ABF, 'Unified Canadian Aboriginal Syllabics Extended-A')
BLOCK_PAU_CIN_HAU: Final = UnicodeBlock(0x11AC0, 0x11AFF, 'Pau Cin Hau')
BLOCK_DEVANAGARI_EXTENDED_A: Final = UnicodeBlock(0x11B00, 0x11B5F, 'Devanagari Extended-A')
BLOCK_SHARADA_SUPPLEMENT: Final = UnicodeBlock(0x11B60, 0x11B7F, 'Sharada Supplement')
BLOCK_SUNUWAR: Final = UnicodeBlock(0x11BC0, 0x11BFF, 'Sunuwar')
BLOCK_BHAIKSUKI: Final = UnicodeBlock(0x11C00, 0x11C6F, 'Bhaiksuki')
BLOCK_MARCHEN: Final = UnicodeBlock(0x11C70, 0x11CBF, 'Marchen')
BLOCK_MASARAM_GONDI: Final = UnicodeBlock(0x11D00, 0x11D5F, 'Masaram Gondi')
BLOCK_GUNJALA_GONDI: Final = UnicodeBlock(0x11D60, 0x11DAF, 'Gunjala Gondi')
BLOCK_TOLONG_SIKI: Final = UnicodeBlock(0x11DB0, 0x11DEF, 'Tolong Siki')
BLOCK_BENGALI_SUPPLEMENT: Final = UnicodeBlock(0x11DF0, 0x11DFF, 'Bengali Supplement')
BLOCK_MAKASAR: Final = UnicodeBlock(0x11EE0, 0x11EFF, 'Makasar')
BLOCK_KAWI: Final = UnicodeBlock(0x11F00, 0x11F5F, 'Kawi')
BLOCK_LISU_SUPPLEMENT: Final = UnicodeBlock(0x11FB0, 0x11FBF, 'Lisu Supplement')
BLOCK_TAMIL_SUPPLEMENT: Final = UnicodeBlock(0x11FC0, 0x11FFF, 'Tamil Supplement')
BLOCK_CUNEIFORM: Final = UnicodeBlock(0x12000, 0x123FF, 'Cuneiform')
BLOCK_CUNEIFORM_NUMBERS_AND_PUNCTUATION: Final = UnicodeBlock(0x12400, 0x1247F, 'Cuneiform Numbers and Punctuation')
BLOCK_EARLY_DYNASTIC_CUNEIFORM: Final = UnicodeBlock(0x12480, 0x1254F, 'Early Dynastic Cuneiform')
BLOCK_ARCHAIC_CUNEIFORM_NUMERALS: Final = UnicodeBlock(0x12550, 0x1268F, 'Archaic Cuneiform Numerals')
BLOCK_CYPRO_MINOAN: Final = UnicodeBlock(0x12F90, 0x12FFF, 'Cypro-Minoan')
BLOCK_EGYPTIAN_HIEROGLYPHS: Final = UnicodeBlock(0x13000, 0x1342F, 'Egyptian Hieroglyphs')
BLOCK_EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS: Final = UnicodeBlock(0x13430, 0x1345F, 'Egyptian Hieroglyph Format Controls')
BLOCK_EGYPTIAN_HIEROGLYPHS_EXTENDED_A: Final = UnicodeBlock(0x13460, 0x143FF, 'Egyptian Hieroglyphs Extended-A')
BLOCK_ANATOLIAN_HIEROGLYPHS: Final = UnicodeBlock(0x14400, 0x1467F, 'Anatolian Hieroglyphs')
BLOCK_GURUNG_KHEMA: Final = UnicodeBlock(0x16100, 0x1613F, 'Gurung Khema')
BLOCK_BAMUM_SUPPLEMENT: Final = UnicodeBlock(0x16800, 0x16A3F, 'Bamum Supplement')
BLOCK_MRO: Final = UnicodeBlock(0x16A40, 0x16A6F, 'Mro')
BLOCK_TANGSA: Final = UnicodeBlock(0x16A70, 0x16ACF, 'Tangsa')
BLOCK_BASSA_VAH: Final = UnicodeBlock(0x16AD0, 0x16AFF, 'Bassa Vah')
BLOCK_PAHAWH_HMONG: Final = UnicodeBlock(0x16B00, 0x16B8F, 'Pahawh Hmong')
BLOCK_KIRAT_RAI: Final = UnicodeBlock(0x16D40, 0x16D7F, 'Kirat Rai')
BLOCK_MEDEFAIDRIN: Final = UnicodeBlock(0x16E40, 0x16E9F, 'Medefaidrin')
BLOCK_BERIA_ERFE: Final = UnicodeBlock(0x16EA0, 0x16EDF, 'Beria Erfe')
BLOCK_MIAO: Final = UnicodeBlock(0x16F00, 0x16F9F, 'Miao')
BLOCK_IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION: Final = UnicodeBlock(0x16FE0, 0x16FFF, 'Ideographic Symbols and Punctuation')
BLOCK_TANGUT: Final = UnicodeBlock(0x17000, 0x187FF, 'Tangut')
BLOCK_TANGUT_COMPONENTS: Final = UnicodeBlock(0x18800, 0x18AFF, 'Tangut Components')
BLOCK_KHITAN_SMALL_SCRIPT: Final = UnicodeBlock(0x18B00, 0x18CFF, 'Khitan Small Script')
BLOCK_TANGUT_SUPPLEMENT: Final = UnicodeBlock(0x18D00, 0x18D7F, 'Tangut Supplement')
BLOCK_TANGUT_COMPONENTS_SUPPLEMENT: Final = UnicodeBlock(0x18D80, 0x18DFF, 'Tangut Components Supplement')
BLOCK_JURCHEN: Final = UnicodeBlock(0x18E00, 0x1919F, 'Jurchen')
BLOCK_JURCHEN_RADICALS: Final = UnicodeBlock(0x191A0, 0x191DF, 'Jurchen Radicals')
BLOCK_KANA_EXTENDED_B: Final = UnicodeBlock(0x1AFF0, 0x1AFFF, 'Kana Extended-B')
BLOCK_KANA_SUPPLEMENT: Final = UnicodeBlock(0x1B000, 0x1B0FF, 'Kana Supplement')
BLOCK_KANA_EXTENDED_A: Final = UnicodeBlock(0x1B100, 0x1B12F, 'Kana Extended-A')
BLOCK_SMALL_KANA_EXTENSION: Final = UnicodeBlock(0x1B130, 0x1B16F, 'Small Kana Extension')
BLOCK_NUSHU: Final = UnicodeBlock(0x1B170, 0x1B2FF, 'Nushu')
BLOCK_DUPLOYAN: Final = UnicodeBlock(0x1BC00, 0x1BC9F, 'Duployan')
BLOCK_SHORTHAND_FORMAT_CONTROLS: Final = UnicodeBlock(0x1BCA0, 0x1BCAF, 'Shorthand Format Controls')
BLOCK_SYMBOLS_FOR_LEGACY_COMPUTING_SUPPLEMENT: Final = UnicodeBlock(0x1CC00, 0x1CEBF, 'Symbols for Legacy Computing Supplement')
BLOCK_MISCELLANEOUS_SYMBOLS_SUPPLEMENT: Final = UnicodeBlock(0x1CEC0, 0x1CEFF, 'Miscellaneous Symbols Supplement')
BLOCK_ZNAMENNY_MUSICAL_NOTATION: Final = UnicodeBlock(0x1CF00, 0x1CFCF, 'Znamenny Musical Notation')
BLOCK_BYZANTINE_MUSICAL_SYMBOLS: Final = UnicodeBlock(0x1D000, 0x1D0FF, 'Byzantine Musical Symbols')
BLOCK_MUSICAL_SYMBOLS: Final = UnicodeBlock(0x1D100, 0x1D1FF, 'Musical Symbols')
BLOCK_ANCIENT_GREEK_MUSICAL_NOTATION: Final = UnicodeBlock(0x1D200, 0x1D24F, 'Ancient Greek Musical Notation')
BLOCK_MUSICAL_SYMBOLS_SUPPLEMENT: Final = UnicodeBlock(0x1D250, 0x1D28F, 'Musical Symbols Supplement')
BLOCK_KAKTOVIK_NUMERALS: Final = UnicodeBlock(0x1D2C0, 0x1D2DF, 'Kaktovik Numerals')
BLOCK_MAYAN_NUMERALS: Final = UnicodeBlock(0x1D2E0, 0x1D2FF, 'Mayan Numerals')
BLOCK_TAI_XUAN_JING_SYMBOLS: Final = UnicodeBlock(0x1D300, 0x1D35F, 'Tai Xuan Jing Symbols')
BLOCK_COUNTING_ROD_NUMERALS: Final = UnicodeBlock(0x1D360, 0x1D37F, 'Counting Rod Numerals')
BLOCK_MATHEMATICAL_ALPHANUMERIC_SYMBOLS: Final = UnicodeBlock(0x1D400, 0x1D7FF, 'Mathematical Alphanumeric Symbols')
BLOCK_SUTTON_SIGNWRITING: Final = UnicodeBlock(0x1D800, 0x1DAAF, 'Sutton SignWriting')
BLOCK_MISCELLANEOUS_SYMBOLS_AND_ARROWS_EXTENDED: Final = UnicodeBlock(0x1DB00, 0x1DBFF, 'Miscellaneous Symbols and Arrows Extended')
BLOCK_LATIN_EXTENDED_G: Final = UnicodeBlock(0x1DF00, 0x1DFFF, 'Latin Extended-G')
BLOCK_GLAGOLITIC_SUPPLEMENT: Final = UnicodeBlock(0x1E000, 0x1E02F, 'Glagolitic Supplement')
BLOCK_CYRILLIC_EXTENDED_D: Final = UnicodeBlock(0x1E030, 0x1E08F, 'Cyrillic Extended-D')
BLOCK_NYIAKENG_PUACHUE_HMONG: Final = UnicodeBlock(0x1E100, 0x1E14F, 'Nyiakeng Puachue Hmong')
BLOCK_TOTO: Final = UnicodeBlock(0x1E290, 0x1E2BF, 'Toto')
BLOCK_WANCHO: Final = UnicodeBlock(0x1E2C0, 0x1E2FF, 'Wancho')
BLOCK_NAG_MUNDARI: Final = UnicodeBlock(0x1E4D0, 0x1E4FF, 'Nag Mundari')
BLOCK_OL_ONAL: Final = UnicodeBlock(0x1E5D0, 0x1E5FF, 'Ol Onal')
BLOCK_TAI_YO: Final = UnicodeBlock(0x1E6C0, 0x1E6FF, 'Tai Yo')
BLOCK_ETHIOPIC_EXTENDED_B: Final = UnicodeBlock(0x1E7E0, 0x1E7FF, 'Ethiopic Extended-B')
BLOCK_MENDE_KIKAKUI: Final = UnicodeBlock(0x1E800, 0x1E8DF, 'Mende Kikakui')
BLOCK_ADLAM: Final = UnicodeBlock(0x1E900, 0x1E95F, 'Adlam')
BLOCK_INDIC_SIYAQ_NUMBERS: Final = UnicodeBlock(0x1EC70, 0x1ECBF, 'Indic Siyaq Numbers')
BLOCK_OTTOMAN_SIYAQ_NUMBERS: Final = UnicodeBlock(0x1ED00, 0x1ED4F, 'Ottoman Siyaq Numbers')
BLOCK_ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS: Final = UnicodeBlock(0x1EE00, 0x1EEFF, 'Arabic Mathematical Alphabetic Symbols')
BLOCK_MAHJONG_TILES: Final = UnicodeBlock(0x1F000, 0x1F02F, 'Mahjong Tiles')
BLOCK_DOMINO_TILES: Final = UnicodeBlock(0x1F030, 0x1F09F, 'Domino Tiles')
BLOCK_PLAYING_CARDS: Final = UnicodeBlock(0x1F0A0, 0x1F0FF, 'Playing Cards')
BLOCK_ENCLOSED_ALPHANUMERIC_SUPPLEMENT: Final = UnicodeBlock(0x1F100, 0x1F1FF, 'Enclosed Alphanumeric Supplement')
BLOCK_ENCLOSED_IDEOGRAPHIC_SUPPLEMENT: Final = UnicodeBlock(0x1F200, 0x1F2FF, 'Enclosed Ideographic Supplement')
BLOCK_MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS: Final = UnicodeBlock(0x1F300, 0x1F5FF, 'Miscellaneous Symbols and Pictographs')
BLOCK_EMOTICONS: Final = UnicodeBlock(0x1F600, 0x1F64F, 'Emoticons')
BLOCK_ORNAMENTAL_DINGBATS: Final = UnicodeBlock(0x1F650, 0x1F67F, 'Ornamental Dingbats')
BLOCK_TRANSPORT_AND_MAP_SYMBOLS: Final = UnicodeBlock(0x1F680, 0x1F6FF, 'Transport and Map Symbols')
BLOCK_ALCHEMICAL_SYMBOLS: Final = UnicodeBlock(0x1F700, 0x1F77F, 'Alchemical Symbols')
BLOCK_GEOMETRIC_SHAPES_EXTENDED: Final = UnicodeBlock(0x1F780, 0x1F7FF, 'Geometric Shapes Extended')
BLOCK_SUPPLEMENTAL_ARROWS_C: Final = UnicodeBlock(0x1F800, 0x1F8FF, 'Supplemental Arrows-C')
BLOCK_SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS: Final = UnicodeBlock(0x1F900, 0x1F9FF, 'Supplemental Symbols and Pictographs')
BLOCK_CHESS_SYMBOLS: Final = UnicodeBlock(0x1FA00, 0x1FA6F, 'Chess Symbols')
BLOCK_SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A: Final = UnicodeBlock(0x1FA70, 0x1FAFF, 'Symbols and Pictographs Extended-A')
BLOCK_SYMBOLS_FOR_LEGACY_COMPUTING: Final = UnicodeBlock(0x1FB00, 0x1FBFF, 'Symbols for Legacy Computing')
BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B: Final = UnicodeBlock(0x20000, 0x2A6DF, 'CJK Unified Ideographs Extension B')
BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C: Final = UnicodeBlock(0x2A700, 0x2B73F, 'CJK Unified Ideographs Extension C')
BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D: Final = UnicodeBlock(0x2B740, 0x2B81F, 'CJK Unified Ideographs Extension D')
BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E: Final = UnicodeBlock(0x2B820, 0x2CEAF, 'CJK Unified Ideographs Extension E')
BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F: Final = UnicodeBlock(0x2CEB0, 0x2EBEF, 'CJK Unified Ideographs Extension F')
BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_I: Final = UnicodeBlock(0x2EBF0, 0x2EE5F, 'CJK Unified Ideographs Extension I')
BLOCK_CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT: Final = UnicodeBlock(0x2F800, 0x2FA1F, 'CJK Compatibility Ideographs Supplement')
BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G: Final = UnicodeBlock(0x30000, 0x3134F, 'CJK Unified Ideographs Extension G')
BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_H: Final = UnicodeBlock(0x31350, 0x323AF, 'CJK Unified Ideographs Extension H')
BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_J: Final = UnicodeBlock(0x323B0, 0x3347F, 'CJK Unified Ideographs Extension J')
BLOCK_SEAL: Final = UnicodeBlock(0x3D000, 0x3FC3F, 'Seal')
BLOCK_TAGS: Final = UnicodeBlock(0xE0000, 0xE007F, 'Tags')
BLOCK_VARIATION_SELECTORS_SUPPLEMENT: Final = UnicodeBlock(0xE0100, 0xE01EF, 'Variation Selectors Supplement')
BLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_A: Final = UnicodeBlock(0xF0000, 0xFFFFF, 'Supplementary Private Use Area-A')
BLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_B: Final = UnicodeBlock(0x100000, 0x10FFFF, 'Supplementary Private Use Area-B')

BLOCKS: Final = (
    BLOCK_BASIC_LATIN,
    BLOCK_LATIN_1_SUPPLEMENT,
    BLOCK_LATIN_EXTENDED_A,
    BLOCK_LATIN_EXTENDED_B,
    BLOCK_IPA_EXTENSIONS,
    BLOCK_SPACING_MODIFIER_LETTERS,
    BLOCK_COMBINING_DIACRITICAL_MARKS,
    BLOCK_GREEK_AND_COPTIC,
    BLOCK_CYRILLIC,
    BLOCK_CYRILLIC_SUPPLEMENT,
    BLOCK_ARMENIAN,
    BLOCK_HEBREW,
    BLOCK_ARABIC,
    BLOCK_SYRIAC,
    BLOCK_ARABIC_SUPPLEMENT,
    BLOCK_THAANA,
    BLOCK_NKO,
    BLOCK_SAMARITAN,
    BLOCK_MANDAIC,
    BLOCK_SYRIAC_SUPPLEMENT,
    BLOCK_ARABIC_EXTENDED_B,
    BLOCK_ARABIC_EXTENDED_A,
    BLOCK_DEVANAGARI,
    BLOCK_BENGALI,
    BLOCK_GURMUKHI,
    BLOCK_GUJARATI,
    BLOCK_ORIYA,
    BLOCK_TAMIL,
    BLOCK_TELUGU,
    BLOCK_KANNADA,
    BLOCK_MALAYALAM,
    BLOCK_SINHALA,
    BLOCK_THAI,
    BLOCK_LAO,
    BLOCK_TIBETAN,
    BLOCK_MYANMAR,
    BLOCK_GEORGIAN,
    BLOCK_HANGUL_JAMO,
    BLOCK_ETHIOPIC,
    BLOCK_ETHIOPIC_SUPPLEMENT,
    BLOCK_CHEROKEE,
    BLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS,
    BLOCK_OGHAM,
    BLOCK_RUNIC,
    BLOCK_TAGALOG,
    BLOCK_HANUNOO,
    BLOCK_BUHID,
    BLOCK_TAGBANWA,
    BLOCK_KHMER,
    BLOCK_MONGOLIAN,
    BLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED,
    BLOCK_LIMBU,
    BLOCK_TAI_LE,
    BLOCK_NEW_TAI_LUE,
    BLOCK_KHMER_SYMBOLS,
    BLOCK_BUGINESE,
    BLOCK_TAI_THAM,
    BLOCK_COMBINING_DIACRITICAL_MARKS_EXTENDED,
    BLOCK_BALINESE,
    BLOCK_SUNDANESE,
    BLOCK_BATAK,
    BLOCK_LEPCHA,
    BLOCK_OL_CHIKI,
    BLOCK_CYRILLIC_EXTENDED_C,
    BLOCK_GEORGIAN_EXTENDED,
    BLOCK_SUNDANESE_SUPPLEMENT,
    BLOCK_VEDIC_EXTENSIONS,
    BLOCK_PHONETIC_EXTENSIONS,
    BLOCK_PHONETIC_EXTENSIONS_SUPPLEMENT,
    BLOCK_COMBINING_DIACRITICAL_MARKS_SUPPLEMENT,
    BLOCK_LATIN_EXTENDED_ADDITIONAL,
    BLOCK_GREEK_EXTENDED,
    BLOCK_GENERAL_PUNCTUATION,
    BLOCK_SUPERSCRIPTS_AND_SUBSCRIPTS,
    BLOCK_CURRENCY_SYMBOLS,
    BLOCK_COMBINING_DIACRITICAL_MARKS_FOR_SYMBOLS,
    BLOCK_LETTERLIKE_SYMBOLS,
    BLOCK_NUMBER_FORMS,
    BLOCK_ARROWS,
    BLOCK_MATHEMATICAL_OPERATORS,
    BLOCK_MISCELLANEOUS_TECHNICAL,
    BLOCK_CONTROL_PICTURES,
    BLOCK_OPTICAL_CHARACTER_RECOGNITION,
    BLOCK_ENCLOSED_ALPHANUMERICS,
    BLOCK_BOX_DRAWING,
    BLOCK_BLOCK_ELEMENTS,
    BLOCK_GEOMETRIC_SHAPES,
    BLOCK_MISCELLANEOUS_SYMBOLS,
    BLOCK_DINGBATS,
    BLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A,
    BLOCK_SUPPLEMENTAL_ARROWS_A,
    BLOCK_BRAILLE_PATTERNS,
    BLOCK_SUPPLEMENTAL_ARROWS_B,
    BLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B,
    BLOCK_SUPPLEMENTAL_MATHEMATICAL_OPERATORS,
    BLOCK_MISCELLANEOUS_SYMBOLS_AND_ARROWS,
    BLOCK_GLAGOLITIC,
    BLOCK_LATIN_EXTENDED_C,
    BLOCK_COPTIC,
    BLOCK_GEORGIAN_SUPPLEMENT,
    BLOCK_TIFINAGH,
    BLOCK_ETHIOPIC_EXTENDED,
    BLOCK_CYRILLIC_EXTENDED_A,
    BLOCK_SUPPLEMENTAL_PUNCTUATION,
    BLOCK_CJK_RADICALS_SUPPLEMENT,
    BLOCK_KANGXI_RADICALS,
    BLOCK_IDEOGRAPHIC_DESCRIPTION_CHARACTERS,
    BLOCK_CJK_SYMBOLS_AND_PUNCTUATION,
    BLOCK_HIRAGANA,
    BLOCK_KATAKANA,
    BLOCK_BOPOMOFO,
    BLOCK_HANGUL_COMPATIBILITY_JAMO,
    BLOCK_KANBUN,
    BLOCK_BOPOMOFO_EXTENDED,
    BLOCK_CJK_STROKES,
    BLOCK_KATAKANA_PHONETIC_EXTENSIONS,
    BLOCK_ENCLOSED_CJK_LETTERS_AND_MONTHS,
    BLOCK_CJK_COMPATIBILITY,
    BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A,
    BLOCK_YIJING_HEXAGRAM_SYMBOLS,
    BLOCK_CJK_UNIFIED_IDEOGRAPHS,
    BLOCK_YI_SYLLABLES,
    BLOCK_YI_RADICALS,
    BLOCK_LISU,
    BLOCK_VAI,
    BLOCK_CYRILLIC_EXTENDED_B,
    BLOCK_BAMUM,
    BLOCK_MODIFIER_TONE_LETTERS,
    BLOCK_LATIN_EXTENDED_D,
    BLOCK_SYLOTI_NAGRI,
    BLOCK_COMMON_INDIC_NUMBER_FORMS,
    BLOCK_PHAGS_PA,
    BLOCK_SAURASHTRA,
    BLOCK_DEVANAGARI_EXTENDED,
    BLOCK_KAYAH_LI,
    BLOCK_REJANG,
    BLOCK_HANGUL_JAMO_EXTENDED_A,
    BLOCK_JAVANESE,
    BLOCK_MYANMAR_EXTENDED_B,
    BLOCK_CHAM,
    BLOCK_MYANMAR_EXTENDED_A,
    BLOCK_TAI_VIET,
    BLOCK_MEETEI_MAYEK_EXTENSIONS,
    BLOCK_ETHIOPIC_EXTENDED_A,
    BLOCK_LATIN_EXTENDED_E,
    BLOCK_CHEROKEE_SUPPLEMENT,
    BLOCK_MEETEI_MAYEK,
    BLOCK_HANGUL_SYLLABLES,
    BLOCK_HANGUL_JAMO_EXTENDED_B,
    BLOCK_HIGH_SURROGATES,
    BLOCK_HIGH_PRIVATE_USE_SURROGATES,
    BLOCK_LOW_SURROGATES,
    BLOCK_PRIVATE_USE_AREA,
    BLOCK_CJK_COMPATIBILITY_IDEOGRAPHS,
    BLOCK_ALPHABETIC_PRESENTATION_FORMS,
    BLOCK_ARABIC_PRESENTATION_FORMS_A,
    BLOCK_VARIATION_SELECTORS,
    BLOCK_VERTICAL_FORMS,
    BLOCK_COMBINING_HALF_MARKS,
    BLOCK_CJK_COMPATIBILITY_FORMS,
    BLOCK_SMALL_FORM_VARIANTS,
    BLOCK_ARABIC_PRESENTATION_FORMS_B,
    BLOCK_HALFWIDTH_AND_FULLWIDTH_FORMS,
    BLOCK_SPECIALS,
    BLOCK_LINEAR_B_SYLLABARY,
    BLOCK_LINEAR_B_IDEOGRAMS,
    BLOCK_AEGEAN_NUMBERS,
    BLOCK_ANCIENT_GREEK_NUMBERS,
    BLOCK_ANCIENT_SYMBOLS,
    BLOCK_PHAISTOS_DISC,
    BLOCK_LYCIAN,
    BLOCK_CARIAN,
    BLOCK_COPTIC_EPACT_NUMBERS,
    BLOCK_OLD_ITALIC,
    BLOCK_GOTHIC,
    BLOCK_OLD_PERMIC,
    BLOCK_UGARITIC,
    BLOCK_OLD_PERSIAN,
    BLOCK_DESERET,
    BLOCK_SHAVIAN,
    BLOCK_OSMANYA,
    BLOCK_OSAGE,
    BLOCK_ELBASAN,
    BLOCK_CAUCASIAN_ALBANIAN,
    BLOCK_VITHKUQI,
    BLOCK_TODHRI,
    BLOCK_LINEAR_A,
    BLOCK_LATIN_EXTENDED_F,
    BLOCK_CYPRIOT_SYLLABARY,
    BLOCK_IMPERIAL_ARAMAIC,
    BLOCK_PALMYRENE,
    BLOCK_NABATAEAN,
    BLOCK_HATRAN,
    BLOCK_PHOENICIAN,
    BLOCK_LYDIAN,
    BLOCK_SIDETIC,
    BLOCK_MEROITIC_HIEROGLYPHS,
    BLOCK_MEROITIC_CURSIVE,
    BLOCK_KHAROSHTHI,
    BLOCK_OLD_SOUTH_ARABIAN,
    BLOCK_OLD_NORTH_ARABIAN,
    BLOCK_MANICHAEAN,
    BLOCK_AVESTAN,
    BLOCK_INSCRIPTIONAL_PARTHIAN,
    BLOCK_INSCRIPTIONAL_PAHLAVI,
    BLOCK_PSALTER_PAHLAVI,
    BLOCK_OLD_TURKIC,
    BLOCK_OLD_HUNGARIAN,
    BLOCK_HANIFI_ROHINGYA,
    BLOCK_GARAY,
    BLOCK_RUMI_NUMERAL_SYMBOLS,
    BLOCK_YEZIDI,
    BLOCK_ARABIC_EXTENDED_C,
    BLOCK_OLD_SOGDIAN,
    BLOCK_SOGDIAN,
    BLOCK_OLD_UYGHUR,
    BLOCK_CHORASMIAN,
    BLOCK_ELYMAIC,
    BLOCK_BRAHMI,
    BLOCK_KAITHI,
    BLOCK_SORA_SOMPENG,
    BLOCK_CHAKMA,
    BLOCK_MAHAJANI,
    BLOCK_SHARADA,
    BLOCK_SINHALA_ARCHAIC_NUMBERS,
    BLOCK_KHOJKI,
    BLOCK_MULTANI,
    BLOCK_KHUDAWADI,
    BLOCK_GRANTHA,
    BLOCK_TULU_TIGALARI,
    BLOCK_NEWA,
    BLOCK_TIRHUTA,
    BLOCK_SIDDHAM,
    BLOCK_MODI,
    BLOCK_MONGOLIAN_SUPPLEMENT,
    BLOCK_TAKRI,
    BLOCK_MYANMAR_EXTENDED_C,
    BLOCK_AHOM,
    BLOCK_DOGRA,
    BLOCK_WARANG_CITI,
    BLOCK_DIVES_AKURU,
    BLOCK_NANDINAGARI,
    BLOCK_ZANABAZAR_SQUARE,
    BLOCK_SOYOMBO,
    BLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED_A,
    BLOCK_PAU_CIN_HAU,
    BLOCK_DEVANAGARI_EXTENDED_A,
    BLOCK_SHARADA_SUPPLEMENT,
    BLOCK_SUNUWAR,
    BLOCK_BHAIKSUKI,
    BLOCK_MARCHEN,
    BLOCK_MASARAM_GONDI,
    BLOCK_GUNJALA_GONDI,
    BLOCK_TOLONG_SIKI,
    BLOCK_BENGALI_SUPPLEMENT,
    BLOCK_MAKASAR,
    BLOCK_KAWI,
    BLOCK_LISU_SUPPLEMENT,
    BLOCK_TAMIL_SUPPLEMENT,
    BLOCK_CUNEIFORM,
    BLOCK_CUNEIFORM_NUMBERS_AND_PUNCTUATION,
    BLOCK_EARLY_DYNASTIC_CUNEIFORM,
    BLOCK_ARCHAIC_CUNEIFORM_NUMERALS,
    BLOCK_CYPRO_MINOAN,
    BLOCK_EGYPTIAN_HIEROGLYPHS,
    BLOCK_EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS,
    BLOCK_EGYPTIAN_HIEROGLYPHS_EXTENDED_A,
    BLOCK_ANATOLIAN_HIEROGLYPHS,
    BLOCK_GURUNG_KHEMA,
    BLOCK_BAMUM_SUPPLEMENT,
    BLOCK_MRO,
    BLOCK_TANGSA,
    BLOCK_BASSA_VAH,
    BLOCK_PAHAWH_HMONG,
    BLOCK_KIRAT_RAI,
    BLOCK_MEDEFAIDRIN,
    BLOCK_BERIA_ERFE,
    BLOCK_MIAO,
    BLOCK_IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION,
    BLOCK_TANGUT,
    BLOCK_TANGUT_COMPONENTS,
    BLOCK_KHITAN_SMALL_SCRIPT,
    BLOCK_TANGUT_SUPPLEMENT,
    BLOCK_TANGUT_COMPONENTS_SUPPLEMENT,
    BLOCK_JURCHEN,
    BLOCK_JURCHEN_RADICALS,
    BLOCK_KANA_EXTENDED_B,
    BLOCK_KANA_SUPPLEMENT,
    BLOCK_KANA_EXTENDED_A,
    BLOCK_SMALL_KANA_EXTENSION,
    BLOCK_NUSHU,
    BLOCK_DUPLOYAN,
    BLOCK_SHORTHAND_FORMAT_CONTROLS,
    BLOCK_SYMBOLS_FOR_LEGACY_COMPUTING_SUPPLEMENT,
    BLOCK_MISCELLANEOUS_SYMBOLS_SUPPLEMENT,
    BLOCK_ZNAMENNY_MUSICAL_NOTATION,
    BLOCK_BYZANTINE_MUSICAL_SYMBOLS,
    BLOCK_MUSICAL_SYMBOLS,
    BLOCK_ANCIENT_GREEK_MUSICAL_NOTATION,
    BLOCK_MUSICAL_SYMBOLS_SUPPLEMENT,
    BLOCK_KAKTOVIK_NUMERALS,
    BLOCK_MAYAN_NUMERALS,
    BLOCK_TAI_XUAN_JING_SYMBOLS,
    BLOCK_COUNTING_ROD_NUMERALS,
    BLOCK_MATHEMATICAL_ALPHANUMERIC_SYMBOLS,
    BLOCK_SUTTON_SIGNWRITING,
    BLOCK_MISCELLANEOUS_SYMBOLS_AND_ARROWS_EXTENDED,
    BLOCK_LATIN_EXTENDED_G,
    BLOCK_GLAGOLITIC_SUPPLEMENT,
    BLOCK_CYRILLIC_EXTENDED_D,
    BLOCK_NYIAKENG_PUACHUE_HMONG,
    BLOCK_TOTO,
    BLOCK_WANCHO,
    BLOCK_NAG_MUNDARI,
    BLOCK_OL_ONAL,
    BLOCK_TAI_YO,
    BLOCK_ETHIOPIC_EXTENDED_B,
    BLOCK_MENDE_KIKAKUI,
    BLOCK_ADLAM,
    BLOCK_INDIC_SIYAQ_NUMBERS,
    BLOCK_OTTOMAN_SIYAQ_NUMBERS,
    BLOCK_ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS,
    BLOCK_MAHJONG_TILES,
    BLOCK_DOMINO_TILES,
    BLOCK_PLAYING_CARDS,
    BLOCK_ENCLOSED_ALPHANUMERIC_SUPPLEMENT,
    BLOCK_ENCLOSED_IDEOGRAPHIC_SUPPLEMENT,
    BLOCK_MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS,
    BLOCK_EMOTICONS,
    BLOCK_ORNAMENTAL_DINGBATS,
    BLOCK_TRANSPORT_AND_MAP_SYMBOLS,
    BLOCK_ALCHEMICAL_SYMBOLS,
    BLOCK_GEOMETRIC_SHAPES_EXTENDED,
    BLOCK_SUPPLEMENTAL_ARROWS_C,
    BLOCK_SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS,
    BLOCK_CHESS_SYMBOLS,
    BLOCK_SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A,
    BLOCK_SYMBOLS_FOR_LEGACY_COMPUTING,
    BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B,
    BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C,
    BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D,
    BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E,
    BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F,
    BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_I,
    BLOCK_CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT,
    BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G,
    BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_H,
    BLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_J,
    BLOCK_SEAL,
    BLOCK_TAGS,
    BLOCK_VARIATION_SELECTORS_SUPPLEMENT,
    BLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_A,
    BLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_B,
)
