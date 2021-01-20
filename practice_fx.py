from random import *
#일반 유닛
# class Unit:
#     def __init__(self, name, hp): #3가지 갯수만큼은 항상 포함해야함
#         self.name = name
#         self.hp = hp
        # self.damage = damage
        # print("{}유닛이 생성되었습니다.".format(name))
        # print("체력 {0}, 공격력 {1}".format(hp, damage))
#메딕 : 의무병 (공격 x)
# marine1 = Unit("marine", 40, 5)
# marine2 = Unit("marine", 40, 5)
# tank1 = Unit("tank", 150, 35)
# # tank1 = Unit("tank")
#
# #레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("wraith", 80, 5)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))
#
# #마인드 컨트롤 : 상대방 유닛을 내것으로 만드는것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True
#
# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


#일반 유닛
class Unit:
    def __init__(self, name, hp, speed): #3가지 갯수만큼은 항상 포함해야함
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        # print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        self.damage = damage
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): #3가지 갯수만큼은 항상 포함해야함
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        self.location = location
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 :{2}]".format(\
            self.name, location, self.damage)) #self 자기 자신에게 있는 멤버 변수 사용 전달 / location 전달받은 변수 사용

#마린
class marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    #스팀팩 : 일정시간동안 이동 및 공격속도를 증가, 체력을 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. ( HP 10감소 )".format(self.name))
        else:
            print("{0} : 체력이 부족해서 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class tank(AttackUnit):
    # 시즈모드 : 탱크를 지상으로 고정, 더 높은 파워로 공격 가능, 이동 불가
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if tank.seize_developed == False:
            return #시즈모드 개발 안되어있으면 아무것도 안하고 나감

        # 현재 시즈모드가 아닐때 --> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

        # 현재 시즈모드일때 --> 시즈모드 해제


# #파이어뱃 : 공격유닛, 화염방사기
# firebat1 = AttackUnit("firebat", 50, 16)
# firebat1.attack("5시")
# #공격 두번 받음
# firebat1.damaged(25)
# firebat1.damaged(25)

#드랍쉽 : 공중유닛, 수송기 (마린/파이어뱃/탱크 등을 수송 공격 x)
class Flyable:
    def __init__(self, flying_speed):
        self.flyung_speend = flying_speed

    def fly(self, name, location):
        # self.name = name
        # self.location = location
        # print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flyung_speend))
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flyung_speend))

class FlyableAttack(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드 0
        Flyable.__init__(self,flying_speed) #날아다니는 스피드가 있으니깐

    def move(self, location):
        # print("[공중 유닛 이동]")
        self.fly(self.name, location) #Flyable 상속된 fly 여서 self.fly

# 레이스
class wraith(FlyableAttack):
    def __init__(self):
        FlyableAttack.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        # 클로킹 모드 -> 해제
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
         # 해제 -> 클로킹 모드
        else:
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    print("Player : gg")
    print("Player님이 게임에서 퇴장하셨습니다.")

#발키리 : 공중 공격 유닛, 한발에 14발 미사일 발사
# valkyrie = FlyableAttack("valkyrie", 200, 6, 5)
# valkyrie.fly(valkyrie.name,"3시")
# valkyrie.fly("valkyrie","3시")

#벌쳐 : 지상 유닛, 기동성 좋음
# vulture = AttackUnit("vulture", 80, 10, 20)

#배틀 크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battleCrusier = FlyableAttack("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battleCrusier.fly(battleCrusier.name, "9시")
# battleCrusier.move("9시")

#건물
class buildingUnit(Unit):
    def __init__(self, name, hp, location):
        # pass
        # super().__init__(name, hp, 0)
        Unit.__init__(self, name, hp, 0)
        self.location = location

#서플라이 디폿 : 건물 (1개 건물 = 8유닛)
# supply_depot = buildingUnit("서플라이 디폿", 500, "7시")

# 실제 게임 진행
game_start()

#마린 3 생성
m1 = marine()
m2 = marine()
m3 = marine()

#탱크 2 생성
t1 = tank()
t2 = tank()

#레이스 1 생성
w1 = wraith()

#유닛 일괄 관리 ; 관리힘들어서 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

#공격모드준비 (마린 : 스팀팩, 탱크: 시즈모드 , 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, marine):  #지금 만들어진 객체가 어떤 유닛의 객체인지 확인
        unit.stimpack()
    elif isinstance(unit, tank):
        unit.set_seize_mode()   
    elif isinstance(unit, wraith):
        unit.clocking()

#전군공격
for unit in attack_units:
    unit.attack("1시")

#전군피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격은 랜덤으로 받음 (5~20)

#게임종료
game_over()