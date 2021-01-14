#표준 입출력
# print("python","java", sep=",", end="? ")
# print("무엇이 더 재미있을까요?")

# import sys
# print("python","java", file=sys.stdout) #표준 출력으로 처리
# print("python","java", file=sys.stderr) #표준에러로 처리

#시험 성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8),str(score).rjust(4), sep=":") #ljust(n) : 왼쪽으로 정렬을 하는데 8칸만큼 확보,str 정수값이니깐 붙임

#은행 대기 순번표
#001,002,003,...
# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3)) #zfill : 0으로 n만큼 채움

# answer = input("아무 값이나 입력하세요 : ") #input 으로 값을 받으면 항상 str으로 받음
# print(type(answer))
# print("입력한 값은 "+answer+" 입니다.")

#빈자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 확보
print("{0: >10}".format(500)) # 빈공간 > 오른쪽 정렬 10 총 열자리 공간 확보하면서 500출력

#양수일때, +, 음수일때,- 표시
print("{0: >+10}".format(500)) #  >+: 양수일땐 + 음수일땐 -로 표시됨
print("{0: >+10}".format(-500))

#왼쪽 정렬, 빈칸 밑줄
print("{0:_<+10}".format(500))
#세자리 마다 콤마 찍기
print("{0:,}".format(123456789))
#세자리 마다 콤마 찍기, +-부호 붙이기
print("{0:+,}".format(123456789))
print("{0:+,}".format(-123456789))
#세자리 마다 콤마 찍기, +-부호 붙이기, 자릿수 확보, 빈자리 ^ 로 대체
print("{0:^<+15,}".format(123456789))
#소숫점 출력
print("{0:f}".format(5/3))
#소숫점 특정자리까지 출력 (소숫점 3째자리에서 반올림)
print("{0:.2f}".format(5/3))