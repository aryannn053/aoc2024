import re

arr = ""

for i in range(6):
    s = input()
    arr += s
    
matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", arr)

flag = True

ans = 0
for match in matches:
    if match[2] == "" and flag:
        ans += int(match[0]) * int(match[1])
    else:
        if match[2] == "do()":
            flag = True
        else:
            flag = False

print(ans)