import jsonlines
import pandas as pd
import matplotlib.pyplot as plt
import pylab

def readTwitterData(twitterDataFile):
    tweets = []
    with jsonlines.open(twitterDataFile) as infile:
        reader = jsonlines.Reader(infile)
        for line in reader:
            tweets.append(line)
    print(type(tweets[0]))
    return tweets


def key_words(row):
    words = []
    if row['text']:
        text = row['text'].lower()
        if "trump" in text:
            words.append('trump')
        if 'president' in text:
            words.append('president')
        if 'biden' in text:
            words.append('biden')
        if 'pennsylvania' in text:
            words.append('pennsylvania')
        if 'election' in text:
            words.append('election')

    return ','.join(words)


if __name__ == '__main__':
    tweets = pd.DataFrame()
    tweet_file = 'output.json'
    tweet_data = readTwitterData(tweet_file)
    tweets['text'] = list(map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweet_data))
    tweets['words'] = tweets.apply(key_words, axis=1)
    counts = pd.DataFrame(tweets.words.value_counts())
    print(counts)
    counts.plot(kind='bar')
    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize='15')
    ax.tick_params(axis='y', labelsize='10')
    ax.set_xlabel('Key Words', fontsize=15)
    ax.set_ylabel('Number of Tweets', fontsize=15)
    ax.set_title('Key Words', fontsize=15,
                  fontweight='bold')
    counts[1:5].plot(ax=ax, kind='bar', color='red')

    pylab.show()
