
import sys
import random
if len(sys.argv) < 2:
    print("""
[USAGE]  python3 scramble.py <INPUT_FILE> <MIN_SPACE> <MAX_SPACE> <OUTPUT_FILE>
    INPUT_FILE  :   A text file
    MIN_SPACE   :   INT (inclusive) of minimum gap between words before another HTML tag
    MAX_SPACE   :   INT (exclusive) maximum gap between tags before an HTML tag
    OUTPUT_FILE :   Optional. Name of output file. Defaults to stdout

    This program adds html tags at random between the provided interval.
""")
    sys.exit(0)


# TODO this could be flexible?
# maybe from a number system?
from CONSTANTS.constants_html import HTML_LIST_youtube as html_list

# MAKE 50% CLOSING TAGS -- DEFAULT TRUE
add_closing_tags = True

outfile = sys.stdout
if len(sys.argv) > 4:
    output_file = open(sys.argv[4], "w")

min_space = int(sys.argv[2])
if min_space < 1:
    print("[WARN]  MIN_SPACE cannot be < 1, setting to 1...")
    min_space == 0
max_space = int(sys.argv[3])
if max_space <= min_space:
    print("[ERROR]  MIN SPACE cannot be greater than or equal to MAX SPACE")
    sys.exit(-1)

infile = open(sys.argv[1], "r")
text = infile.read()
infile.close()

words = text.split(" ")

final_words = []

count = 1
current_split = random.randrange(min_space, max_space)

for word in words:
    if count == current_split:
        tag = html_list[random.randrange(0, len(html_list))]
        if add_closing_tags:
            if random.randrange(0, 2) == 1:
                tag = tag[0] + "/" + tag[1:]
        final_words.append(tag)
        count = 0
        current_split = random.randrange(min_space, max_space)
    final_words.append(word)
    count += 1

outfile.write(" ".join(final_words) + "\n")

if outfile is not sys.stdout:
    outfile.close()


