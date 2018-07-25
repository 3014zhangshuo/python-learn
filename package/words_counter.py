"""Fetch words from url count frequency

Usage:
    python package words_counter.py
"""
from urllib.request import urlopen

def count_words():
    """

    Args:
        None

    Return:
        A dict with words number.
    """
    response = urlopen("https://eggman.tv/files/w.txt")
    words = {}

    for line in response.readlines():
        data = line.split()
        for word in data:
            word = word.decode('utf-8').lower()
            words[word] = words.get(word, 0) + 1

    # print(word) print last word is data can access

    return words

def print_count(words):
    for key in words:
        print(key, words[key])

def main():
    print_count(count_words())

if __name__ == "__main__":
    main()
