import httpx


def get_chats(access_token):
    url = 'http://127.0.0.1:8000/chat/chats'
    headers = {'Authorization': f'Bearer {access_token}'}
    with httpx.Client() as client:
        response = client.post(url, headers=headers)
        data = response.json()
        chats = data['data']
        return chats


if __name__ == '__main__':
    access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNzI5NjM4NTk3LjAzMzk5MX0.OMIzvBpbb5KExFH4hn8K8UQv8f302dXQESMJC2_vPSA'
    print(get_chats(access_token))
