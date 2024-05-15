import sys
import random
if len(sys.argv) < 2:
    print("""
[USAGE]  python3 scramble_byLine.py <INPUT_FILE> <OUTPUT_FILE>
    INPUT_FILE  :   A text file. All individual 'lines' must be period '.' delimited.
    OUTPUT_FILE :   Optional. Name of output file. Defaults to stdout.
""")
    sys.exit(0)
outfile = sys.stdout
if len(sys.argv) > 2:
    output_file = open(sys.argv[2], "w")
infile = open(sys.argv[1], "r")
text = infile.read()
infile.close()
lines = text.split(".")
final_lines = []
for l in lines:
    new_line = l.strip()
    if len(new_line) > 1:
        final_lines.append(new_line)
shuffled_lines = [""] * len(final_lines)
for i in range(len(final_lines)):
    shuffled_lines[i-1] = final_lines.pop(random.randrange(0, len(final_lines)))
for l in shuffled_lines:
    outfile.write(l + "." + " " * random.randrange(1, 4) + "   " * random.randrange(0, 2))
outfile.write("\n")
if outfile is not sys.stdout:
    outfile.close()


