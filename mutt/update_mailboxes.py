#!/usr/bin/python


raw_list = open("offlineimap.mailboxes.tmp").readlines()
from_list = map(lambda x:x[:-1], raw_list)
forbidden_words = ("quarantaine", "trash", "draft", ".sent", "/sent", "corbeille", "archives")
to_list = filter(lambda x: x != "" and not any(forbidden_word in x.lower() for forbidden_word in forbidden_words), from_list)

# print len(raw_list), raw_list
# print len(from_list), from_list
print len(to_list), to_list

f = open("offlineimap.mailboxes", "wt")
f.write("mailboxes ")
for mb in to_list:
    f.write(mb + " ")
f.write("\n")
