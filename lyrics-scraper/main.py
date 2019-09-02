from bs4 import BeautifulSoup
import requests
import json
import spotipy
import spotipy.util as util
from spotipy import Spotify
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QLineEdit,QLabel
import os

SPOTIPY_CLIENT_ID = 'client_key_redacted'
SPOTIPY_CLIENT_SECRET = 'client_secret_redacted'
SPOTIPY_REDIRECT_URI = 'https://google.com/'

class SpotifyRequest:

    def __init__(self):
        self.status_code = '0'
        self.user_id = ''
        self.spotify_handler = None


    def create_handler(self):

            self.spotify_handler = spotipy.Spotify(auth=self.token)
            print('success with verification inside handler')
            return

    def auth_user(self,the_user_id):
        self.user_id = the_user_id
        self.token = util.prompt_for_user_token(the_user_id, 'user-read-playback-state',
                                                client_id='5da1070f0d344e94ac7ca2a36a977ff8',
                                                client_secret='523c7930cada4d2fb992728562dccd63',
                                                redirect_uri='https://www.google.com/')

        if self.token:
            self.authenticated = True
            print("user successfully verified")
            self.status_code = 200
            self.create_handler()
            return self.status_code

        else:
            self.authenticated = False
            print("problem with verification")
            self.status_code = 500
            return self.status_code


    def current_user(self):
        user = self.spotify_handler.current_user()
        print(json.dumps(user, sort_keys=True, indent=4))


    def convert_song_to_object(self, song):
        song_str = json.dumps(song)
        song_obj = json.loads(song_str)
        return song_obj


    def get_current_song_info(self, old_song=''):
        first_run = False
        curr = self.spotify_handler.current_user_playing_track()

        if old_song == '':
            first_run = True
            #return current_song, False
        curr_song_data = self.convert_song_to_object(curr)
        prev_song_data = self.convert_song_to_object(old_song)

        if first_run:
            return curr, True
        if curr_song_data["item"]["id"] != prev_song_data["item"]["id"] or first_run:
            return curr, True # the song has changed
        else:
            return curr, False


    def get_lyrics(self, song):
        song_data = self.convert_song_to_object(song)
        song_name = str(song_data[0]["item"]["name"]).lower()
        song_artist = str(song_data[0]["item"]["artists"][0]['name']).capitalize()

        song_artist = song_artist.replace(' ', '-')
        song_name = song_name.replace(' ', '-').lower()
        
        print(song_name) #for debug purposes
        print(song_artist)

        lyrics = []
        scrape_url = 'http://www.genius.com/'+song_artist+'-'+song_name+'-lyrics'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

        page_response = requests.get(scrape_url,headers=headers, timeout=10)
        print("trying to connect")
        if page_response.status_code == 200:
            print("connected to site")
            page_content = BeautifulSoup(page_response.content, 'html.parser')
            main_container = page_content.find("div", class_='lyrics')
            # lyrics_container = main_container.find_all("div", class_="text-center")
            paragraph = main_container.find_all("p")
            lyrics_div = paragraph[0].text
            the_lyrics = lyrics_div.splitlines()
            lyrics = the_lyrics
            print(lyrics)
            return lyrics
        else: print("There was a problem connecting to the site: " + str(page_response.status_code))
        return "no lyrics found"

    def check_if_playing(self):
        playback = self.spotify_handler.current_user_playing_track()
        if playback:
            return True
        else:
            return False

class Gui:
    def __init__(self,spotify):
        self.app = QApplication([])
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.spotify = spotify
        self.account = '3nf1gn8sgkpfdknxxch66kp7x'
        self.user_id = ''
        self.authenticated = False
        self.status_message = ''


    def check_auth(self):
        print("checking user account")
        
        if self.authenticated:
            print("User already authenticated")
            status = self.spotify.status_code
            return status
        else:
            user_id = self.get_user()
            print(str(user_id) + " user not authenticated")
            status = self.spotify.status_code
            self.spotify.auth_user(user_id)
            self.logged_in(self.spotify)
            return status
      

    def update_lyrics(self, lyrics):

        if lyrics:
            lyrics_arr = lyrics[1:]

            lyrics_string = "\n".join(lyrics_arr)

            self.lyrics.setText(lyrics_string)
            print("lyrics string: " + lyrics_string)
        self.layout.addWidget(self.lyrics)

    def scrape_for_lyrics(self):
        print("scraping")
        playback = self.spotify.check_if_playing()
        if playback:
            song, changed = self.spotify.get_current_song_info('')
            song_data = self.spotify.get_current_song_info(song)
            lyr = self.spotify.get_lyrics(song_data)
            for i in lyr:
                print(i)
                print()
            if lyr:
                self.update_lyrics(lyr)
        else:
            print("No song currently playing. Please try again later")
        


    def logged_in(self, spotifyOb):
        playback = spotifyOb.check_if_playing()
        if playback:
            song = spotifyOb.get_current_song_info()
            self.layout.addWidget(self.get_lyrics_button)


    def main_gui(self):
        self.user_id_field= QLineEdit()
        self.layout.addWidget(self.user_id_field)

        self.use_acc_button = QPushButton("Use Account")
        self.layout.addWidget(self.use_acc_button)

        self.get_lyrics_button = QPushButton("Get Lyrics")

        self.lyrics = QLabel()
        label = QLabel("Welcome to KiekerLyrics")
        self.layout.addWidget(label)

        label2 = QLabel("User id (this can be acquired from your profile, otherwise just use your account name):")
        self.layout.addWidget(label2)
        self.window.setLayout(self.layout)


    def run_gui(self):
        self.use_acc_button.clicked.connect(self.check_auth)
        self.get_lyrics_button.clicked.connect(self.scrape_for_lyrics)
        self.window.show()
        self.app.exec_()


    def get_user(self):
        self.account = self.user_id_field.text()
        if self.account:
            print("User account: " + self.account)
            return self.account
        else:
            return '0'


def display_error_message(ex):
     errormessage = "An exception of type {0} occurred. Arguments: \n{1!r}"
     message = errormessage.format(type(ex).__name__, ex.args)
     #print("There was an issue with the program, please try again later")
     print(message)



#try:
    # 3nf1gn8sgkpfdknxxch66kp7x - my spotify user id
    # print(json.dumps(VARIABLE, sort_keys=True, indent=4)) - for copying later on

spoofy = SpotifyRequest()
the_gui = Gui(spoofy)
the_gui.main_gui()
the_gui.run_gui()
print("done")
# except Exception as e:
 #   display_error_message(e)