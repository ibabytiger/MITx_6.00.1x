s = 'azcbobobegghakl'
counter = 0

for n in range(0, len(s)):
    if s[n] == 'b':
        if s[n:n + 3] == 'bob':
            counter += 1
print "Number of times bob occurs is: " + str(counter)
