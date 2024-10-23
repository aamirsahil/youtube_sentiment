import re

class YoutubeScraper:
    def __init__(self, url):
        self.video_id = self._getVideoId(url)

    def _getVideoId(self, url):
        regex = "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(?:-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|live\/|v\/)?)([\w\-]+)(\S+)?$"

        match = re.search(regex, url)

        if match:
            return match.group(5)  # Returns the video ID
        else:
            return None