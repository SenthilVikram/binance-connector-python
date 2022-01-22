from wazirx_sapi_client.rest import Client
import time
from playsound import playsound

# public
client = Client()
# print(client.send("ping"))
# print(client.send("time"))
# print(client.send("system_status"))
# print(client.send("exchange_info"))

# private
api_key = "I8Iu3yoBJV5qGkIxDwBYhsQ9PFrE6ONV7YsONeTevf0vh9UbBkrBiZuS8CEoOcBi"
secret_key = "xZQKqCpOnV4kxfsQAnTQk1U83caYXKHMJ4beAqle"

client = Client(api_key=api_key, secret_key=secret_key)
upper_limit = 16.9
lower_limit = 15
while(1):
    hist_data = client.send("historical_trades",
             {"limit": 1, "symbol": "dogeinr", "recvWindow": 10000, "timestamp": int(time.time() * 1000)}
             )
    for i in hist_data[1][:]:
        print(hist_data[1][:])
        if ((float(i['price']) > upper_limit) or (float(i['price']) < lower_limit)):
            print(i['price'])
            for i in range(1):
                playsound('wazirx_auto/wazirx-connector-python/audios/stoplimit.mp3')
                time.sleep(0)
        else:
            #print(i['price'])
            pass
    time.sleep(1)       

# print(client.send('create_order',
#              {"symbol": "btcinr", "side": "buy", "type": "limit", "price": 500, "quantity": 1, "recvWindow": 10000,
#               "timestamp": int(time.time() * 1000)}))





