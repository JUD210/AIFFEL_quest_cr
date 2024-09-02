""" [메인 퀘스트 2번: 간단한 자동사냥 RPG 만들기 | 2점]

간단한 자동사냥 RPG 게임을 만들어봅시다! 사용자의 이름을 입력 받아 플레이어를 생성하고, 몬스터들을 차례로 자동사냥하는 게임을 만들어보고자 합니다.

@@Review Q1 [x] : Character 클래스 만들기
- 이름, 레벨, 체력, 공격력, 방어력의 속성을 가짐
- 인스턴스의 현재 체력이 0 이상인지 bool 값을 반환하는 is_alive 메서드 만들기
- 공격을 받았을 때, (받은 데미지 - 본인의 방어력)만큼 현재 체력이 감소하는 take_damage 메서드 만들기
    - 본인의 방어력이 데미지보다 크다면 체력 감소하지 않음
- 타겟에게 데미지를 입히는 attack_target 메서드 만들기
    - 데미지는 1부터 공격력 사이의 랜덤한 정수

@@Review Q2 [x] : Player 클래스와 Monster 클래스 만들기
Character 클래스를 상속 받는 Player와 Monster 클래스를 만들기
● Player 클래스
    - Character를 상속 받기
    - 레벨 1, 체력 100, 공격력 25, 방어력 5로 초기화하기
    - Player 클래스는 경험치 속성을 추가로 가짐
    - 인수로 받은 정수 만큼 경험치를 획득하는 gain_experience 메서드 만들기
    - 현재 경험치가 50이상이면 레벨을 1, 공격력을 10, 방어력을 5씩 올리는 level_up 메서드 만들기
● Monster 클래스
    - Character를 상속 받기
    - 몬스터의 레벨에 비례하는 체력, 공격력, 방어력 초기화하기
        - 체력: 10~30 사이의 랜덤한 정수 * 레벨
        - 공격력: 5~20 사이의 랜덤한 정수 * 레벨
        - 방어력: 1~5 사이의 랜덤한 정수 * 레벨

@@Review Q3 [x] : battle 함수 만들기
● battle 함수
    - Player 인스턴스와 Monster 인스턴스를 인수로 받아 둘 중 하나의 체력이 0 이하가 될 때까지 공격을 주고 받는 함수
    - 만약 Player 인스턴스가 살아남았다면
        - Player 인스턴스에 (몬스터 레벨 * 20)만큼의 경험치를 추가
        - player의 레벨업 메서드 호출
        - '전투 승리!'를 출력
    - Player 인스턴스가 살아남지 못했을 경우
        - '전투 패배..'를 출력하기

@@Review Q4 [x] : main 함수 만들기
● 몬스터의 이름, 레벨이 매핑된 딕셔너리 정의하기
    - monster_dict = {'슬라임': 1, '고블린': 2, '오크': 3}
● 사용자로부터 이름을 입력받아 Player 인스턴스 생성하기
● 몬스터 딕셔너리로부터 Monster 인스턴스 생성하기
● 생성된 Monster 인스턴스와 Player 인스턴스가 battle 함수를 통해 전투
    - player는 생성된 몬스터 3마리(슬라임, 고블린, 오크)와 모두 전투해야함
    - 전투 도중에 Player가 사망하면 이후 전투를 진행하지 않고 '게임오버' 출력하고 종료

채점 기준 | 2점
@@Review [x] : Player와 Monster 클래스를 완성 | 1점
@@Review [x] : battle 함수와 main 함수 완성 | 1점

"""

import random


class Character:
    """
    게임 캐릭터를 나타내는 기본 클래스.

    Attributes:
        name (str): 캐릭터의 이름.
        level (int): 캐릭터의 레벨.
        hp (int): 캐릭터의 체력.
        attack (int): 캐릭터의 공격력.
        defense (int): 캐릭터의 방어력.
        speed (int): 캐릭터의 스피드, 전투 순서에 영향을 줌.
    """

    def __init__(self, name, level, hp, attack, defense, speed):
        """
        Character 클래스의 초기화 메서드.

        Args:
            name (str): 캐릭터의 이름.
            level (int): 캐릭터의 레벨.
            hp (int): 캐릭터의 체력.
            attack (int): 캐릭터의 공격력.
            defense (int): 캐릭터의 방어력.
            speed (int): 캐릭터의 스피드.
        """
        self.name = name
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def is_alive(self):
        """
        캐릭터가 살아있는지 여부를 확인.

        Returns:
            bool: 체력이 0 이상이면 True, 그렇지 않으면 False.
        """
        return self.hp > 0

    def take_damage(self, damage):
        """
        캐릭터가 공격을 받았을 때 체력을 감소시킴.

        Args:
            damage (int): 받은 데미지 값.
        """
        damage_taken = max(0, damage - self.defense)
        self.hp -= damage_taken
        print(f"『{self.name}』이(가) {damage_taken}의 피해를 입었습니다. | 남은 체력: {self.hp}")

    def attack_target(self, target):
        """
        타겟에게 공격을 가함.

        Args:
            target (Character): 공격할 대상 캐릭터.
        """
        damage = random.randint(1, self.attack)
        print(f"【 🗡️ 】 『{self.name}』이(가) '{target.name}'에게 {damage} 만큼 공격했다!")
        target.take_damage(damage)


class Player(Character):
    """
    플레이어 캐릭터를 나타내는 클래스.

    Attributes:
        experience (int): 플레이어의 경험치.
    """

    def __init__(self, name):
        """
        Player 클래스의 초기화 메서드. 기본 속성을 설정함.

        Args:
            name (str): 플레이어의 이름.
        """
        super().__init__(name, level=1, hp=100, attack=25, defense=5, speed=15)
        self.experience = 0

    def gain_experience(self, amount):
        """
        플레이어가 경험치를 획득함.

        Args:
            amount (int): 획득할 경험치 양.
        """
        self.experience += amount
        print(f"[{self.name}]이(가) {amount}의 경험치를 획득했습니다. | 총 경험치: {self.experience}")

    def level_up(self):
        """
        플레이어의 경험치가 50 이상이면 레벨업을 수행함.
        레벨업 시 공격력, 방어력, 스피드가 증가함.
        """
        while self.experience >= 50:
            self.level += 1
            self.attack += 10
            self.defense += 5
            self.speed += 3
            self.experience -= 50
            print(
                f"[{self.name}]이(가) 레벨업 했습니다! 현재 레벨: {self.level}, 공격력: {self.attack}, 방어력: {self.defense}, 스피드: {self.speed}"
            )


class Monster(Character):
    """
    몬스터 캐릭터를 나타내는 클래스.
    """

    def __init__(self, name, level):
        """
        Monster 클래스의 초기화 메서드. 몬스터의 속성을 랜덤하게 설정함.

        Args:
            name (str): 몬스터의 이름.
            level (int): 몬스터의 레벨.
        """
        hp = random.randint(10, 30) * level
        attack = random.randint(5, 20) * level
        defense = random.randint(1, 5) * level
        speed = random.randint(5, 10) * level
        super().__init__(name, level, hp, attack, defense, speed)


def battle(player, monster):
    """
    플레이어와 몬스터 간의 전투를 처리하는 함수.

    전투는 두 캐릭터 중 하나의 체력이 0 이하가 될 때까지 반복됨.
    스피드에 따라 선공자가 결정되며, 전투 결과에 따라 플레이어의 경험치와 레벨이 조정됨.

    Args:
        player (Player): 전투에 참여하는 플레이어 인스턴스.
        monster (Monster): 전투에 참여하는 몬스터 인스턴스.
    """
    print(f"\n===== {player.name} vs {monster.name} =====")

    battle_turn = 0

    # 스피드 비교를 통해 전투 순서 결정
    if player.speed >= monster.speed:
        first_attacker, second_attacker = player, monster
    else:
        first_attacker, second_attacker = monster, player

    # 선공자를 출력
    print(f"\n{first_attacker.name}이(가) 스피드 {first_attacker.speed}로 선공을 잡았습니다!")
    print(f"{second_attacker.name}의 스피드는 {second_attacker.speed}입니다.")

    while player.is_alive() and monster.is_alive():
        battle_turn += 1
        print(f"\n----- {battle_turn}번째 턴 -----")

        # 첫 번째 공격자 공격
        first_attacker.attack_target(second_attacker)

        # 두 번째 공격자가 살아있으면 공격
        if second_attacker.is_alive():
            second_attacker.attack_target(first_attacker)

    # 전투 결과 출력
    if player.is_alive():
        player.gain_experience(monster.level * 20)
        player.level_up()
        print("전투 승리!")
    else:
        print("전투 패배..")


def main():
    """
    게임의 메인 함수를 정의함. 플레이어와 몬스터를 생성하고 전투를 진행함.

    몬스터와의 전투는 순차적으로 진행되며, 플레이어가 사망하면 게임이 종료됨.
    """
    monster_dict = {"슬라임": 1, "고블린": 2, "오크": 3}

    # 플레이어 생성
    player_name = input("플레이어 이름을 입력하세요: ")
    player = Player(player_name)

    # 몬스터와의 전투
    for monster_name, level in monster_dict.items():
        monster = Monster(monster_name, level)
        battle(player, monster)

        if not player.is_alive():
            print("게임오버")
            break


# import 했을 때, main 함수가 자동으로 실행되지 않도록 하는 코드
# 즉, 직접 실행 시에만 main() 실행
if __name__ == "__main__":
    main()
