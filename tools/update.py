import shutil

import httpx
import langcodes

import unidata_blocks
from tools import project_root_dir


def main():
    unidata_dir = project_root_dir.joinpath('src', 'unidata_blocks', 'unidata')
    translations_dir = unidata_dir.joinpath('translations')
    translations_tmp_dir = project_root_dir.joinpath('build', 'translations')

    response = httpx.get('https://www.unicode.org/Public/UNIDATA/Blocks.txt')
    assert response.is_success and 'text/plain' in response.headers['Content-Type']
    unidata_dir.joinpath('Blocks.txt').write_text(response.text, 'utf-8')
    # noinspection PyProtectedMember
    unicode_version, blocks = unidata_blocks._parse_blocks(response.text)

    if translations_tmp_dir.exists():
        shutil.rmtree(translations_tmp_dir)
    translations_tmp_dir.mkdir(parents=True)

    for file_path in translations_dir.iterdir():
        if file_path.suffix != '.txt':
            continue
        language = langcodes.standardize_tag(file_path.stem)
        # noinspection PyProtectedMember
        translation = unidata_blocks._parse_translation(file_path.read_text('utf-8'))

        with translations_tmp_dir.joinpath(f'{language}.txt').open('w', encoding='utf-8') as file:
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


if __name__ == '__main__':
    main()
