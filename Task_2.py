n = int(input())
result = 0
while n > 0:
    result += n % 10
    n //= 10
print(result)

print()



# Решение без цикла, если это подразумевалось: 


# z = 123
# res = 0
# s = z%10
# res = res+s
# z=z//10
# s = z%10
# res = res+s
# z=z//10
# s = z%10
# res = res+s
# print(res)
