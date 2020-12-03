days = ("Mon", "Tue", "Wed", "Thu", "Fri")

# x 는 변수이름. days는 sequence type
# x는 작업되는 배열의 item을 가리킨다. 

for x in days:
    if x is "Wed":
        break
    else:
        print(x)

for day in [1, 2, 3, 4, 5]:
    print(day)