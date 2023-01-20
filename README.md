# Daily OMORI Music

![Daily_OMORI_Music_logo](pics/dailyomorimusic-pfp.png)

**Author**: George Nakhle

## About

[@dailyomorimusic](https://twitter.com/dailyomorimusic) \
Daily OMORI Music is a Twitter bot that post songs from the [OMORI OST](https://open.spotify.com/artist/4DoTDDfW3gkeyb06XrIHlg) everyday between **9:00am** - **12:00am PST**. The bot is written in Python and takes advantage of the [Tweepy](https://github.com/tweepy/tweepy) library to easily interface with [Twitter's API](https://developer.twitter.com/en/docs/twitter-api).

## Functionality

- **Posting**
  - Posts daily tweets.
  - Includes the song title and credits the composer(s) in every tweet.
- **Liking**
  - Performs a daily search query for #OMORI.
  - Likes at most 15 tweets from the query.
- **Error Detection**
  - Sends a direct message to the account owner ([@BluePinataSSBM](https://twitter.com/bluepinatassbm)) if an error is detected.