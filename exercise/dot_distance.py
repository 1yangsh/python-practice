# 1. 다음 입사문제
# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# (단 점들의 배열은 모두 정렬되어있다고 가정한다.)
# 예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.

s = [1, 3, 4, 8, 13, 17, 20]


def short_list(s):
    myList = []
    myList2 = []
    dis = 0
    myList.append(s[1] - s[0])
    for i in range(len(s) - 1):
        dis = s[i + 1] - s[i]
        if dis < myList[-1]:
            myList.append(dis)
            myList2.append((s[i], s[i + 1]))

    print(myList2[-1])


short_list(s)
