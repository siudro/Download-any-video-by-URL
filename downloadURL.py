import urllib.request 
url_link = input("Enter the video URL\n")
video_name = input("Name the video\n")
video_name = video_name+".mp4"
urllib.request.urlretrieve(url_link, video_name)
print("done!") 