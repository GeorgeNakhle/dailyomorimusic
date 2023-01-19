import tweepy
import keys

def api():
    auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print("Tweeted successfully!")

if __name__ == '__main__':
    api = api()
    tweet(api, 'This was tweeted from Python', './ost/dailyomorimusic-pfp.jpg')

#Todo
#https://omori.fandom.com/wiki/MUSIC add composer (change file metadataa?)