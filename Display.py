"""Everything about the what to show

DISPLAY SHALL

1.  Use a given algorithm to show content
2

ALGORITHM TYPES

1.  TIME (default)
2.
"""

import database
import vlc
import time

class Display:

    algorithm = 'TIME'

    def __init__(self, algorithm):
        print("Display init...")
        if algorithm == 'TIME':
            self.algorithm = 'TIME'
            database_object = database.Database()
            database_object.load_playlist(playlist=database_object.video_playlist_list)
            self.play_by_time(object=database_object)

    def play_by_time(self, object):
        print("Playing by time...")

        while True:
            for video in object.video_playlist_list:
                print("PLaying %s" % video)
                eyivert = vlc.MediaPlayer(video)
                eyivert.play()
                #eyivert.set_fullscreen(1)
                time.sleep(2)
                while eyivert.is_playing():
                    pass
                eyivert.stop()
                self.check_instructions()

    def check_instructions(self):
        """Used to determine whether to come out loop or not"""
        pass



if __name__ == "__main__":
    display_object = Display(algorithm='TIME')
    display_object.play_by_time()