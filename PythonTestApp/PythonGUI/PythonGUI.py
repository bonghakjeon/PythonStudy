# 파이썬 인터프리터 버전 3.7 설치 및 비쥬얼스튜디오 연동 방법 
# 참고 URL - https://wendys.tistory.com/148
# 참고 2 URL - https://www.python.org/downloads/
# 참고 3 URL - https://learn.microsoft.com/ko-kr/visualstudio/python/installing-python-interpreters?view=vs-2022

# 파이썬 화면 구현 패키지 tkinter 사용 방법 
# 참고 URL - https://imspear.tistory.com/25

# 파이썬 정적 타입 오류 검사 도구 Mypy 설치 방법 및 설명 
# 참고 URL - https://www.daleseo.com/python-mypy/
# 참고 2 URL - https://dailyheumsi.tistory.com/222

# 파이썬 일반 코드 타입 오류 검사 도구 pylint 설치 방법 및 설명 
# 참고 URL - https://zoosso.tistory.com/635
# 참고 2 URL - https://dailyheumsi.tistory.com/222

# IronPython 호환하기 위해 파이썬 2.7 버전 설치 
# 참고 URL - https://ossian.tistory.com/23

# 파이썬 2.7 버전에서 Tkinter 패키지 사용하기 
# 참고 URL - https://stackoverflow.com/questions/18729147/python-2-7-no-module-named-tkinter
import Tkinter 
#import tkMessageBox

# 파이썬 tkinter 패키지 설치 (설치 명령어 - pip install tk)
# 참고 URL - https://ngio.co.kr/11034

# 파이썬 3.7 버전 tkinter import 및 GUI 화면 구현 
# 참고 URL - https://www.c-sharpcorner.com/article/how-to-create-gui-in-python/
# from tkinter import*

# 파이썬 main 메서드 구현 
# 참고 URL - https://www.entity.co.kr/entry/51-Python-Main-%ED%95%A8%EC%88%98-%EB%B0%8F-%EB%A9%94%EC%86%8C%EB%93%9C-def-Main%EC%9D%98-%EC%9D%B4%ED%95%B4
# 참고 2 URL - https://gdbs.tistory.com/113
def main():
    # obj=Tk()
    obj = Tkinter.Tk()  
    obj.title("RevitBox Test")   # set title of our window form  - 해당 윈도우 폼의 제목 설정
    obj.geometry("300x300")      # set dimension of form - 해당 윈도우 폼 양식의 크기 설정
    # 파이썬 2.7 버전 패키지 "Text" 설치
    # 참고 URL - https://lcj8390.tistory.com/86
    #wintext = Text(obj)  
    #wintext.insert(INSERT, "Hello.....")  
    #wintext.insert(END, "Welcome to RevitBox.....")  
    #wintext.pack()  
    obj.mainloop()  

if __name__ == '__main__':
    main()

