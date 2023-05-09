import os

import unidata_blocks
from tools import i18n_dir


def main(locale: str):
    if not os.path.exists(i18n_dir):
        os.makedirs(i18n_dir)

    i18n_file_path = os.path.join(i18n_dir, f'{locale}.txt')
    with open(i18n_file_path, 'w', encoding='utf-8') as file:
        file.write(f'# {locale}.txt\n\n')
        for block in unidata_blocks.get_blocks():
            file.write(f'{block.name}:\n')


if __name__ == '__main__':
    main('en')
