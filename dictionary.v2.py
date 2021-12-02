message='It is a cold day of december, and the clock is striking thirteen'

count={}

for c in message.upper():
    count.setdefault(c,0)
    count[c] = count[c]+1

print(count)