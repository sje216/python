# print("나는 %d 살 입니다." %20)
# print("나는 %s 를 좋아해요." %"python")
# print("apple은 %c로 시작함." %"a")
# print("나는 %s 와 %s 를 좋아해요." %("파란색","빨간색"))
# print("나는 {}살 입니다.".format(20))
# print("나는 {1} 와 {0} 를 좋아해요.".format(20,40))
# print("나는 {age} 이며 {color} 를 좋아해요.".format(age = 20, color = "red"))

# age = 20
# color = "red"
# print(f"나는 {age} 이며 {color} 를 좋아해요.")

print("RED Apple\rPine")
print("redd\bApple")

url = "http://www.naver.com"
ex1 = url.replace("http://www.", "")
print(ex1)
# ex2 = ex1.replace(".com","")
ex1 = ex1[:ex1.index(".")]
print(ex1)
password = ex1[:3] + str(len(ex1)) + str(ex1.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url,password))