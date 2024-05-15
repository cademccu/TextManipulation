
import sys
import re


if len(sys.argv) < 2:
    print("[USAGE]  python3 parse_html.py <INPUT_FILE> <COUNT_BOOLEAN>")
    print("\t<INPUT_FILE>   File containing HTML")
    print("\t<COUNT_BOOLEAN  (optional - default: False) whether or not the ")
    print("\t                count of each tag is displayed. True = display")
    sys.exit(0)

infile_path = sys.argv[1]
display_count = False
if len(sys.argv) == 3:
    if sys.argv[2].lower() == "true":
        display_count = True


html_tag_dictionary = {}

f = open(infile_path, "r")
text = f.read()
f.close()

#basic html matching, might need upgrade
# HTML tags often have <div .....random junk...class...etc....>
# therefore matching \<sometaf\> could TECHNICALLY recursivly
# cover the entire file. In lieu of making a MUCH more robust
# regex, (or iteritively doing it by character...which could
# also work... just pattern match and append '>'. Display will 
# show if this broke something.. in which case I iterate?
html_matcher = re.compile(r"\<[a-zA-Z]+")

tags = html_matcher.findall(text)

# could do this later for speed idk 
tags = [i + ">" for i in tags]

# toss em in dictionary
for i in tags:
    if not html_tag_dictionary.get(i):
        html_tag_dictionary[i] = 0
    html_tag_dictionary[i] += 1

# sort dictionary by occurence
html_tag_dictionary = dict(sorted(html_tag_dictionary.items(), key=lambda item: item[1], reverse=True))


for key, value in html_tag_dictionary.items():
    out_str = ""
    # make it pretty
    if display_count:
        out_str += str(value).ljust(6)
    out_str += key
    print(out_str)
        
    
# print out the list for use in program
print(list(html_tag_dictionary.keys()))

