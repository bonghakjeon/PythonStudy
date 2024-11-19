def main():
    # 원소의 갯수(n) 입력
    n = int(input())
    # 전체 원소 리스트(datas)로 입력 받기 
    datas = list(map(int, input().split()))
    # 찾고자 하는 값 value 입력 받기 
    value = int(input())
    # 이진 탐색 수행 (함수 binarySearch 호출)
    result = binarySearch(datas, value, 0, n-1)
    # 이진 탐색 수행 결과 출력
    # 값을 찾지 못한 경우 -1 출력 
    if result == None:
        print(-1)
    # 값을 찾은 경우 인덱스 + 1 출력
    else:
        print(result+1)

# 파이썬 이진 탐색 트리 구현 
# 유튜브 참고 URL - https://youtu.be/-Gx0T92-7h8?si=ZI1ipSapQSIy3Arx
def binarySearch(pDatas, pValue, pStart, pEnd):
    # 값을 찾지 못한 경우 None 반환
    if pStart > pEnd:
        return None
    mid = (pStart + pEnd) // 2 
    # 찾은 경우 중간점 인덱스 mid 반환 
    if pDatas[mid] == pValue:
        # 반복문 사용해서 찾은 값이 존재하는 가장 처음 위치 찾기
            for i in range(len(pDatas)):
                # i 인덱스가 mid 보다 작은 가장 처음 위치인 경우
                if pDatas[i] == pDatas[mid] and i < mid:
                    return i      # 인덱스 i 반환
                # mid 인덱스가 가장 처음 위치인 경우  
                elif pDatas[i] == pDatas[mid] and i >= mid:
                    return mid    # 중간점 인덱스 mid 반환
                
    # 중간점의 값(pDatas[mid])보다 찾고자 하는 값이 작은 경우 왼쪽 확인 
    elif pDatas[mid] > pValue:
        return binarySearch(pDatas, pValue, pStart, mid-1)
    # 중간점의 값(pDatas[mid])보다 찾고자 하는 값이 큰 경우 오른쪽 확인 
    else:
        return binarySearch(pDatas, pValue, mid+1, pEnd)

if __name__ == "__main__":
    main()
