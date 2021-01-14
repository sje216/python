# q) 매주 1회 보고서 작성
# -보고서 형태
# - x 주차 주간보고 -
#  부서 :
#  이름 :
#  업무 요약:
# 1-15 주차 까지
# 파일명은 1주차.txt

# with open("1주차.txt", "w", encoding="utf8") as week_file:
#     week_file.write('''
#      - 1 주차 주간보고 -
#       부서 :
#       이름 :
#       업무 요약:
#       ''')


for i in range(1,16):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as week_file:
        week_file.write('''
         - '''+str(i)+''' 주차 주간보고 -
          부서 :
          이름 :
          업무 요약:
          ''')

for i in range(1,16):
    with open(str(i)+"주차.txt", "r", encoding="utf8") as week_file:
        print(week_file.read(), end="")