import requests
# from pprint import pprint

class VkPhoto:
    host = 'https://api.vk.com/method/users.get'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }


    def PhotosGetAllTest(self, user_id):
        domain = 'https://api.vk.com/method'
        params = {
        'access_token': self.token,
        'user_id': user_id,
        'extended': 1,
        'v': '5.131'
        }
        # query = f"{domain}/photos.getAll?access_token={access_token}&user_id={user_id}&extended=1&v={v}"
        query = f"{domain}/photos.getAll"
        response = requests.get(query, params=params)
        resp_resp = response.json()['response']['items']
        # pprint(resp_resp)

        downloadFiles = []
        for photo_element in resp_resp:
            photoURL = photo_element['sizes'][-1]['url']
            photoLikes = photo_element['likes']['count']
            photoDate = photo_element['date']
            # print(photo_element['sizes'][-1]['url'])
            downloadFiles.append({'url': photoURL, 'likes': photoLikes, 'date': photoDate})
            photoURL = 0
            photoLikes = 0
            photoDate = 0
        return downloadFiles


# photo_sizes


    def PhotosGetAllParams(self, user_id):
        domain = 'https://api.vk.com/method'
        params = {
            'access_token': self.token,
            'user_id': user_id,
            'extended': 1,
            'photo_sizes': 0,
            'v': '5.131'
        }
        # query = f"{domain}/photos.getAll?access_token={access_token}&user_id={user_id}&extended=1&v={v}"
        query = f"{domain}/photos.getAll"
        response = requests.get(query, params=params)
        resp_resp = response.json()['response']['items']
        # pprint(resp_resp)

        downloadFiles = []
        for photo_element in resp_resp:
            photoURL = photo_element['sizes'][-1]['url']
            photoType = photo_element['sizes'][-1]['type']
            photoLikes = photo_element['likes']['count']
            photoDate = photo_element['date']
            # print(photo_element['sizes'][-1]['url'])
            downloadFiles.append({'url': photoURL, 'likes': photoLikes, 'date': photoDate, 'size': photoType})
            photoURL = 0
            photoType = 0
            photoLikes = 0
            photoDate = 0
        # pprint(downloadFiles)
        return downloadFiles





