import requests

from bs4 import BeautifulSoup






# video_url = "https://www.jiocinema.com/51ad5f3d-4354-4e9a-a074-cdb6bff39bd3"# Replace with the actual video URL
url = 'https://www.jiocinema.com/tv-shows/ranjish-hi-sahi/1/shankar-and-his-dreams/3520870'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


response = requests.get(url,headers=headers)
soup =  BeautifulSoup(response.text,'html.parser')
print(soup.find('video'))

# print(response)
# if response.status_code == 200:
#     with open("video.mp4", "wb") as f:
#         f.write(response.content)
#     print("Video downloaded successfully!")
# else:
#     print("Failed to download the video.")
