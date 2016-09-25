import pandas
import uuid
import numpy as np
import random
from collections import *


def export_content():
    data = pandas.read_csv("full-corpus.csv")
    size = len(data['TweetText'])
    f1 = open("tweet_text.txt", "w")
    for i in range(0, size):
        f1.write(data['TweetText'][i])
        f1.write("\n")

    f1.close()


def convert(filename, fileout):
    data = pandas.read_csv(filename)

    rows = data.shape[0]
    f = open(fileout, "w")
    for i in range(0, rows):
        content = data['TweetText'][i].replace("\n", " ")
        sentiment = data['Sentiment'][i]

        if sentiment != 'irrelevant':
            line = "{0}\t{1}\t{2}\t{3}".format(data['TweetId'][i], uuid.uuid4(), data['Sentiment'][i],
                                               content)
            f.write(line)
            f.write("\n")
    f.close()


def divides(filename, training, testing, ratio):
    f = open(filename)

    lines = []
    for line in f:
        lines.append(line)

    f1 = open(training, "w")
    f2 = open(testing, "w")

    training_size = int(len(lines) * ratio)
    training_indices = random.sample(range(0, len(lines)), training_size)
    testing_indices = [x for x in range(0, len(lines)) if x not in training_indices]

    for i in training_indices:
        f1.write(lines[i])

    for i in testing_indices:
        f2.write(lines[i])

    f1.close()
    f2.close()


convert("Apple.txt", "twitter_converted.csv")
convert("google.txt", "google_converted.csv")
convert("microsoft.txt", "microsoft_converted.csv")
convert("apple.txt", "apple_converted.csv")

divides("twitter_converted.csv", "twitter_training_80.csv", "twitter_testing_80.csv", 0.8)
divides("google_converted.csv", "google_training_80.csv", "google_testing_80.csv", 0.8)
divides("microsoft_converted.csv", "microsoft_training_80.csv", "microsoft_testing_80.csv", 0.8)
divides("apple_converted.csv", "apple_training_80.csv", "apple_testing_80.csv", 0.8)
