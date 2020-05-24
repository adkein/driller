#!/usr/bin/env python3

import itertools as it
import yaml


LOOKBACK_WINDOW = 3

LANGUAGES = ["deutsch", "english"]


def quiz(entry, flip):
    query_language = LANGUAGES[int(flip)]
    response_language = LANGUAGES[int(not flip)]

    translations = entry["translations"]

    input("Quiz: {}".format(translations[query_language]))
    input("Translation: {}".format(translations[response_language]))
    print("\n" + ("-" * 50) + "\n")


def load_entries():
    return yaml.load(open("entries.yml", "r").read())["meanings"]


def main():
    entries = load_entries()

    for i in it.cycle(range(len(entries))):
        for j in range(LOOKBACK_WINDOW):
            quiz(entries[i-j], flip=bool(j % 2))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nFine, who needs you anyway, I have better things to do too, you know!  :_(\n")
