import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def cleanword(string):
    unclean_characters = "?!+=_)(*&%$#@![]{}'><,."
    string_cleaned = ""
    for letter in string:
        if letter not in unclean_characters:
            string_cleaned += letter
    return string_cleaned


def has_dashdash(string):
    dashdash = "--"
    has = False
    if dashdash in string:
        has = True
    return has


def extract_words(string):
    if has_dashdash(string):
        string = string.replace("--", " ")
    return cleanword(string).lower().split()


def wordcount(word, my_list):
    count = 0
    for words in my_list:
        if word == words:
            count += 1
    return count


def wordset(my_list):
    new_list = []
    for words in my_list:
        if words not in new_list:
            new_list.append(words)
    new_list.sort()
    return new_list


def longestword(my_list):
    longest_size = 0
    for words in my_list:
        if len(words) > longest_size:
            longest_size = len(words)
    return longest_size
