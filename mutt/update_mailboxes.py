#!/usr/bin/python
import os
import re


raw_list = open("offlineimap.mailboxes.tmp").readlines()
from_list = map(lambda x: x[:-1], raw_list)


def keep_this_mailbox(x):
    if x == "":
        return False
    forbidden_words = ("quarantaine", "trash", "draft", ".sent", "/sent", "corbeille", "archives")
    if any(forbidden_word in x.lower() for forbidden_word in forbidden_words):
        return False
    folder = os.path.join(os.path.expanduser("~/Mails"), x[2:-1])
    total_files = 0
    for root, dirs, files in os.walk(folder):
        total_files += len(files)
    if total_files == 0:
        return False
    return True

to_list = filter(lambda x: keep_this_mailbox(x), from_list)


#sort from account priority
def mb_sort(mb1, mb2):
    # get first part
    regexp = "\"\+(.*)/(.*)\""
    match1 = re.match(regexp, mb1)
    match2 = re.match(regexp, mb2)

    def str_cmp(s1, s2):
        if s1 < s2:
            return -1
        elif s1 > s2:
            return +1
        else:
            return 0
    if match1.group(1) == match2.group(1):
        return str_cmp(match1.group(2), match2.group(2))
    order = ["frozax", "laposte", "gffree", "fgfree"]
    return order.index(match1.group(1)) - order.index(match2.group(1))


to_list.sort(cmp=mb_sort)

# decomment this for this to work
f = open("offlineimap.mailboxes", "wt")
f.write("mailboxes ")
for mb in to_list:
    f.write(mb + " ")
f.write("\n")
