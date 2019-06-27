"""Logic right here. Decsion maker here"""

import database
import vlc
import time

class Logic:

    def __init__(self):
        pass

    def send_to_display(self):

        for video in data.playlist_list:
            print("PLaying %s" % video)
            eyivert = vlc.MediaPlayer(video)
            eyivert.play()
            eyivert.set_fullscreen(1)
            time.sleep(2)
            while(eyivert.is_playing()):
                pass
            eyivert.stop()




if __name__ == "__main__":
    print("START")
    data = database.Database()
    logic = Logic()
    logic.send_to_display()
    print("END")