import re
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
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
    
    def _getComments(self, youtube, video_id, part="snippet", max_results=100):
        """
        # Get comments from the url
        Arg\n
            video_id (str) : youtube video id
            part (str)
            max_results (int)
        Return\n
            comments (list) : list of comments
        """
        # get comments
        try:
            # Retrieve comment thread using the youtube.commentThreads().list() method
            response = youtube.commentThreads().list(
                part=part,
                videoId=video_id,
                textFormat="plainText",
                maxResults=max_results
            ).execute()

            comments = []
            for item in response["items"]:
                comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                likes = item["snippet"]["topLevelComment"]["snippet"]["likeCount"]
                comments.append({"comment": comment_text, "num_of_likes": likes})

            return comments
        
        except HttpError as error:
            print(f"An HTTP error {error.http_status} occurred:\n {error.content}")
            return None

    def _saveComments(self, comments, save_loc):
        if comments:
            # Create a pandas dataframe from the comments list
            df = pd.DataFrame(comments)

            # Sort dataframe by number of likes in descending order
            df = df.sort_values(by=['num_of_likes'], ascending=False)

            # Print a preview of the first 10 rows
            print(df.head(10))

            # Export dataframe to a CSV file named "comments.csv"
            df.to_csv(save_loc, index=False)
        else:
            print("Error: Could not retrieve comments from video.")

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
        youtube = build("youtube", "v3", developerKey=self.api_key)
        comments = self._getComments(youtube, video_id)

        # convert comments to dataframe
        df_comments = pd.DataFrame(comments)
        
        # save comments
        self._saveComment(comments, save_loc)

        return df_comments