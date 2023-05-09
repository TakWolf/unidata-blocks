import os.path

import requests

from tools import blocks_doc_url, unidata_dir, blocks_file_path


def main():
    response = requests.get(blocks_doc_url)
    assert response.ok
    assert 'text/plain' in response.headers['Content-Type']

    if not os.path.exists(unidata_dir):
        os.makedirs(unidata_dir)

    with open(blocks_file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)


if __name__ == '__main__':
    main()
