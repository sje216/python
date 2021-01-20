class soldOutError(Exception):
    pass

chicken = 10
wating = 1
while(True):
    try:
        print("남은 치킨 : {0}".format(chicken))
        order = int(input("치킨 몇마리 주문 하시겠습니까? "))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문 완료되었습니다.".format(wating, order))
            wating += 1
            chicken -= order

        if chicken == 0:
            raise soldOutError
    except ValueError as err:
        print("잘못된 값을 입력하셨습니다.")
    except soldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break