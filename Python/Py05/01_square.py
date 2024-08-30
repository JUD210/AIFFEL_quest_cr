# @@Review [OK] 문제로 주어진 조건 확인해보기
#
# [OK] 평가 기준: 평행사변형, 사다리꼴 넓이를 구하는 메서드를 직접 작성할 수 있다.
#  ㄴ self 인자를 잊지 않고 넣고, 변수를 알맞게 사용했다.


class Square:
    def __init__(self):
        self.square = int(
            input("넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n 1.직사각형 2.평행사변형 3.사다리꼴 \n >>>")
        )

        if self.square == 1:
            print("직사각형 함수는 rect()입니다.")

        elif self.square == 2:
            print("평행사변형 함수는 par()입니다.")

        elif self.square == 3:
            print("사다리꼴 함수는 trape()입니다.")

        else:
            print("1, 2, 3 중에서 다시 입력해주세요")

    def rect(self):
        width, vertical = map(int, input("가로, 세로를 입력하세요. 예시 : 가로,세로\n >>>").split(","))
        area = width * vertical
        result = "직사각형의 넓이는 : " + str(area)
        return result

    def par(self):
        bottom, height = map(int, input("밑변과 높이를 입력하세요. 예시 : 밑변,높이\n >>>").split(","))
        area = bottom * height
        result = "평행사변형의 넓이는 : " + str(area)
        return result

    def trape(self):
        bottom, top, height = map(int, input("밑변, 윗변, 높이를 입력하세요. 예시 : 밑변,윗변,높이\n >>>").split(","))
        area = (bottom + top) * height * 0.5
        result = "사다리꼴의 넓이는 : " + str(area)
        return result


# 객체 생성 및 테스트
a = Square()

# 직사각형은 rect()를 호출
if a.square == 1:
    print(a.rect())

# 평행사변형은 par()를 호출
elif a.square == 2:
    print(a.par())

# 사다리꼴은 trape()를 호출
elif a.square == 3:
    print(a.trape())
