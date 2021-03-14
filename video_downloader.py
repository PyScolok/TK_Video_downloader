import pytube

from preview_downloader import PreviewDownloader


class VideoDownloader:

    def __init__(self, url):
        self._preview_loader = PreviewDownloader(url)
        self._video = pytube.YouTube(url)

    def _get_streams(self):
        return self._video.streams.filter(progressive=True)

    def get_title(self):
        return self._video.title
    
    def get_preview_image(self):
        self._preview_loader.download_image()

    def get_all_res(self):
        return [stream.resolution for stream in self._get_streams()]

    def download(self, resolution, path):
        video = self._get_streams().filter(res=resolution).first()
        video.download('./video')
    


    