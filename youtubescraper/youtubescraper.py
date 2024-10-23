import re
from dotenv import load_dotenv
import os

class YoutubeScraper:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("YOUTUBE_SCRAPE_KEY")

    def _getVideoId(self, url):
        regex = "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(?:-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|live\/|v\/)?)([\w\-]+)(\S+)?$"

        match = re.search(regex, url)

        if match:
            return match.group(5)  # Returns the video ID
        else:
            return None
    
    def _getComments(self):
        pass

    def _saveComments(self):
        pass

    def scrapeYoutube(self, url):
        """
        Go to youtube url, scrape the comments and save it in save_loc\n
        Args\n
            api_key : youtube scrapper api key
            url : youtube url
            save_loc : location to save the comments   
        """
        # request youtube url
        save_loc = f"../data/comments_{video_id}.csv"

        video_id = self._getVideoId(url)
        comments = self._getComments(video_id, self.api_key, save_loc)
        
        # save comments
        self._saveComment(comments, save_loc)