from urllib.request import urlopen

response = urlopen("https://eggman.tv/files/w.txt")
words = []

for line in response.readlines():
    data = line.split()
    for word in data:
        word = word.decode('utf-8').lower()
        words.append(word)

print(words)
