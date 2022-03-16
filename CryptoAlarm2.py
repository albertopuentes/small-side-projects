
import cbpro
import pandas as pd

from api import Coinbase_API2
from api import Coinbase_secret
from coinbase.wallet.client import Client


coinbase_API_key = 'Coinbase_API2'
coinbase_API_secret = 'Coinbase_secret'
client = Client(coinbase_API_key, coinbase_API_secret)

total = 0
message = []

accounts = client.get_accounts()
for wallet in accounts.data:
    message.append( str(wallet['name']) + ' ' +   str(wallet['native_balance']) )
    value = str( wallet['native_balance']).replace('USD','')
    total += float(value)
message.append( 'Total Balance: ' + 'USD ' + str(total) )
print ('\n'.join( message ))
