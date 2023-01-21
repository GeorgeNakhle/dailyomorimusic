import tweepy
from dotenv import load_dotenv
import os
import random
import shutil
from tinytag import TinyTag
import time
import datetime

#region CREDENTIALS

load_dotenv()
client = tweepy.Client(os.environ['bearer_token'], os.genvironetenv['api_key'], os.environ['api_secret'], os.environ['access_token'], os.environ['access_token_secret'])
auth = tweepy.OAuth1UserHandler(os.environ['api_key'], os.environ['api_secret'], os.environ['access_token'], os.environ['access_token_secret'])
api = tweepy.API(auth)

#endregion

#region CONSTANTS

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

OST_FOLDER = "./ost"
USED_FOLDER = "./ost-used"
OWNER = "BluePinataSSBM"

#endregion

#region FILE EXPLORER

def move_all_files(source_folder, target_folder):
    files = os.listdir(source_folder)
    for file in files:
        shutil.move(os.path.join(source_folder, file), target_folder)
    print(bcolors.OKGREEN + "Moved all files successfully!" + bcolors.ENDC)

def get_random_file(folder):
    if len(os.listdir(folder)) == 0:
        move_all_files(USED_FOLDER, OST_FOLDER)
    return random.choice(os.listdir(folder))

def move_file(file, folder):
    shutil.move(file, folder)

#endregion

#region POSTING

def get_title(file):
        return file[16:-4]

def get_composition(file):
        song = TinyTag.get(OST_FOLDER + "/" + file)
        return song.artist.replace("/", ", ")

def create_tweet_text(file):
    title = get_title(file)
    composition = get_composition(file)
    tweet_text = title + "\nComposition: " + composition + "\n#OMORI"
    print(bcolors.OKBLUE + tweet_text + bcolors.ENDC)
    return tweet_text

def post_tweet(text, file):
    media = api.media_upload(filename=file, media_category="tweet_video")
    api.update_status(text, media_ids = [media.media_id_string])
    print(bcolors.OKGREEN + "Tweeted successfully!" + bcolors.ENDC)

#endregion

#region LIKING

def find_tweets():
    tweets = api.search_tweets(q="#omori", lang="en", result_type="mixed", count=15)
    for tweet in tweets:
        print(bcolors.OKBLUE + tweet.text + bcolors.ENDC + "\n---------------")
    return tweets

def like_tweets(results):
    count = 0
    for result in results:
        status = api.get_status(result.id)
        if status.favorited == False:
            result.favorite()
            count+=1
    print(bcolors.OKGREEN + "{} tweets liked successfully!".format(count) + bcolors.ENDC)

#endregion

#region ERROR DETECTION

def get_account_id(account):
    user = api.get_user(screen_name=account)
    return user.id_str

def message_account(id, error, time):
    api.send_direct_message(id, "ERROR\n{}\nTimestamp: {}\nFix here: {}".format(str(error), time, "https://github.com/GeorgeNakhle/dailyomorimusic"))
    print(bcolors.OKGREEN + "Direct message sent!" + bcolors.ENDC)

#endregion

# region MAIN

def tasks():
    today_file = get_random_file(OST_FOLDER)
    tweet_text = create_tweet_text(today_file)
    post_tweet(tweet_text, OST_FOLDER + '/' + today_file)
    move_file(OST_FOLDER + '/' + today_file, USED_FOLDER)
    like_tweets(find_tweets())
    print(bcolors.OKGREEN + "Completed tasks for today!" + bcolors.ENDC)

try:
    while True:
        if (datetime.datetime.now().hour >= 9 and datetime.datetime.now().hour <= 12):
            tasks()
        time.sleep(3600 * 3) # 3hr
except Exception as e:
    timestamp = datetime.datetime.now()
    print(bcolors.FAIL + "ERROR\n{}\nTimestamp: {}".format(str(e), timestamp) + bcolors.ENDC)
    message_account(get_account_id(OWNER), str(e), timestamp)
    exit()

#endregion