# Сумма цифр
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = int (input ("Введите трехзначное число: "))
b = int (a / 10 % 10)
c = int (a / 100 )
a = a % 10
sum = a+b+c
print(sum )