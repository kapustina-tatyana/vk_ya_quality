from pprint import pprint
#from typing import Dict

import requests


class YaDisk:
    host = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    def get_files_list(self):
        url = f'{self.host}/v1/disk/resources/files'
        # ?fields=items.size'
        headers = self.get_headers()
        params = {'fields': 'items.name, items.created, items.size'}
        # params = {}
        response = requests.get(url, headers=headers, params=params)
        # print(response.url)
        pprint(response.json())

    def _get_upload_link(self,path):
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        # print(response.status_code)
        # print(response.json())
        resp_status = response.json().get('href')
        # resp_status = response.json()
        # print(resp_status)
        return resp_status


    def upload_file(self, path, file_name):
        upload_link = self._get_upload_link(path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

    def upload_link(self, path, download_link):
        url = f'{self.host}/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path, 'url': download_link}

        response = requests.post(url, headers=headers, params=params)
        response.raise_for_status()

        if response.status_code == 201:
            print('Success')
        # print(response.status_code)

    def create_folder(self, path):
        """Создание папки. \n path: Путь к создаваемой папке."""
        url = f'{self.host}/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path}
        requests.put(url, params=params, headers=headers)