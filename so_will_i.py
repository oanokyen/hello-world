
# Just respond with directory for .txt file

name = input('Enter file:')
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = {}
for word in words: 
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount == None or count > bigcount:
        bigword = word 
        bigcount = count 
print (bigword, bigcount)
