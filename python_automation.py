import requests
import schedule

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : '+447123456789',
        'message' : 'Hey, Good morning',
        'key' : 'textbelt'
    })

    print(resp.json())

schedule.every().day.at('23:20').do(send_message)