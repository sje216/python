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

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): #3가지 갯수만큼은 항상 포함해야함
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        self.location = location
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 :{2}]".format(\
            self.name, location, self.damage)) #self 자기 자신에게 있는 멤버 변수 사용 전달 / location 전달받은 변수 사용

    def damaged(self, damage):
        self.damage = damage
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

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
        print("[공중 유닛 이동]")
        self.fly(self.name, location) #Flyable 상속된 fly 여서 self.fly

#발키리 : 공중 공격 유닛, 한발에 14발 미사일 발사
# valkyrie = FlyableAttack("valkyrie", 200, 6, 5)
# valkyrie.fly(valkyrie.name,"3시")
# valkyrie.fly("valkyrie","3시")

#벌쳐 : 지상 유닛, 기동성 좋음
vulture = AttackUnit("vulture", 80, 10, 20)

#배틀 크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battleCrusier = FlyableAttack("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battleCrusier.fly(battleCrusier.name, "9시")
battleCrusier.move("9시")