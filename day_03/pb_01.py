import re

arr = ""

for i in range(6):
    s = input()
    arr += s
    
matches = re.findall(r"mul\((\d+),(\d+)\)", arr)

ans = 0
for match in matches:
    ans += int(match[0]) * int(match[1])

print(ans)