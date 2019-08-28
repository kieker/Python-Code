# I got tired of having to search for song lyrics everytime i listen to a song. This program checks my spotify playback status then scrapes a-z lyrics for the lyrics of the song that I am listening to. Planned for future versions: build gui, refactor into classes for code organisation & scrape genius lyrics instead of a-z

from bs4 import BeautifulSoup
import requests
import urllib
import json

import spotipy

import spotipy.util as util
import tkinter as tk
import os

from spotipy import Spotify

SPOTIPY_CLIENT_ID = 'client id taken out for security purposes'
SPOTIPY_CLIENT_SECRET = 'client secret taken out for security purposes'
SPOTIPY_REDIRECT_URI = 'https://google.com/'



def display_error_message(ex):
     errormessage = "An exception of type {0} occurred. Arguments: \n{1!r}"
     message = errormessage.format(type(ex).__name__, ex.args)
    #print("There was an issue with the program, please try again later")
     print(message)

def check_for_playback(spotify,song = ''):
    user_play = spotify.current_user_playing_track()
    if user_play['is_playing']:
        return True
    else:
        return False

def convert_song_to_object(song):
    song_str = json.dumps(song)
    song_obj = json.loads(song_str)
    return song_obj

def get_current_song_info(spotify, old_song=''):
   current_song = spotify.current_user_playing_track()
   if old_song == '':
       return current_song, False
   curr_song_data = convert_song_to_object(current_song)
   prev_song_data = convert_song_to_object(old_song)

   if curr_song_data["item"]["id"] != prev_song_data["item"]["id"]:
       return current_song, True # the song has changed
   else:
       return current_song, False


def get_lyrics(song):
    song_name = str(song["item"]["name"]).lower()
    song_artist = str(song["item"]["artists"][0]['name']).lower()


    song_artist = ''.join(e for e in song_artist if e.isalnum())
    song_name = ''.join(e for e in song_name if e.isalnum())
    print(song_name)
    print(song_artist)

    #TODO: implement beautifulsoup to go to https://www.azlyrics.com/lyrics/artist/songname.html and scrape
    lyrics = []
    scrape_url = 'http://www.azlyrics.com/lyrics/'+song_artist+'/'+song_name+'.html'
    page_response = requests.get(scrape_url,timeout=5)
    if page_response.status_code == 200:
        print("connected to site")
        page_content = BeautifulSoup(page_response.content, 'html.parser')
        main_container = page_content.find("div", class_='main-page')
        lyrics_container = main_container.find_all("div", class_="text-center")
        paragraph = lyrics_container[1].find_all("div")
        lyrics_div = paragraph[6].text
        the_lyrics = lyrics_div.splitlines()
        lyrics = the_lyrics
        return lyrics
    else: return "There was a problem connecting to the site"

def mainLoop(spotifyObject):
    playback = check_for_playback(spotifyObject)
    if playback:
        song, changed = get_current_song_info(spotifyObject, '')
        print(json.dumps(song, sort_keys=True, indent=4))
    else:
        print("No song currently playing. Please try again later")
    while playback:
        playback = check_for_playback(spotifyObject)
        while playback:
            playback = check_for_playback(spotifyObject)
            song, changed = get_current_song_info(spotifyObject, song)
            #print(json.dumps(song, sort_keys=True, indent=4))

            if changed:
                song_data = convert_song_to_object(song)
                print("song was changed")
                lyr = get_lyrics(song_data)

                for i in lyr:
                    print(i)
                    print()
                changed = False
try:
    # print(json.dumps(VARIABLE, sort_keys=True, indent=4)) code snippet to print json data

    user_id = input("Please enter user id:")
    token = util.prompt_for_user_token(user_id,'user-read-playback-state', client_id = '5da1070f0d344e94ac7ca2a36a977ff8', client_secret= '523c7930cada4d2fb992728562dccd63', redirect_uri= 'https://www.google.com/' )
    spotifyObject = spotipy.Spotify(auth=token)

    if token:
        print("user successfully verified")
    else:
        print("problem with verification")

    # user = spotifyObject.current_user() #Prints some user information, if you should need it
    mainLoop(spotifyObject)


    user_act = input("Are you planning on playing another song soon?")

    while user_act.lower() not in ("y","n"):
        print("Sorry, I don't understand. Y/N:")
        user_act = input("Are you planning on playing another song soon?")
    if user_act.lower() == "y":
        mainLoop(spotifyObject)

except Exception as e:

    display_error_message(e)
    
# class Gui:
# code to be implemented in a future version
# class SpotifyLyrics:
# code to be implemented in a future version 