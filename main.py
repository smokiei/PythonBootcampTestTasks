"""
Python Bootcamp Test Tasks
There is string s = "Python Bootcamp". Write the code that hashes string.

You are working on a project for TikTok. The future project will be a web-site of all public GIF images.
You need to write a function that converts TikTok video to GIF. The input parameter is url address of TikTok video,
i.e. "TikTok example". The output parameter is path to GIF image, i.e. "/home/user/TikTok-example-1.gif".
"""
import datetime
import hashlib
import os
import time


from moviepy.editor import VideoFileClip

import requests


def get_tiktok_video_url_from_link(link):
    link = link.split("?")[0]

    params = {
        "link": link
    }
    headers = {
        'x-rapidapi-host': "tiktok-info.p.rapidapi.com",
        'x-rapidapi-key': ""
    }

    ### Get your Free TikTok API from https://rapidapi.com/TerminalWarlord/api/tiktok-info/
    # Using the default one can stop working any moment

    api = f"https://tiktok-info.p.rapidapi.com/dl/"
    return requests.get(api, params=params, headers=headers).json()['videoLinks']['download']


def get_tiktok_vid(video_url, filename):
    try:
        video_bytes = requests.get(video_url, headers={"User-Agent": "okhttp"}).content
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    with open(filename, "wb") as out_file:
        out_file.write(video_bytes)


def convert_tiktok_video_gif(video_url):
    # filename = str(int(time.time()))
    filename = datetime.datetime.now().strftime("%y%m%d%H%M%S")

    mp4_filename = f"{filename}.mp4"
    gif_filename = f"{filename}.gif"

    get_tiktok_vid(video_url, mp4_filename)

    try:
        video = VideoFileClip(mp4_filename)
    except IOError as e:
        raise ValueError("Error in video URL, maybe u are trying to proceed wrong video URL")

    video.write_gif(gif_filename)

    return f"{os.getcwd()}\\{gif_filename}"


def string_hash(s):
    h = hashlib.md5(s.encode())
    print(h.hexdigest())


if __name__ == '__main__':
    # the code that hashes string s = "Python Bootcamp"
    s = "Python Bootcamp"
    string_hash(s)

    #url = "https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55"

    #url = "https://www.tiktok.com/@osychenkon/video/7122427392596921606"
    url = "https://www.tiktok.com/@andry3ua/video/7125762860357274885?_t=8UPjvd2ocre&_r=1"
    url = get_tiktok_video_url_from_link(url)
    #print(url)


    print(convert_tiktok_video_gif(url))
