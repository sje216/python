# def profile(name, age, main_lan):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name,age,main_lan))
# profile("유재석",25,"자바")
# profile("김태호",45,"C")

# 같은 학교, 같은 반, 같은 나이, 같은 수업
# def profile(name, age=17, main_lan="python"):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name,age,main_lan))
# profile("유재석")
# profile("하하")

# def profile(name, age, main_lan):
#     print(name,age,main_lan)
# profile(name="유재석", age=45, main_lan="python")
# profile(name="김태호", main_lan="java", age=55)

def profile(name, age, *language): # *가변인자입니다,,
    print("이름 : {0}\t나이: {1}\t".format(name,age),end=" ")
    for lang in language:
        print(lang, end=" ")
    print() #줄바꿈을 위해

profile("유재석", 25, "python", "java", "c", "c++", "jvs", "html")
profile("김태호", 30, "kotlin", "swift")