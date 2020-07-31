#sys가 있고 없고의 차이는 마지막 한 줄의 띄어지냐 마냐
#sys가 input보다 여러개 입력 처리를 할 때 처리 속도가 빠르다고 한다.
import sys

x = input()
y = sys.stdin.readline()
print(x, y)