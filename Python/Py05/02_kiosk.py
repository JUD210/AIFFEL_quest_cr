####### MEMO #######

# Todo [OK] 비슷한 출력 반복하는 부분들 모듈화하기

# Review [OK] 문제로 주어진 조건 확인해보기
# [OK] 평가 1. Kiosk 클래스를 생성하고, 주문, 추가 주문 메서드를 적절하게 구현할 수 있다.
#  ㄴ 각각의 메서드가 에러 없이, 정상적으로 동작하였다.
# [OK] 평가 2. 지불, 주문표 작성 메서드를 적절하게 구현할 수 있다.
#  ㄴ 각각의 메서드가 에러 없이, 정상적으로 동작하였다.

# Debug [OK] 제출하기 전에 ipynb 돌려보기
# 주의점 1
#   .py와 다르게, .ipynb에서는 f" " 안에서 translate(" ", "")를 사용하면 에러가 발생한다.
# f" " 범위 내에서는 replace(' ', '')와 같이 "를 쓰지 않도록 주의하자.

from datetime import datetime


# 주문표 장식을 위한 데코레이터
def decorate_output(func):
    """출력 양식을 꾸며주는 데코레이터 함수"""

    def wrapper(*args):
        print(f"⟝{'-' * 40}⟞")
        for _ in range(3):
            print(f"|{' ' * 40}|")
        result = func(*args)
        for _ in range(3):
            print(f"|{' ' * 40}|")
        print(f"⟝{'-' * 40}⟞")
        return result

    return wrapper


class Kiosk:
    def __init__(self):
        """Kiosk 클래스 초기화 메서드"""
        self.menu = [
            ["americano", 2000],
            ["latte", 3000],
            ["mocha", 3000],
            ["yuza_tea", 2500],
            ["green_tea", 2500],
            ["choco_latte", 3000],
        ]  # 메뉴와 가격을 다차원 리스트로 관리
        self.order_menu = []  # 주문 리스트 초기화
        self.order_price = []  # 가격 리스트 초기화
        self.price_sum = 0  # 합계 금액 초기화
        self.pay_type = ""  # 지불 방식 초기화

    def menu_print(self):
        """메뉴와 가격을 출력하는 메서드"""
        print("\n=== 📝 Cafe AIFFEL 메뉴판 ===")
        for i, item in enumerate(self.menu, start=1):
            print(f"  [{i}] {item[0].title().replace('_', ' ')} : {item[1]}원")
        print("==============================\n")

    def ask_temperature(self):
        """음료의 온도를 물어보고 반환하는 메서드"""
        while True:
            try:
                t = int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
                if t in [1, 2]:
                    return "HOT" if t == 1 else "ICE"
                else:
                    print("1과 2 중 하나를 입력하세요.\n")
            except ValueError:
                print("유효한 숫자를 입력해주세요.\n")

    def add_order(self, n, temp):
        """주문 리스트와 가격 리스트에 음료를 추가하는 메서드"""
        self.order_menu.append(f"{temp} {self.menu[n - 1][0]}")
        self.order_price.append(self.menu[n - 1][1])
        self.price_sum += self.menu[n - 1][1]

        print("--------------------------------------")
        print(f"주문 음료 | {temp} {self.menu[n - 1][0].title().replace('_', ' ')} : {self.menu[n - 1][1]}원")
        print("--------------------------------------\n")

    def take_order(self, n=0):
        """음료 주문을 받고 주문 리스트와 가격 리스트에 추가하는 메서드"""
        while n < 1 or len(self.menu) < n:
            try:
                n = int(input("주문할 음료의 번호를 입력하세요 : "))
                if n < 1 or len(self.menu) < n:
                    print("없는 메뉴입니다. 다시 주문해 주세요.\n")

            except ValueError:
                print("유효한 숫자를 입력해주세요.\n")
                continue

        # 메뉴판에 있는 음료 번호일 때
        if 1 <= n <= len(self.menu):
            temp = self.ask_temperature()
            self.add_order(n, temp)
        else:
            print("없는 메뉴입니다. 다시 주문해 주세요.\n")

    def display_order_summary(self, message):
        """현재까지의 주문 요약을 출력하는 메서드"""
        print(message)
        print("~~~ 주문할 음료 목록 ~~~")
        for i in range(len(self.order_menu)):
            print(f"{self.order_menu[i]} : {self.order_price[i]}원")
        print(f"합계 : {self.price_sum}원")
        print("===============================\n")

    def menu_select(self):
        """사용자로부터 메뉴 선택을 받아 주문 리스트를 업데이트하는 메서드"""
        self.take_order()  # 첫 주문 받기
        self.display_order_summary("주문이 완료되었습니다.\n")

        # 추가 주문 받기
        while True:
            try:
                n = int(input("추가 주문은 음료 번호를, 지불은 0을 누르세요 : "))
            except ValueError:
                print("유효한 숫자를 입력해주세요.\n")
                continue

            if n == 0:
                self.display_order_summary("주문이 완료되었습니다.\n")
                break
            elif 1 <= n <= len(self.menu):
                self.take_order(n)  # 추가 주문 받기
                self.display_order_summary("~~~ 현재까지 주문한 음료 목록 ~~~")
            else:
                print("없는 메뉴입니다. 다시 주문해 주세요.\n")

    # 지불 메서드
    def pay(self):
        """지불 방식을 입력받고 확인하는 메서드"""
        while True:
            self.pay_type = input("지불 방식을 입력하세요\n(현금: 'cash' or 1 | 카드: 'card' or 2) : ")

            if self.pay_type in ["1", "cash"]:
                self.pay_type = "현금"
                print("[안내문] 직원을 호출하겠습니다.\n")
                break

            elif self.pay_type in ["2", "card"]:
                self.pay_type = "카드"
                print("[안내문] IC칩 방향에 맞게 카드를 꽂아주세요.\n")
                break

            else:
                print("[안내문] 다시 결제를 시도해주세요.\n")

    # 주문표 메서드
    @decorate_output
    def table(self):
        """최종 주문표를 출력하는 메서드"""
        order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 주문 상품명 : 해당 금액
        print("| 주문해주셔서 감사합니다! 😊")
        print(f"|")
        for i in range(len(self.order_menu)):
            print(f"| {self.order_menu[i]} : {self.order_price[i]}원")
        print(f"|")

        # 합계 금액 출력
        print(f"| 합계 금액 : {sum(self.order_price)}원")
        print(f"|")

        # 지불 방식 출력
        print(f"| 지불 방식 : {self.pay_type}")
        print(f"|")

        # 주문 일시 출력
        print(f"| 주문 일시 : {order_time}")
        print(f"|")


# 객체 생성 및 함수 호출
kiosk_001 = Kiosk()  # 객체 생성
kiosk_001.menu_print()  # 메뉴 출력
kiosk_001.menu_select()  # 주문
kiosk_001.pay()  # 지불
kiosk_001.table()  # 주문표 출력


"""샘플로 제시되었던 코드의 전체적인 문제점 정리

1. 비트 연산자 '&'를 사용함

Before: # 비트 연산자를 사용하면 안됨
    if 1 <= n & n <= len(menu):
After:
    if 1 <= n and n <= len(menu):

2. menu는 인스턴스 변수이므로 self.menu로 사용해야 함

Before:
    len(menu)
After:
    len(self.menu)

3. self.price_sum을 초기화하지 않음
Before:
    def __init__(self):
        self.menu = ["americano", "latte", "mocha", "yuza_tea", "green_tea", "choco_latte"]  # 메뉴
        self.price = [2000, 3000, 3000, 2500, 2500, 3000]  # 가격

After:
    def __init__(self):
        self.menu = ["americano", "latte", "mocha", "yuza_tea", "green_tea", "choco_latte"]  # 메뉴
        self.price = [2000, 3000, 3000, 2500, 2500, 3000]  # 가격
        self.price_sum = 0  # 합계 금액

"""
