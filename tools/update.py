import os
import shutil

import langcodes
import requests

import unidata_blocks

blocks_doc_url = 'https://www.unicode.org/Public/UNIDATA/Blocks.txt'

project_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
unidata_dir = os.path.join(project_root_dir, 'src', 'unidata_blocks', 'unidata')
blocks_file_name = 'Blocks.txt'
blocks_file_path = os.path.join(unidata_dir, blocks_file_name)
translations_dir = os.path.join(unidata_dir, 'translations')
translations_tmp_dir = os.path.join(project_root_dir, 'build', 'translations')
languages_file_path = os.path.join(unidata_dir, 'languages.txt')


def main():
    response = requests.get(blocks_doc_url)
    assert response.ok
    assert 'text/plain' in response.headers['Content-Type']
    with open(blocks_file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)
    unicode_version, blocks = unidata_blocks._parse_blocks(response.text)

    if os.path.exists(translations_tmp_dir):
        shutil.rmtree(translations_tmp_dir)
    os.makedirs(translations_tmp_dir)

    languages = ['en']

    for translation_file_name in os.listdir(translations_dir):
        if not translation_file_name.endswith('.txt'):
            continue
        language = langcodes.standardize_tag(translation_file_name.removesuffix('.txt'))
        languages.append(language)

        translation_file_path = os.path.join(translations_dir, translation_file_name)
        with open(translation_file_path, 'r', encoding='utf-8') as file:
            translation = unidata_blocks._parse_translation(file.read())

        translation_tmp_file_path = os.path.join(translations_tmp_dir, translation_file_name)
        with open(translation_tmp_file_path, 'w', encoding='utf-8') as file:
            file.write(f'# Unicode: {unicode_version}\n')
            file.write(f'# {language}\n\n')
            for block in blocks:
                localized_name = translation.get(block.name, None)
                if localized_name is None:
                    file.write(f'# TODO # {block.name}:\n')
                else:
                    file.write(f'{block.name}: {localized_name}\n')
    shutil.rmtree(translations_dir)
    os.rename(translations_tmp_dir, translations_dir)

    languages.sort()
    with open(languages_file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(languages))
        file.write('\n')


if __name__ == '__main__':
    main()
