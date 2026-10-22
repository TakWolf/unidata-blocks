import httpx

from tools import PROJECT_ROOT_DIR


def main() -> None:
    response = httpx.get('https://www.unicode.org/Public/UNIDATA/Blocks.txt')
    assert response.is_success and 'text/plain' in response.headers['Content-Type']
    unidata_dir = PROJECT_ROOT_DIR.joinpath('src', 'unidata_blocks', 'unidata')
    unidata_dir.joinpath('Blocks.txt').write_text(response.text, 'utf-8')


if __name__ == '__main__':
    main()
