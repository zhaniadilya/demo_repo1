comments = {}
while True:
    text = input()
    if not text:
        break
    name, comment = text.split(": ")
    comments[name] = None

print(len(comments))
