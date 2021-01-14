# score_file = open("score.txt", "w", encoding="utf8") #w 읽기 쓰기
# print("영어 : 100", file=score_file)
# print("수학 : 60", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") #a 원래 있던 파일에 이어쓰기
# score_file.write("과학 : 70")
# score_file.write("\n국어 : 80") #write 는 줄바꿈 x
# score_file.close()

#파일 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) # 모든 내용 다 읽기
# print(score_file.readline(), end="") # 한 줄씩 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 한 줄씩 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 한 줄씩 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 한 줄씩 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()

# 몇 줄인지 모를경우(1)
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 몇 줄인지 모를경우(2)
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()