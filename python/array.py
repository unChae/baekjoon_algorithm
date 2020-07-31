# coding=utf-8 
data = "Hello World"

print(data)
print('---- Result ---')
#0은 생략가능 x~y까지
print(data[0:4])
print(data[:5])
print(data[6:])
#마지막 index
print(data[-1])
#마지막 index 빼고
print(data[:-1])
#뒤집어서 출력
print(data[::-1])

print(data[3:0:-1])
print(data[3::-1])