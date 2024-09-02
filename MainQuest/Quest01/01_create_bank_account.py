""" [메인 퀘스트 1번: 은행계좌 만들기 | 3점]

@@Review Q1 [x] : Account 클래스
- 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다.
- Account 클래스를 생성한 후 생성자(hint: 매직매서드..!!)를 구현해보세요.
- 생성자에서는 예금주와 초기 잔액만 입력 받습니다.
- 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
(은행이름: SC은행, 계좌번호: 111-11-111111)

@@Review Q2 [x] : 클래스 변수
- 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.

@@Review Q3 [x] : 클래스 변수 출력
- Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.
ㄴ 클래스 변수를 참조하므로, 클래스 메서드로 구현해보았음.
ㄴ 'get' prefix가 붙은 메서드는 보통 값을 return하는 것이 일반적인 관례이나, 출력을 하라고 하여 print문도 사용했음.
ㄴ get_account_count 가 더 낫지 않을까...? get_account_num은 계좌번호를 반환하는 것으로 오해할 수 있는데... 그래도 일단 지시받은대로 해야겠다.

@@Review Q4 [x] : 입금 메서드
- Account 클래스에 입금을 위한 deposit 메서드를 추가하세요.
- 입금은 최소 1원 이상만 가능합니다.

@@Review Q5 [x] : 출금 메서드
- Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요.
- 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.

@@Review Q6 [x] : 정보 출력 메서드
- Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요.
- 잔고는 세자리마다 쉼표를 출력하세요.
- (은행이름: SC은행, 예금주: 파이썬, 계좌번호: 111-11-111111, 잔고: 10,000원)

@@Review Q7 [x] : 이자 지급하기
- 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.

@@Review Q8 [x] : 여러 객체 생성
- Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.

@@Review Q9 [x] : 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.
- 객체 순회 반복문을 통해서 순회하세요.

@@Review Q10 [x] : 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요.
- 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.
ㄴ 'show' 또는 'print'와 같은 prefix가 있었으면 좀 더 좋았을 듯. 제시받은 메서드명은 변수명으로 딱인데... 쩝

채점 기준 (총 3점)
@@Review [x] Account 클래스로부터 생성된 계좌의 개수 출력, 잔고 100만원 이상 고객 정보만 출력 | 1점
@@Review [x] 입금 메서드, 출금 메서드, 이자 지급 기능 완성 | 1점
@@Review [x] 입금과 출금 내역 출력에 성공 | 1점

"""

import random


def decorate_with_title(title):
    """
    데코레이터 함수로, 출력 문구에 제목을 추가하여 가독성을 향상시킵니다.

    Args:
        title (str): 출력될 제목.
    """

    def decorator(func):
        def wrapped_func(self, *args, **kwargs):
            print(f"\n-------- {title} -------- ")
            func(self, *args, **kwargs)
            print("=" * (len(title) + 22), "\n")

        return wrapped_func

    return decorator


class Account:
    """
    은행 계좌를 나타내는 클래스입니다. 예금주, 계좌번호, 잔고 등의 정보를 저장하고, 입출금 등의 기능을 제공합니다.

    클래스 변수:
        account_count (int): 생성된 계좌 객체의 수를 저장합니다.

    인스턴스 변수:
        bank (str): 은행 이름 (기본값: "SC은행").
        user_name (str): 예금주 이름.
        balance (int): 계좌 잔고.
        account_num (str): 계좌 번호 (3자리-2자리-6자리 형식).
        deposit_records (list): 입금 내역을 저장하는 리스트.
        withdraw_records (list): 출금 내역을 저장하는 리스트.
    """

    account_count = 0

    @classmethod
    def get_account_num(cls):
        """
        생성된 계좌 객체의 총 개수를 반환합니다.

        Returns:
            int: 생성된 계좌의 수.
        """
        print(f"총 계좌 개수: {cls.account_count}")
        return cls.account_count

    def __init__(self, user_name, balance):
        """
        Account 객체의 초기화를 담당하는 생성자입니다.

        Args:
            user_name (str): 예금주 이름.
            balance (int or float): 초기 잔고. 0 이상이어야 합니다.

        Raises:
            ValueError: 초기 잔고가 0보다 작거나, 유효하지 않은 예금주 이름이 입력된 경우 발생합니다.
            TypeError: 잔고가 숫자가 아닌 경우 발생합니다.
        """
        try:
            if not isinstance(balance, (int, float)):
                raise TypeError("잔고는 숫자여야 합니다.")
            if balance < 0:
                raise ValueError("초기 잔고는 0 이상이어야 합니다.")
            if not user_name or not isinstance(user_name, str):
                raise ValueError("유효한 예금주 이름을 입력하세요.")
            if len(user_name) > 100:
                raise ValueError("예금주 이름은 100자 이하이어야 합니다.")

            self.bank = "SC은행"
            self.user_name = user_name
            self.balance = balance
            self.account_num = f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(100000, 999999)}"
            self.deposit_records = []
            self.withdraw_records = []

            Account.account_count += 1

        except (TypeError, ValueError) as e:
            print(f"계좌 생성 에러: {e}. 객체가 생성되지 않았습니다.")
            # 객체 생성 중단 후, raise 하여 다음 코드가 실행되지 않도록 함
            raise

    def deposit(self, amount):
        """
        계좌에 입금합니다. 입금 횟수가 5회가 될 때마다 잔고의 1%를 이자로 지급합니다.

        Args:
            amount (int or float): 입금할 금액. 최소 1원 이상이어야 합니다.

        Raises:
            TypeError: 입금 금액이 숫자가 아닌 경우 발생합니다.
            ValueError: 입금 금액이 1원 미만인 경우 발생합니다.
        """
        try:
            if not isinstance(amount, (int, float)):
                raise TypeError("입금 금액은 숫자여야 합니다.")
            if amount < 1:
                raise ValueError("입금은 최소 1원 이상 가능합니다.")
            self.balance += amount
            self.deposit_records.append(amount)
            interest = 0
            if len(self.deposit_records) > 0 and len(self.deposit_records) % 5 == 0:
                interest = self.balance * 0.01  # 잔고의 1% 계산
                self.balance += interest  # 이자 지급
                print(f"[알림] {self.user_name}님에게 이자가 {format(int(interest), ',')}원 지급되었습니다.")
            if interest > 0:
                self.deposit_records.append(interest)
        except (TypeError, ValueError) as e:
            print(f"입금 에러: {e}")

    def withdraw(self, amount):
        """
        계좌에서 출금합니다. 잔고 이상으로는 출금할 수 없습니다.

        Args:
            amount (int or float): 출금할 금액.

        Raises:
            TypeError: 출금 금액이 숫자가 아닌 경우 발생합니다.
            ValueError: 출금 금액이 잔고를 초과한 경우 발생합니다.
        """
        try:
            if not isinstance(amount, (int, float)):
                raise TypeError("출금 금액은 숫자여야 합니다.")
            if self.balance < amount:
                raise ValueError("계좌 잔고 이상으로는 출금할 수 없습니다.")
            if amount < 1:
                raise ValueError("출금은 최소 1원 이상 가능합니다.")
            self.balance -= amount
            self.withdraw_records.append(amount)
        except (TypeError, ValueError) as e:
            print(f"출금 에러: {e}")

    @decorate_with_title(title="계좌 정보")
    def display_info(self):
        """
        계좌 정보를 출력합니다. 은행 이름, 예금주, 계좌 번호, 잔고를 포함합니다.
        잔고는 세 자리마다 쉼표를 사용하여 출력됩니다.
        """
        print(
            f"은행이름: {self.bank}\n"
            f"예금주: {self.user_name}\n"
            f"계좌번호: {self.account_num}\n"
            f"잔고: {format(int(self.balance), ',')}원"
        )

    @decorate_with_title(title="입금 내역")
    def deposit_history(self):
        """
        계좌의 입금 내역을 출력합니다.
        """
        if self.deposit_records:
            for i, record in enumerate(self.deposit_records):
                print(f"[입금 {i + 1}] +{format(int(record), ',')}원")
        else:
            print("입금 내역이 없습니다.")

    @decorate_with_title(title="출금 내역")
    def withdraw_history(self):
        """
        계좌의 출금 내역을 출력합니다.
        """
        if self.withdraw_records:
            for i, record in enumerate(self.withdraw_records):
                print(f"[출금 {i + 1}] -{format(int(record), ',')}원")
        else:
            print("출금 내역이 없습니다.")


#####################################################
# 조건 테스트 구간
#####################################################

accounts = []


def create_account(user_name, balance):
    """
    새로운 계좌를 생성하고, 생성된 계좌를 accounts 리스트에 추가합니다.

    Args:
        user_name (str): 예금주 이름.
        balance (int or float): 초기 잔고. 0 이상이어야 합니다.

    Raises:
        ValueError: 초기 잔고가 0보다 작거나, 유효하지 않은 예금주 이름이 입력된 경우 발생합니다.
        TypeError: 잔고가 숫자가 아닌 경우 발생합니다.

    예외 처리:
        - 계좌 생성 시 오류가 발생하면, 오류 메시지를 출력하고 계좌가 생성되지 않았다는 메시지를 출력합니다.
        - 예외가 발생해도 프로그램이 중단되지 않으며, 다음 코드를 계속 실행할 수 있습니다.
    """
    try:
        account = Account(user_name, balance)

        # 하단은 else 구문으로 뺄 수 있지만, 언어 호환성을 위해 생략
        accounts.append(account)

    except (ValueError, TypeError) as e:
        print(f"계좌 생성에 실패했습니다.")


### 계좌 생성 테스트
create_account("민혁", 123000000)
create_account("와이프", 123000000)
create_account("큰아들", 1000000)
create_account("작은딸", 999999)
create_account("파이썬", 10000)

### 잘못된 초기화 시도 테스트 (에러 발생, 객체 생성되지 않음)
create_account("⚠️ Missing No1 ？", -9)  # 초기 잔고 음수
# 계좌 생성 에러: 초기 잔고는 0 이상이어야 합니다.. 객체가 생성되지 않았습니다.
# 계좌 생성에 실패했습니다: 초기 잔고는 0 이상이어야 합니다.

create_account(-3.14, "Misssssssssss")  # 잘못된 잔고 타입
# 계좌 생성 에러: 잔고는 숫자여야 합니다.. 객체가 생성되지 않았습니다.
# 계좌 생성에 실패했습니다: 잔고는 숫자여야 합니다

Account.get_account_num()  # 총 계좌 개수: 5

### 입출금 테스트
for _ in range(5):
    accounts[1].deposit(1000000)
    accounts[1].withdraw(1000000)
    accounts[2].deposit(1000000)
    accounts[2].withdraw(1000000)
# [알림] 와이프님에게 이자가 1,240,000원 지급되었습니다.
# [알림] 큰아들님에게 이자가 20,000원 지급되었습니다.


### 잔액 100만원 이상 계좌의 정보, 입출금 내역 조회
for account in accounts:
    if account.balance >= 1000000:
        print("\n~~~~~~~~ 잔액 100만원 이상의 계좌가 조회되었습니다. ~~~~~~~~")
        account.display_info()
        account.deposit_history()
        account.withdraw_history()
        print("$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

### 예외처리 테스트: 입금, 출금
accounts[4].deposit(-1)  # 입금 에러: 입금은 최소 1원 이상 가능합니다.
accounts[4].deposit("test")  # 입금 에러: 입금 금액은 숫자여야 합니다.
accounts[4].withdraw(-1)  # 출금 에러: 출금은 최소 1원 이상 가능합니다.
accounts[4].withdraw("test")  # 출금 에러: 출금 금액은 숫자여야 합니다.
accounts[4].withdraw(1000000)  # 출금 에러: 계좌 잔고 이상으로는 출금할 수 없습니다.
