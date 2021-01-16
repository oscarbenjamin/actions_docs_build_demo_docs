"""
Script to test the behaviour of a post-push action.
"""
with open('index.html') as infile:
    lines = infile.readlines()

n = lines.index('<!DOCTYPE html>\n')

lines.insert(n + 1, '<!--Added by post-push script to see that it works-->\n')

with open('index.html', 'w') as outfile:
    for line in lines:
        outfile.write(line)
