from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # delclear variables
    li_len = 0
    a_list = a.split("\n")
    b_list = b.split("\n")
    sim_list = []

    # judge comparing line's length
    if len(a_list) < len(b_list):
        li_len = len(a_list)
    else:
        li_len = len(b_list)

    # append lines corresponding between a and b to sim_list
    for a_item in a_list:
        for b_item in b_list:
            if a_item == b_item:
                sim_list.append(a_item)
                break

    # print(a_list)
    # print(b_list)
    # print(sim_list)

    return sim_list


def sentences(a, b):
    """Return sentences in both a and b"""

    # split sentences by sentence
    a_list = sent_tokenize(a, language='english')   # split by '.'
    a_list = list(dict.fromkeys(a_list))
    b_list = sent_tokenize(b, language='english')
    b_list = list(dict.fromkeys(b_list))

    # judge comparing line's length
    li_len = 0
    if len(a_list) < len(b_list):
        li_len = len(a_list)
    else:
        li_len = len(b_list)

    # append sentences corresponding between a and b to sim_list
    sim_list = []
    for a_item in a_list:
        for b_item in b_list:
            if a_item == b_item:
                sim_list.append(a_item)
                break

    # print(a_list)
    # print(b_list)
    # print(sim_list)
    return sim_list


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # store each strings(a and b) as substring
    a_list = []
    b_list = []
    a_substr_num = len(a) - n + 1
    b_substr_num = len(b) - n + 1
    substr = ""

    # create substrings list by each strings(a and b)
    for i in range(a_substr_num):
        substr = ""
        for j in range(i, i+n, 1):
            substr = substr + a[j]
        a_list.append(substr)
    a_list = list(dict.fromkeys(a_list))

    for i in range(b_substr_num):
        substr = ""
        for j in range(i, i+n, 1):
            substr = substr + b[j]
        b_list.append(substr)
    b_list = list(dict.fromkeys(b_list))

    # append substrings corresponding between a and b to sim_list
    sim_list = []
    for a_item in a_list:
        for b_item in b_list:
            if a_item == b_item:
                sim_list.append(a_item)
                break

    # print(a_list)
    # print(b_list)
    # print(sim_list)

    return sim_list

