# 파이썬 인터프리터 버전 3.7 설치 및 비쥬얼스튜디오 연동 방법 
# 참고 URL - https://wendys.tistory.com/148
# 참고 2 URL - https://www.python.org/downloads/
# 참고 3 URL - https://learn.microsoft.com/ko-kr/visualstudio/python/installing-python-interpreters?view=vs-2022

# 파이썬 화면 구현 패키지 tkinter 사용 방법 
# 참고 URL - https://imspear.tistory.com/25

import sys
from math import cos, radians
# print("Hello, Visual Studio")

#for i in range(360):
#	print(cos(radians(i)))

# Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    rad = radians(x)                          # cos works with radians
    numspaces = int(20 * cos(rad) + 20)       # scale to 0-40 spaces
    st = ' ' * numspaces + 'o'                # place 'o' after the spaces
    return st

# 파이썬 main 메서드 구현 
# 참고 URL - https://www.entity.co.kr/entry/51-Python-Main-%ED%95%A8%EC%88%98-%EB%B0%8F-%EB%A9%94%EC%86%8C%EB%93%9C-def-Main%EC%9D%98-%EC%9D%B4%ED%95%B4
# 참고 2 URL - https://gdbs.tistory.com/113
def main():
    for i in range(0, 1800, 12):
        s = make_dot_string(i)
        print(s)

if __name__ == "__main__":
    main()

#def make_dot_string(x):
#    return ' ' * int(20 * cos(radians(x)) + 20) + 'o'

#for i in range(0, 1800, 12):
#    s = make_dot_string(i)
#    print(s)
