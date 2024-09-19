import requests

API_KEY = input('Input your API key here: ')#'YOUR_API_KEY'  # Replace with your API key
SPACE_ID = input('Enter chat id which can be found on the online google chat: ')#'YOUR_SPACE_ID'  # Replace with your space ID
BASE_URL = 'https://chat.googleapis.com/v1/spaces'

def get_messages_count(space_id):
    url = f'{BASE_URL}/{space_id}/messages?key={API_KEY}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        messages = response.json().get('messages', [])
        return len(messages)
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

if __name__ == '__main__':
    count = get_messages_count(SPACE_ID)
    if count is not None:
        print(f'Total messages in space: {count}')
