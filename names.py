import sys
names=["mary", "wairimu", "wanyoike", "hope", "jire", "wambui"]
name = input("Name: ")
for n in names:
    if name == n:
        print("found")
        sys.exit(0)
        
print("Not found")
sys.exit(1)