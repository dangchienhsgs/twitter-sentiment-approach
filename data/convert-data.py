import random
from collections import defaultdict


def create_small_train():
    f1 = open("train-converted.csv")

    data = defaultdict()

    data['negative'] = []
    data['positive'] = []

    for line in f1:
        args = line.split(",")

        label = args[0].replace("|", "")
        tweet = args[1].replace("|", "")

        data[label].append(tweet)

    total_positive = len(data['positive'])
    total_negative = len(data['negative'])

    num_positive = 8000
    num_negative = 8000

    positive_members = random.sample(xrange(0, total_positive), num_positive)
    negative_members = random.sample(xrange(0, total_negative), num_negative)

    train_file = open("train_small.csv", "w")
    raw_tweet = open("raw_tweet.csv", "w")

    for i in positive_members:
        train_file.write('{0}|||{1}'.format('positive', data['positive'][i]))
        raw_tweet.write(data['positive'][i])

    for i in negative_members:
        train_file.write('{0}|||{1}'.format('negative', data['negative'][i]))
        raw_tweet.write(data['negative'][i])

    train_file.close()


def create_small_test():
    f1 = open("test-converted.csv")

    data = defaultdict()

    data['negative'] = []
    data['positive'] = []
    data['neutral'] = []

    for line in f1:
        args = line.split(",")

        label = args[0].replace("|", "")
        tweet = args[1].replace("|", "")

        data[label].append(tweet)

    total_positive = len(data['positive'])
    total_negative = len(data['negative'])

    test_file = open("test_small.csv", "w")
    raw_tweet = open("raw_tweet_test.csv", "w")

    for i in range(0, total_positive):
        test_file.write('{0}|||{1}'.format('positive', data['positive'][i]))
        raw_tweet.write(data['positive'][i])

    for i in range(0, total_negative):
        test_file.write('{0}|||{1}'.format('negative', data['negative'][i]))
        raw_tweet.write(data['negative'][i])

    test_file.close()


create_small_test()