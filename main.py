# Project by: Daniel Peacock
# This project is a Youtube video downloader
# It automatically downloads the highest quality video available

from pytube import YouTube

repeat = "Y"
while repeat == "Y":

    link = input("Enter the link: ")

    yt = YouTube(link)
    print()
    print(yt.title)

    print("Title: " + yt.title)
    print("Number of views: " + str(yt.views))
    print("Length: " + str(yt.length) + " seconds")

    print(yt.streams.filter(progressive=True))

    ys = yt.streams.get_highest_resolution()

    print("Downloading...")
    ys.download()
    print("Download Complete!")
    print()
    repeat = input("Would you like to download another video? (Y/N): ")
