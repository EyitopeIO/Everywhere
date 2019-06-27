"""Managing all the database and stuff"""

import os

userID = os.environ.get('USER') #Obtain user ID
video_path = "/home/"+ userID + "/eyivertVideos/" #standard path


class Database():

    playlist_list = []
    playlist_dict = {"DEFAULT": None}

    def __init__(self):
        if not os.path.exists(video_path):
            os.makedirs(video_path)
        else:
            self.load_playlist(self.playlist_list)

    def remove_item(self, reference):
        pass

    def add_item(self, item):
        pass

    def load_playlist(self, playlist):
        all_videos = os.listdir(video_path)
        #print("all_videos = %s" % all_videos)   #debug
        count = 0
        for items in all_videos:
            #print("items = %s" % items)
            self.playlist_list.append(video_path + all_videos[count])
            #print(self.playlist_list)
            count = count + 1
