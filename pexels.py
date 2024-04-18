from pexelsapi.pexels import Pexels
import os
import random
import requests

dirname = os.path.dirname(__file__)

def load_video(Api_Key,query,min_resolution_width):
    pexel = Pexels(Api_Key)
    search_videos = pexel.search_videos(query=query, orientation='portrait')["videos"]

    max_res_videos = []

    for element in search_videos:
        videos = element["video_files"]
        videos = sorted(videos,key=lambda x: x["width"])
        video = videos[-1]

        max_res_videos.append(video)

    max_res_videos_min_res = [x for x in max_res_videos if x["width"]>=min_resolution_width]
    if len(max_res_videos_min_res) == 0:
        return random.choice(max_res_videos)["link"]
    return random.choice(max_res_videos_min_res)["link"]

def download_video(link,savePath):
    video_response = requests.get(link)

    # Save the video to a file
    with open(savePath, "wb") as f:
        f.write(video_response.content)
