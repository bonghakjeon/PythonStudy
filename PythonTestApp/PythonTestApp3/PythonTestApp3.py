# 파이썬 인터프리터 버전 3.7 설치 및 비쥬얼스튜디오 연동 방법 
# 참고 URL - https://wendys.tistory.com/148
# 참고 2 URL - https://www.python.org/downloads/
# 참고 3 URL - https://learn.microsoft.com/ko-kr/visualstudio/python/installing-python-interpreters?view=vs-2022

# 파이썬 정적 타입 오류 검사 도구 Mypy 설치 방법 및 설명 
# 참고 URL - https://www.daleseo.com/python-mypy/
# 참고 2 URL - https://dailyheumsi.tistory.com/222

# 파이썬 일반 코드 타입 오류 검사 도구 pylint 설치 방법 및 설명 
# 참고 URL - https://zoosso.tistory.com/635
# 참고 2 URL - https://dailyheumsi.tistory.com/222

# 파이썬 화면 구현 패키지 tkinter 사용 방법 
# 참고 URL - https://imspear.tistory.com/25

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for c,z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]):
    xs = np.arange(20)
    ys = np.random.rand(20)

    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

