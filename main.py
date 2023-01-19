import tweepy
import keys
import os
import random
import shutil
from tinytag import TinyTag
import schedule
import time

client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

OST_FOLDER = "./ost"
USED_FOLDER = "./ost-used"

#region FILE EXPLORER

def move_all_files(source_folder, target_folder):
    files = os.listdir(source_folder)
    for file in files:
        shutil.move(os.path.join(source_folder, file), target_folder)
    print("Moved all files successfully!")

def get_random_file(folder):
    if len(os.listdir(folder)) == 0:
        move_all_files(USED_FOLDER, OST_FOLDER)
    return random.choice(os.listdir(folder))

def move_file(file, folder):
    shutil.move(file, folder)

#endregion

#region TWITTER

def get_title(file):
        return file[16:-4]

def get_composition(file):
        song = TinyTag.get(OST_FOLDER + "/" + file)
        return song.artist.replace("/", ", ")

def create_tweet_text(file):
    title = get_title(file)
    composition = get_composition(file)
    tweet_text = title + "\n\nComposition: " + composition
    return tweet_text

def post_tweet(text, file):
    media = api.media_upload(filename=file, media_category="tweet_video")
    api.update_status(text, media_ids = [media.media_id_string])
    print("Tweeted successfully!")

#endregion

today_file = get_random_file(OST_FOLDER)
print(create_tweet_text(today_file))
post_tweet(create_tweet_text(today_file), OST_FOLDER + '/' + today_file)
#move_file(OST_FOLDER + '/' + today_file, USED_FOLDER)