class House:
    def __init__(self, location, house_type, deal_type, price, complection_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.complection_year = complection_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.complection_year)

house = []
h1 = House("강남", "아파트", "매매", "10억", "2010년")
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h3 = House("송파", "빌라", "월세", "500/50", "2000년")
house.append(h1)
house.append(h2)
house.append(h3)

print("총 {}대의 매물이 있습니다.".format(len(house)))
for h in house:
    House.show_detail(h)

