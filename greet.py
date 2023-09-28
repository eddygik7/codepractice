from sys import argv
if len(argv) ==2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")
print("#######")
    ##or
for i in range(len(argv)):
    print(argv[i])
print("#######")
##or
for arg in argv[1:]:
    print(arg)
print("#######")