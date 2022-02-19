from pytube import Playlist, YouTube, Stream, StreamQuery
import re

from tools.extract_links_from_pdf import extractLinksFromPDF

#! DISCLAIMER
# all youtube playlist and video urls must lead to public or unlisted youtube content
# if you are trying to reach a private youtube playlist or video wont work as expected


def main():
    # DOWNLOAD VIDEOS FROM YOUTUBE PLAYLIST
    # use following line to extract youtube videos from a youtube playlist

    # TODO edit following url for your platlist

    videos = Playlist("https://www.youtube.com/playlist?list=[playlist-ID]")
    # example
    # videos = Playlist(
    #     "https://www.youtube.com/playlist?list=PLEboAksnoN7UtpR7gJzCsZFCPbOo3ur0s"
    # )

    # download path of videos to be downloaded to

    # TODO edit following string for where videos to be downloaded to

    # use following line for windows

    downloadPath = "C:\\Path\\To\\Your\\Download\\Folder\\"
    # example
    # downloadPath = "C:\\Users\\Berkin\\Desktop\\YoutubeDownloads\\ee302-vids\\"

    # use following line for macOS or linux

    # downloadPath = "/path/to/your/download/folder/"

    # file name prefix to be added all downloaded videos
    # TODO edit following string for file name prefix

    fileNamePrefix = "file-name-prefix"
    # example
    # fileNamePrefix = "ee302-2020s"

    # EXTRACT YOUTUBE LINKS FROM PDF
    # you can extract youtube links from pdf and you the array returned to download youtube videos
    #! DISCLAIMER
    # script does not search for youtube links as plain text
    # it only looks for anchors of youtube links as hyperlinks
    # if you have a pdf that contains clickable valid urls of youtube links you can use this
    # there is a validation regex used for validating youtube vid links
    # it is not guaranteed to be working flawlessly

    # TODO uncomment following line and edit pdf path to extract videos from pdf

    # Windows

    # videos = extractLinksFromPDF("C:\\Path\\To\\example-pdf-containing-youtube-video-url-anchors.pdf")
    # videos = extractLinksFromPDF("C:\\Users\\Berkin\\Desktop\\link-pdf.pdf")

    # MacOS or Linux

    # videos = extractLinksFromPDF("/path/to/example-pdf-containing-youtube-video-url-anchors.pdf")

    # CREATE YOUR OWN LIST OF VIDEOS
    # you might use this type of an array of youtube video links to download

    # TODO uncomment following lines and create your own array of youtube vid links

    # videos = [
    #     "https://www.youtube.com/watch?v=[video-id1]",
    #     "https://www.youtube.com/watch?v=[video-id2]",
    # ]

    # counter of videos downloaded
    # you might change this to number whether you want counter index to be start from
    count = 1

    for vidLink in videos:
        ytVid = YouTube(vidLink)
        # registering progress callback
        global previousProgress
        previousProgress = 0
        print(ytVid.title)
        ytVid.register_on_progress_callback(on_progress)
        result = ytVid.streams.get_highest_resolution()
        fileName = (
            fileNamePrefix
            + f"-{'0'+str(count) if count < 10 else count}-"
            + result.title.lower()
            .replace("metu", "") #remove unwanted words
            .replace("2020", "") #or numbers
            .replace("odtu", "metu") #or replace words
            #examples
            # .replace("ee302", "")
            # .replace("feedback systems", "")
            # .replace("- (Lectures on Feedback Control Systems)".lower(), "")
            # .replace("spring 2021", "")
            + ".mp4"
        )
        invalidChars = '<>:;_,"/\|?* '
        # removing invalids chars from name and replacing with -
        for char in invalidChars:
            fileName = fileName.replace(char, "-")
        # remove dash repetition
        fileName = re.sub("\-+", "-", fileName)
        print(fileName)
        result.download(downloadPath, fileName)
        count += 1


# callback to follow downloading progress
previousProgress = 0


def on_progress(stream, chunk, bytesRemaining):
    global previousProgress
    totalSize = stream.filesize
    bytesDownloaded = totalSize - bytesRemaining

    liveProgress = (int)(bytesDownloaded / totalSize * 100)
    if liveProgress > previousProgress:
        previousProgress = liveProgress
        print(liveProgress)


main()
