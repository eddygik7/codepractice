s = input("do yoou agree? ")
s = s.lower()
if s in["y", "yes"]:
    print("Agreed,")
elif s in["n", "no"]:
    print("Not agreed,")