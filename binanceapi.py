from binance import Client
api_key = "X7j79Eebp8LikMco3b9NoOTvFM3bWki9mklMmh5TVesAN2KuQJvbwyW0O6m6niqP"
api_secret = "xUbW21HlVhPlgZvknc9S8zc7m9Nv0FnNhALxZN479qkuKb0dAudD47n47RWVMBBg" #binance 
from binance.spot import Spot as Client

client = Client(api_key, api_secret)
response = client.get_order('BTCUSDT', orderId=11, recvWindow=10000)