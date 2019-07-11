"""Managing all the database and stuff"""

import os
import json

#database functions work on both photo and videos
IMAGE = 'IMAGE'
VIDEO = 'VIDEO'

userID = os.environ.get('USER') #Obtain user ID
file_path = "/home/"+ userID + "/eyiVert/"
video_path = "/home/"+ userID + "/eyiVert/eyivertVideos/" #standard path
image_path = "/home/"+ userID + "/eyiVert/eyivertImages/"


class Database:

    video_playlist_list = []
    video_playlist_dict = {"DEFAULT": None}
    image_playlist_list = []
    image_playlist_dict = {"DEFAULT": None}

    store_dict ={}

    def __init__(self):
        print("Database init...")
        if not os.path.exists(video_path):
            os.makedirs(video_path)
        if not os.path.exists(image_path):
            os.makedirs(image_path)
        if not os.path.isfile(file_path + 'store.json'):
            f = open(file_path + 'store.json', 'w')
            f.close()

    def remove_content(self, type, file_name):
        if type == VIDEO:
            if os.path.isfile(video_path + file_name):
                os.remove(video_path + file_name)
            else:
                #Tell doctor
                pass
        if type == IMAGE:
            if os.path.isfile(image_path + file_name):
                os.remove(image_path + file_name)
            else:
                #Tell doctor
                pass

    def add_content(self):
        """connect to google drive, download video, save in folder"""

    def save_json(self, _dict):
        """File format is a dictionary of dictionaries of customer video and preference"""
        json_data = json.dump(_dict)
        f = open(file_path + 'store.json', 'w')
        f.write(json_data)
        f.close()

    def load_json(self, file_name):
        with open(file_path + file_name, 'r') as f:
            self.store_dict = json.load(f)
            f.close()

    def load_playlist(self, playlist):
        print("Loading playlist...")
        all_videos = os.listdir(video_path)
        count = 0
        for items in all_videos:
            self.video_playlist_list.append(video_path + all_videos[count])
            count = count + 1
