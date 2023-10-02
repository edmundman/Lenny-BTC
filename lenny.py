import requests
import time

previous_price = None

emoji_moods = {
    'happy': '( ͡° ͜ʖ ͡°)',
    'sad': '( ͡° ʖ̯ ͡°)',
    'neutral': '( ͡~ ͜ʖ ͡°)',
}

while True:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    data = response.json()
    current_price = data['bpi']['USD']['rate_float']

    if previous_price:
        if current_price > previous_price:
            print(emoji_moods['happy'])
        elif current_price < previous_price:
            print(emoji_moods['sad'])
        else:
            print(emoji_moods['neutral'])
    else:
        print("Fetching new price...")

    previous_price = current_price
    time.sleep(30)
