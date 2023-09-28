def main():
    height = get_height()
    for i in range(height):
        print("#")
def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n>0:
                return n
        except ValueError:
            print("not an integer")
main()












while True:
    x = int(input("x: "))
    j = int(input("j: "))
    if x >0 and j>0:
        break
    elif x<0 and j<0:
        x = int(input("x: "))
        j = int(input("j: "))
for i in range(x):
    for i in range(j):
        print("%", end="")
    print()