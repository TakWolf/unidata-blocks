import httpx

from tools import ASSETS_DIR


def main() -> None:
    response = httpx.get('https://www.unicode.org/Public/UNIDATA/Blocks.txt')
    assert response.is_success and 'text/plain' in response.headers['Content-Type']
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.joinpath('Blocks.txt').write_text(response.text, 'utf-8')


if __name__ == '__main__':
    main()
