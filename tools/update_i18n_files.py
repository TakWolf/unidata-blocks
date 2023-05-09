import os
import re

import unidata_blocks
from tools import i18n_dir


def load_localized_names(i18n_file_path: str | bytes | os.PathLike[str] | os.PathLike[bytes]):
    localized_names = {}
    with open(i18n_file_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.split('#', 1)[0].strip()
            if line == '':
                continue
            tokens = re.split(r':\s', line)
            if len(tokens) >= 2:
                localized_names[tokens[0]] = tokens[1]
    return localized_names


def main():
    for i18n_file_name in os.listdir(i18n_dir):
        if not i18n_file_name.endswith('.txt'):
            continue
        i18n_file_path = os.path.join(i18n_dir, i18n_file_name)
        localized_names = load_localized_names(i18n_file_path)

        with open(i18n_file_path, 'w', encoding='utf-8') as file:
            file.write(f'# {i18n_file_name}\n\n')
            for block in unidata_blocks.get_blocks():
                if block.name in localized_names:
                    file.write(f'{block.name}: {localized_names[block.name]}\n')
                else:
                    file.write(f'{block.name}:\n')
                    print(f'{i18n_file_name} {block}')


if __name__ == '__main__':
    main()
