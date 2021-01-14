#class: 반복되는 불필요한 소스코드를 최소화하면서 현실세계의 사물을 컴퓨터 프로그래밍상에서 쉽게 표현할 수 있도록 해주는 프로그래밍 기술
class Car:
    def __init__(self, name, color):
        self.name=name
        self.color=color
    def __del__(self):
        print("인스턴스를 소멸시킴")
    def show_info(self):
        print("이름:",self.name, "색상:",self.color)
    def set_name(self,name):
        self.name = name

# car1 = Car("소나타","빨간색")
# car1.set_name("아반떼")
# # print(car1.name,"을 구매함")
# # car1.show_info()
# del car1
# car1.show_info()

class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name, "이(가) 공격을 수행합니다. [전투력: ",self.power, "]")

class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
    def show_info(self):
        print("몬스터 이름:",self.name,"/몬스터 종류:",self.type)
monster = Monster("슬라임", 2, "초급")
monster.attack()
monster.show_info()

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def show_inf0(self):
        print("이름:",self.name,"색상:",self.color)
car1= Car("소나타","하양색")
car1.show_inf0()
class Samsung(Car):
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
samsung1 =Samsung("소나타", "검정색", "중간크기")
samsung1.show_inf0()