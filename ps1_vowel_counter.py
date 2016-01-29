s = "azcbobobegghakl"
count = 0
for letter in s:
    if letter.lower() in ("a", "e", "i", "o", "u"):
        count += 1
print "Number of vowels: " + str(count)
