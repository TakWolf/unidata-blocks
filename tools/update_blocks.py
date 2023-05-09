import os.path

import requests

import unidata_blocks


def main():
    response = requests.get(unidata_blocks.blocks_doc_url)
    assert response.ok
    assert 'text/plain' in response.headers['Content-Type']

    if not os.path.exists(unidata_blocks.unidata_dir):
        os.makedirs(unidata_blocks.unidata_dir)

    with open(unidata_blocks.blocks_file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)


if __name__ == '__main__':
    main()
