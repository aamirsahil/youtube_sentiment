from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager
import time

# def getComments(youtube_url : str) -> list:
#     respose = requests.get(youtube_url)
    
#     if respose.status_code == 200:
#         soup = BeautifulSoup(respose.text, 'html.parser')
#         comment_section = soup.find('ytd-comments')
#         comments = []

#         if comment_section:
#             comment_elements = comment_section.find_all('ytd-comment-renderer')

#             for comment_element in comment_elements:
#                 comment_text = comment_element.find('yt-formatted-string').text.strip()
#                 comments.append(comment_text)
#     return comments

def main():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    youtube_url = "https://www.youtube.com/watch?v=vRzqohAgfoE&t=1260s"
    wait = WebDriverWait(driver, 10)
    driver.get(youtube_url)
    # get_url = driver.current_url
    # wait.until(EC.url_to_be(youtube_url))
    # if get_url == youtube_url:
    #     page_source = driver.page_source

    driver.maximize_window()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, 1000);")
    for i in range(0,6):
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 10000);")

    comments_section = driver.find_element_by_xpath('//*[@id="comments"]')

    # extract the HTML content of the comments section
    comments_html = comments_section.get_attribute('innerHTML')

    soup = BeautifulSoup(comments_html,features='html.parser')
    # keyword=input('Enter a keyword to find instances of in the article:')
    # matches = soup.body.find_all(string=re.compile(keyword))
    # len_match = len(matches)
    # title = soup.title.text
    # print(f"keyword : {keyword} occurs {len_match} times in {title} page")

    # extract the text of the comments
    comments = [comment.text for comment in soup.find_all('yt-formatted-string', {'class': 'style-scope ytd-comment-renderer'})]

    # print the comments
    print(comments)
    driver.close()

    # comments = getComments(youtube_url)

    # for idx, comment in enumerate(comments, start=1):
    #     print(f'{idx} : {comment}')

if __name__=='__main__':
    main()