"""
Analyze, whether the content of a given social media webpage could
potentially polarize a user or not
"""

import re

def calc_polarizing_probability(domain, content):
    """ Returns a probability that the content of a domain will polarize users
    Parameters
--------------------------------------------------------------------------------
    domain: str
	domain name of the social media webpage
    content: str
        innerText of the given domain/page

    Returns
--------------------------------------------------------------------------------
    probability: float
        the probability that the content of the page will polarize a user, where
    0 is the minimum probability and 1 is the maximum probability
    """

    # clean string
    words = content.rstrip().split("%20")
    # list of bad words
    triggers = ["news", "religion", "politics"]
    # look for words like news, religion, politics, a.m.o. TODO in the string
    topic_count = 0
    for word in triggers:
        if word in words:
            topic_count += 1
    # normalize topic_count
    topic_norm = topic_count / len(words)

    # look for emojis in the string
    # https://stackoverflow.com/questions/36216665/find-there-is-an-emoji-in-a-string-in-python3
    def count_emoji(s):
        count = 0
        emojis = "😂😍🤪🤫🤔😒😬🤥😢😭😱😤😡😘😅" # Think about escape
        # sequences, unicode, etc.
        for emoji in emojis:
            count += s.count(emoji)
        return count

    emoji_count = count_emoji(content)
    emoji_norm = emoji_count / len(content)

    topic_weight = .6
    emoji_weight = .4

    probability = topic_weight*topic_norm + emoji_weight*emoji_norm

    return probability

