import os

blocks_doc_url = 'https://www.unicode.org/Public/UNIDATA/Blocks.txt'

unidata_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'unidata'))
blocks_file_name = 'Blocks.txt'
blocks_file_path = os.path.join(unidata_dir, blocks_file_name)

