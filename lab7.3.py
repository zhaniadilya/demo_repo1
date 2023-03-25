n = int(input("Nomerler sany: "))
book = {}
for i in range(n):
    phone, name = input().split()
    book[name] = phone
izdeu = input("Name: ")
if izdeu in book:
    print(book[izdeu])
else:
    print("Telephon kitapshasynda zhoq!")