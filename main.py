import time

# from pprint import pprint
import json
import os
from vkphoto import VkPhoto
from yadisk import YaDisk
import datetime
from alive_progress import alive_bar

token_yd = os.getenv("TOKEN_YD")
#print(token_yd)

token_vk = os.getenv("TOKEN_VK")
# print(token_vk)

yadisk = YaDisk(token_yd)
vkphoto = VkPhoto(token_vk)

def JsonWrite(forJsonDict):
    with open('save.json', 'w') as fileJson:
        json.dump(forJsonDict, fileJson)


def PhotoDoUpLoader(path, count=5):
    """ Загрузка фотографий из vk в папку на Яндекс диске."""
    downloadFiles = vkphoto.PhotosGetAllParams(552934290)

    downloadFilesSort = sorted(downloadFiles, key=lambda x: x['likes'], reverse=True)
    # pprint(downloadFilesSort)
    basenamePrev = 0
    downloadFilesJson = []
    with alive_bar(count, force_tty=True) as bar:
        for i in range(0, count):
            basename = downloadFilesSort[i]['likes']
            url = downloadFilesSort[i]['url']
            size = downloadFilesSort[i]['size']

            # print(basename)
            if basename == basenamePrev:
                dateForName = downloadFilesSort[i]['date']
                readableTime = datetime.datetime.fromtimestamp(dateForName).strftime('%d%m%Y')
                fileName = f"{path}/{basename}_{readableTime}.jpg"
                # print(fileName)
                yadisk.upload_link(fileName, url)
                downloadFilesJson.append({'file_name': fileName, 'size': size})
            else:
                fileName = f"{path}/{basename}.jpg"
                # print(fileName)
                basenamePrev = basename
                yadisk.upload_link(fileName, url)
                downloadFilesJson.append({'file_name': fileName, 'size': size})
            i += i
            time.sleep(3)
            bar()

    def PhotoDoUpLoaderTest(path, count=5):
        """ Загрузка фотографий из vk в папку на Яндекс диске."""
        downloadFiles = vkphoto.PhotosGetAllParams(552934290)

        downloadFilesSort = sorted(downloadFiles, key=lambda x: x['likes'], reverse=True)
        # pprint(downloadFilesSort)
        basenamePrev = 0
        downloadFilesJson = []
        for i in range(0, count):
            basename = downloadFilesSort[i]['likes']
            url = downloadFilesSort[i]['url']
            size = downloadFilesSort[i]['size']

            # print(basename)
            if basename == basenamePrev:
                dateForName = downloadFilesSort[i]['date']
                readableTime = datetime.datetime.fromtimestamp(dateForName).strftime('%d%m%Y')
                fileName = f"{path}/{basename}_{readableTime}.jpg"
                # print(fileName)
                yadisk.upload_link(fileName, url)
                downloadFilesJson.append({'file_name': fileName, 'size': size})
            else:
                fileName = f"{path}/{basename}.jpg"
                # print(fileName)
                basenamePrev = basename
                yadisk.upload_link(fileName, url)
                downloadFilesJson.append({'file_name': fileName, 'size': size})
            i += i
            time.sleep(3)

    JsonWrite(downloadFilesJson)


def PhotoLoad(path, count=5):
    yadisk.create_folder(path)
    PhotoDoUpLoader(path,count)




# mylist = [1,2,3,4,5,6,7,8]
#
# for i in tqdm(mylist):
#     time.sleep(1)

if __name__ == '__main__':
    PhotoLoad('/folder_for_photo1',5)


    # PhotoDoUpLoader()
    # vkphoto.PhotosGetAllParams(552934290)

    # yadisk.upload_link('/123.jpg', 'https://sun9-28.userapi.com/s/v1/if1/Ewp6frruZjG76BgnZ74s9Zu0stqInLHNRbTrp0REiXLRZEq8qcZtSwXNjciM8WEEgPCUgiwM.jpg?size=400x400&quality=96&type=album')

