from pexelsapi.pexels import Pexels
import os
import random
import requests

dirname = os.path.dirname(__file__)

def load_video(Api_Key,query,min_resolution_width):
    # Get a list of videos in portrait mode
    pexel = Pexels(Api_Key)
    search_videos = pexel.search_videos(query=query, orientation='portrait')["videos"]

    # For each video get the version with the highest Resolution
    max_res_videos = []

    for element in search_videos:
        videos = element["video_files"]
        videos = sorted(videos,key=lambda x: x["width"])
        video = videos[-1]

        max_res_videos.append(video)

    # Choose a random video with the specified resolution
    max_res_videos_min_res = [x for x in max_res_videos if x["width"]>=min_resolution_width]
    if len(max_res_videos_min_res) == 0:
        return random.choice(max_res_videos)["link"]
    return random.choice(max_res_videos_min_res)["link"]

def download_video(link,savePath):
    # Download a video provided a link
    video_response = requests.get(link)

    # Save the video to a file
    with open(savePath, "wb") as f:
        f.write(video_response.content)

def getVideo(filepath,query,Api_Key,vertical_res = 1080):
    video_link = load_video(Api_Key,query,vertical_res)
    download_video(video_link,filepath)