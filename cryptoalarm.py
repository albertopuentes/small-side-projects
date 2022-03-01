# from api import Coinbase_API

# import cbpro
# import pandas as pd
# c = cbpro.PublicClient()

# data = pd.DataFrame(c.get_products())
# 
# data.tail().T


class PublicClient(object):
    """cbpro public client API.
    All requests default to the `product_id` specified at object
    creation if not otherwise specified.
    Attributes:
        url (Optional[str]): API URL. Defaults to cbpro API.
    """

    def __init__(self, api_url='https://api.pro.coinbase.com', timeout=30):
        """Create cbpro API public client.
        Args:
            api_url (Optional[str]): API URL. Defaults to cbpro API.
        """
        self.url = api_url.rstrip('/')
        self.auth = None
        self.session = requests.Session()

    def get_products(self):
        """Get a list of available currency pairs for trading.
        Returns:
            list: Info about all currency pairs. Example::
                [
                    {
                        "id": "BTC-USD",
                        "display_name": "BTC/USD",
                        "base_currency": "BTC",
                        "quote_currency": "USD",
                        "base_min_size": "0.01",
                        "base_max_size": "10000.00",
                        "quote_increment": "0.01"
                    }
                ]
        """
        return self._send_message('get', '/products')
