from youtubescraper import YoutubeScraper

def main():
    url = input("Enter the youtube url")
    
    # scrape youtube comments
    youtube_scraper = YoutubeScraper()
    df_comments = youtube_scraper.scrapeYoutube(url=url)
    
    # perform sentiment analysis
    

if __name__=="__main__":
    main()