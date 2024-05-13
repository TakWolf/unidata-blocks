import shutil
from pathlib import Path

import langcodes
import requests

import unidata_blocks

blocks_doc_url = 'https://www.unicode.org/Public/UNIDATA/Blocks.txt'

project_root_dir = Path(__file__).parent.joinpath('..').resolve()
unidata_dir = project_root_dir.joinpath('src', 'unidata_blocks', 'unidata')
blocks_file_path = unidata_dir.joinpath('Blocks.txt')
translations_dir = unidata_dir.joinpath('translations')
translations_tmp_dir = project_root_dir.joinpath('build', 'translations')
languages_file_path = unidata_dir.joinpath('languages.txt')


def main():
    response = requests.get(blocks_doc_url)
    assert response.ok
    assert 'text/plain' in response.headers['Content-Type']
    with open(blocks_file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)
    # noinspection PyProtectedMember
    unicode_version, blocks = unidata_blocks._parse_blocks(response.text)

    if translations_tmp_dir.exists():
        shutil.rmtree(translations_tmp_dir)
    translations_tmp_dir.mkdir(parents=True)

    languages = ['en']

    for file_path in translations_dir.iterdir():
        if file_path.suffix != '.txt':
            continue
        file_name = file_path.name
        language = langcodes.standardize_tag(file_name.removesuffix('.txt'))
        languages.append(language)

        with open(file_path, 'r', encoding='utf-8') as file:
            # noinspection PyProtectedMember
            translation = unidata_blocks._parse_translation(file.read())

        tmp_file_path = translations_tmp_dir.joinpath(file_name)
        with open(tmp_file_path, 'w', encoding='utf-8') as file:
            file.write(f'# Unicode: {unicode_version}\n')
            file.write(f'# {language}\n\n')
            for block in blocks:
                localized_name = translation.get(block.name, None)
                if localized_name is None:
                    file.write(f'# TODO # {block.name}:\n')
                else:
                    file.write(f'{block.name}: {localized_name}\n')
    shutil.rmtree(translations_dir)
    translations_tmp_dir.rename(translations_dir)

    languages.sort()
    with open(languages_file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(languages))
        file.write('\n')


if __name__ == '__main__':
    main()
