n = input()
list1 = list(map(int, input().split()))
x = 1
first = max(list1)
list1.remove(max(list1))
second = max(list1)
print(first * second)
