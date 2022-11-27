import re

text = input()
sentences = re.findall(r"[\w\s,]*[\.\!\?]", text)
counter = 0
for sentence in sentences:
    sentence = re.sub(r"\W", " ", sentence)
    sentence = re.sub(r"\s+", " ", sentence)
    words = re.split(r"\s", sentence)
    words = [w for w in words if w != ""]
    for i, word in enumerate(words):
        if word != "" and i != 0:
            if re.search(r"[A-Z]+", word):
                print("%d:%s" % (counter+i+1, word))
    counter += len(words)
