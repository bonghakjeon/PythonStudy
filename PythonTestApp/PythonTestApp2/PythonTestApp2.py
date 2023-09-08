# 파이썬 인터프리터 버전 3.7 설치 및 비쥬얼스튜디오 연동 방법 
# 참고 URL - https://wendys.tistory.com/148
# 참고 2 URL - https://www.python.org/downloads/
# 참고 3 URL - https://learn.microsoft.com/ko-kr/visualstudio/python/installing-python-interpreters?view=vs-2022

from math import radians
import numpy as np # installed with matplotlib 
import matplotlib.pyplot as plt

# 파이썬 화면 구현 패키지 tkinter 사용 방법 
# 참고 URL - https://imspear.tistory.com/25

# 파이썬 main 메서드 구현 
# 참고 URL - https://www.entity.co.kr/entry/51-Python-Main-%ED%95%A8%EC%88%98-%EB%B0%8F-%EB%A9%94%EC%86%8C%EB%93%9C-def-Main%EC%9D%98-%EC%9D%B4%ED%95%B4
# 참고 2 URL - https://gdbs.tistory.com/113
def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

if __name__ == "__main__":
    main()
    

