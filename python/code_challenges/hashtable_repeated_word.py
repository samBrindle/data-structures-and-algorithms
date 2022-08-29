from data_structures.hashtable import Hashtable
import re


def first_repeated_word(string):
    hashtable = Hashtable()
    regex = r"[.|,|?|!]"
    regex_str = re.sub(regex, "", string)
    split_str = regex_str.lower().split()

    for word in split_str:
        if hashtable.contains(word):
            return word
        hashtable.set(word, 1)

    return None

