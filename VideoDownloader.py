import pytube

__version__ = "1.0.0"

link = input("Enter The Link: ")
yt = pytube.YouTube(link)

print("Title: " + yt.title)
print("Description: " + yt.description)

video = yt.streams.get_highest_resolution()
video.download(r'C:\Users\Jason\Desktop')
