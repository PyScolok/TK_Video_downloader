import re
import pathlib

import requests
from PIL import Image


class PreviewDownloader:
    def __init__(self, url):
        self.id = self._get_video_id(url)

    def download_image(self):
        file = requests.get(f'https://img.youtube.com/vi/{self.id}/hqdefault.jpg')
        self._save_image(file.content)

    def _get_video_id(self, url):
        video_id = re.search(r'v=([^=]+)', url)
        return video_id.group(1)
    
    def _save_image(self, file):
        img = open('preview.jpg', 'wb')
        img.write(file)
        img.close()
        self._convert_image()

    def _convert_image(self):
        image = Image.open('preview.jpg')
        if not pathlib.Path('./img').exists():
            pathlib.Path('./img').mkdir()
        image.save('./img/preview.png')
        self._delete_temp_file()
        
    def _delete_temp_file(self):
        pathlib.Path('./preview.jpg').unlink()
