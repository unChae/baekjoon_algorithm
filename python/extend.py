x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']

#해당 value와 겹치는 index 갯 수
z = x.count('Tick')
print(z)

#가장 앞에 있는 index 위치
z = x.index('Song')
print(z)

#sort 정렬
x.sort()
print(x)

#list 역순 정렬
x.reverse()
print(x)

#있는 그대로 뒤에 추가
x.append(y)
print('append:', x)
#['Tick', 'Tock', 'Song', ['Ping', 'Pong']]

#내부 원소들을 뒤에 추가
x.extend(y)
print('extend:', x)
#['Tick', 'Tock', 'Song', 'Ping', 'Pong']

i = ['Tick', 'Tock', 'Song']
j = 'Ping'

#글자 덩어리 자체를 추가
i.append(j)
print(i)

#원하는 위치에 추가
i.insert(1,j)
print(i)

#문자 하나 하나를 나눠서 리스트에 추가
i.extend(j)
print(i)