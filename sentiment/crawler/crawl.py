from TwitterSearch import *
import random
import codecs
import uuid


def crawl(filename, keywords, language):
    f = codecs.open(filename, "a", "utf-8")
    try:
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
        tso.set_keywords(keywords)  # let's define all words we would like to have a look for
        tso.set_language(language)  # we want to see German tweets only
        tso.set_include_entities(False)  # and don't give us all those entity information

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key='MozbqzFag8UQMbuw9qkuyG7Fm',
            consumer_secret='c4m8EKOwQb90A3nLLySKSEkV7fVXe8taZq4IjgDrMVKihbNW4s',
            access_token='2684788650-VOzUZGhPItlgye6w5LhX5QMevWLK8WTALcxe8KM',
            access_token_secret='9IeW0F8XFnZ7FV5sCyZIahLEZBQTkzwO4L0q3vqRkl4je'
        )

        # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso):
            tweet_text = tweet['text'].replace("\n", " ")
            id1 = uuid.uuid4()
            id2 = uuid.uuid4()
            label = random_label()
            f.write('@%s\t%s\t%s\t%s\n' % (id1, id2, label, tweet_text))

    except TwitterSearchException as e:  # take care of all those ugly errors if there are some
        print(e)

    f.close()


def random_label():
    t = random.randint(0, 3)
    if t % 3 == 0:
        return "positive"
    elif t % 3 == 1:
        return "negative"
    elif t % 3 == 2:
        return "neutral"


if __name__ == "__main__":
    #crawl("Twitter.txt", ["Twitter"], "en")
    crawl("Google.txt", ["Google", "Android"], "en")
    #crawl("Microsoft.txt", ["Microsoft", "Windows", "Windows Phone"], "en")
    #crawl("Apple.txt", ["Apple", "Iphone"], "en")


