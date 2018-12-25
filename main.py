import tweepy
from tweepy import OAuthHandler

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# Creating the authentication object
auth = OAuthHandler(consumer_key, consumer_secret)

# Setting your access token and secret
auth.set_access_token(access_token, access_secret)

# Creating the API object while passing in auth information
api = tweepy.API(auth)


user_choice = int(input("Press 1 to pull 10 most recent tweets from your Timeline feed \n"
                        "Press 2 to pull latest 10 tweets from a specified user \n"
                        "Press 3 to find tweets using a keyword \n"
                        ))

if user_choice == 1:
    # Using the API object to get tweets from timeline and storing it in a variable
    public_tweets = api.home_timeline()

    # foreach through all tweets pulled
    for tweet in public_tweets:
        # printing the text stored inside the tweet object
        print(tweet.user.screen_name, "Tweeted:", tweet.text)

if user_choice == 2:
    name = input("Please give us the name of The Twitter user: ")
    print("")
    tweetCount = 10
    results = api.user_timeline(id=name, count=tweetCount)

    for tweet in results:
        print(tweet.user.screen_name, "Tweeted:", tweet.text)

if user_choice == 3:
    query = input("Please give us the search query string: ")
    print("")
    # Language code (follows ISO 639-1 standards)
    language = "en"

    # Calling the user_timeline function with our parameters
    results = api.search(q=query, lang=language)

    # foreach through all tweets pulled
    for tweet in results:
        # printing the text stored inside the tweet object
        print(tweet.user.screen_name, "Tweeted:", tweet.text)
else:
    continue 



