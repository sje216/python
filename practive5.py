gun = 10
def checkpoint(soldiers):
    # gun = 20 함수내에서의 함수 : 지역함수
    global gun #함수밖에서의 함수를 불러옴 : 전역함수
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun # 바뀐 gun을 외부로 던질수 있음.
print("전체 총 : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))