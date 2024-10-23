from youtubescraper import YoutubeScraper

def main():
    url = input("Enter the youtube url")
    youtube_scraper = YoutubeScraper(url)
    print(youtube_scraper.video_id)

if __name__=="__main__":
    main()