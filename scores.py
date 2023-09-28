from cs50 import get_int
scores = [72,73,33]
average = sum(scores)/len(scores)
print(f"average: {average}")
##
points =[]
y = get_int("subjects: ")
for i in range(y):
    point = get_int("point: ")
    points.append(point)

average = sum(points)/len(points)
print(f"average: {average}")
