import shutil
from io import StringIO
from pathlib import Path

import langcodes
import requests

import unidata_blocks

blocks_doc_url = 'https://www.unicode.org/Public/UNIDATA/Blocks.txt'

project_root_dir = Path(__file__).parent.joinpath('..').resolve()
unidata_dir = project_root_dir.joinpath('src', 'unidata_blocks', 'unidata')
translations_dir = unidata_dir.joinpath('translations')
translations_tmp_dir = project_root_dir.joinpath('build', 'translations')


def main():
    response = requests.get(blocks_doc_url)
    assert response.ok and 'text/plain' in response.headers['Content-Type']
    unidata_dir.joinpath('Blocks.txt').write_text(response.text, 'utf-8')
    # noinspection PyProtectedMember
    unicode_version, blocks = unidata_blocks._parse_blocks(response.text)

    if translations_tmp_dir.exists():
        shutil.rmtree(translations_tmp_dir)
    translations_tmp_dir.mkdir(parents=True)

    for file_path in translations_dir.iterdir():
        if file_path.suffix != '.txt':
            continue
        language = langcodes.standardize_tag(file_path.name.removesuffix('.txt'))
        # noinspection PyProtectedMember
        translation = unidata_blocks._parse_translation(file_path.read_text('utf-8'))

        output = StringIO()
        output.write(f'# Unicode: {unicode_version}\n')
        output.write(f'# {language}\n\n')
        for block in blocks:
            localized_name = translation.get(block.name, None)
            if localized_name is None:
                output.write(f'# TODO # {block.name}:\n')
            else:
                output.write(f'{block.name}: {localized_name}\n')
        translations_tmp_dir.joinpath(f'{language}.txt').write_text(output.getvalue(), 'utf-8')

    shutil.rmtree(translations_dir)
    translations_tmp_dir.rename(translations_dir)


if __name__ == '__main__':
    main()
