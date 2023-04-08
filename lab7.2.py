comments = {}
while True:
    text = input()
    if not text:
        break
    name, comment = text.split(": ")

    comments[name] = list(comments.values())

print(comments)
print("Comments number: ", len(comments))
