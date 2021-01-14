#open(): 파일을 특정한 모드로 여는 함수 (읽을때 r, 쓸 때 w)
#read(): 파일 객체로부터 모든 내용을 읽는 함수
#readline(): 파일 객체로부터 한줄씩 문자열을 읽는 함수
#readlines(): 전체 내용을 한번에 리스트에 담는 함수

# f=open('input.text','r',encoding='UTF-8')
# f.seek(9)
# data = f.read()
# print(data)
# f.close()

# count = 0
# while count<3:
#     data = f.readline()
#     count = count+1
#     print("%d번째 줄: %s" %(count,data), end='')
# f.close()

# list = f.readlines()
# for i,data in enumerate(list):
#     print('%d 번째줄 : %s' %(i+1,data), end='')
# f.close()
# print(list)

# with open('input.text','r', encoding='UTF-8')as f:
#     list = f.readlines()
#     for i, data in enumerate(list):
#         print('%d 번째 줄 : %s'%(i + 1, data), end='')

def process(filename):
    with open(filename, 'r') as f:
        #key = alphabet value = 빈도수
        dict = {}
        data = f.read()
        for i in data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict

dict = process('input.text')
print(dict)
#빈도수를 기준으로 내림차순 정렬 수행
dict = sorted(dict.items(), key=lambda a:a[1], reverse=True)
for data, count in dict:
    if data =='\n' or data == ' ':
        continue
    print('%d 번 출현 : %s'%(count,data))