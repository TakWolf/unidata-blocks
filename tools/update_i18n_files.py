import os
import shutil

import unidata_blocks
from tools import i18n_dir, i18n_tmp_dir


def main():
    if os.path.exists(i18n_tmp_dir):
        shutil.rmtree(i18n_tmp_dir)
    os.makedirs(i18n_tmp_dir)

    for i18n_file_name in os.listdir(i18n_dir):
        if not i18n_file_name.endswith('.txt'):
            continue
        locale = i18n_file_name.removesuffix('.txt')
        i18n_tmp_file_path = os.path.join(i18n_tmp_dir, i18n_file_name)

        with open(i18n_tmp_file_path, 'w', encoding='utf-8') as file:
            file.write(f'# Unicode: {unidata_blocks.unicode_version}\n')
            file.write(f'# {i18n_file_name}\n\n')
            for block in unidata_blocks.get_blocks():
                localized_name = block.name_localized(locale)
                if localized_name is None:
                    file.write(f'{block.name}:\n')
                    print(f'{i18n_file_name} {block}')
                else:
                    file.write(f'{block.name}: {localized_name}\n')

    shutil.rmtree(i18n_dir)
    os.rename(i18n_tmp_dir, i18n_dir)


if __name__ == '__main__':
    main()
