# yt-playlist-downloader
Python tool to download YouTube videos using [pytube](https://github.com/pytube/pytube).

### Things you can do
- You can download videos from a YouTube Playlist
- You can extract YouTube video urls from a pdf and download them as well
- Create your own list own YouTube videos and download them
- Edit file names of videos you are downloading
- Follow download progress from terminal

### Things you **cannot** do
- Download 1080p or higher resolutions with audio *(pytube provides at most 720p videos with audio)*.

## Installation
This tool requires an installation of Python 3.6 or greater and pip. (You should have pip already if you have python3, it is typically bundled with python)

If you don't have python install it (Python 3.6 or higher): [python installations](https://python.org/downloads).

If you have python 3.6 or greater already or validated the installation move to following steps.

Clone the repo and go to repo folder
```bash
$ git clone https://github.com/berkinanik/yt-playlist-downloader.git yt-downloader
$ cd yt-downloader
```
If you want a virtual environment and don't want to use global python and packages to run this tool, you need a virtual python env.

### Using with a virtual environment
#### Create a virtual env
```bash
$ python -m venv venv
```
#### Activate the virtual env
MacOS or Linux:
```bash
$ source venv/bin/activate
```
Windows:
```bash
$ venv\Scripts\activate.bat
```
If you have succesfully installed and activated venv you should see ``(venv)`` in front of current directory in the bash line

### Install required python packages
```bash
$ pip3 install -r requirements.txt
```
You should be good to go.


## Usage
Open **``main.py``** and follow the commented instructions to download your youtube videos

If you notice that tool stopped working, most probably it is because of *``pytube``* requires a newer version.

To fix this, activate the venv and

Manually upgrade the pytube:
```bash
$ pip3 install --upgrade pytube
```
Or run this to update all packages:
```bash
$ pip3 install -r requirements.txt --upgrade
```

## Disclaimer
This is not a custom youtube downloader or crawler.

It uses *pytube* and only adds some predefined methods to customize your downloaded video names etc.

All youtube playlist and video urls must lead to some public or unlisted youtube content.

If you are trying to download videos from a private youtube playlist or video it won't work as expected.

#### **Any contribution is appreciated, thanks!**
