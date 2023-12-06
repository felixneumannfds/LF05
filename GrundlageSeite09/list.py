
def sep():
    print('#########################################')


sep()
list = ["Rammstein", "Alice Cooper", "Metallica", "Finntroll", "Nightwish"]
index = 0
while index < 5:
    print(list[0+index])
    index += 1

sep()
# c
print(len(list))
sep()
# d
index = 1
while index < 5:
    print(list[0+index])
    index += 2
sep()
# e
index = 4
while index >= 0:
    print(list[0+index])
    index -= 1
sep()

# f)

list.pop(2)
list.append("ACDC")
print(list)

sep()
# g
sorted_list = sorted(list)
print(sorted_list)

sep()
