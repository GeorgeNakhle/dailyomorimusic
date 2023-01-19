import tweepy
import keys
import os
from tinytag import TinyTag

client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

def get_all_songs(folder):
    songs = []
    for file in os.listdir(folder):
        songs.append(file[16:-4])
    print(songs)

def get_all_composers(folder):
    songs = []
    for file in os.listdir(folder):
        song = TinyTag.get(folder + '/' + file)
        print('Composer: ' + song.artist)
        songs.append(song.artist)
    #print(songs)

def create_text(song_name, composer_name):
    print('text created')

def post_tweet(file):
    media = api.media_upload(file)
    api.update_status(text, media_ids = [media.media_id_string])

#post_tweet('./ost/OMORI OST - 008 Trouble Brewing.mp4')
#get_all_songs('./ost')
get_all_composers('./ost')
print("Tweeted successfully!")