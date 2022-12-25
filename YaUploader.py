import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file):

        upload_link = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources/upload',
                                   headers={'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'},
                                   params={'path': path_to_file}
                                   )
        response = requests.put(upload_link.json()['href'],
                                headers={'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'},
                                data=open(path_to_file, 'rb')
                                )

        print(response.status_code)
        if response.status_code == 200 or 201:
            print('Загрузка файла успешно завершена!')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)