"""
Pyaddy

Maurice Saldivar

"""

from addy import Addy



def main() -> None:
    """"""
    addy_client = Addy()


    resp = addy_client.get_api_token_details()
    print(f'api details {resp}')


if __name__ == "__main__":
    main()