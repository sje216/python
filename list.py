#index(): 리스트 내 특정한 원소의 인덱스를 찾기
# list=['신지은','곽소영', '조다흰', '변지은']
# print(list.index('신지은'))

# reverse(): 리스트의 원소 뒤집기
# list = [1,2,3]
# list.reverse()
# print(list)
# print(list[::-1])
# list = list[::-1]
# print(list)

#sum(리스트 자료형): 리스트의 모든 원소 합
# list = [1,2,3,4]
# print(sum(list))

#range(시작,끝(-1)): 특정 범위 지정
#list(특정범위): 특정 범위의 원소를 가지는 리스트를 반환
# my_range = range(5,10)
# list = list(my_range)
# print(list)

#all()/any(): 리스트의 모든원소가 참인지 판별/ 하나라도 참인지 판별
# list = [True,False,True]
# print(all(list))
# print(any(list))

#enumalate(): 리스트의 인덱스와 원소를 함께 추출
# my_list=['신지은','곽소영', '조다흰', '변지은']
# result = list(enumerate(my_list))
# print(result)
# for i,k in enumerate(my_list):
    # print("인덱스:",i,"원소:",k)

#sort(): 리스트의 원소를 정렬
# my_list=['신지은','곽소영', '조다흰', '변지은']
# print(sorted(my_list))
# my_list.sort()
# print(my_list)

#count(): 특정한 원소의 개수를 추출
# my_list=['신지은','곽소영', '신지은', '변지은']
# print(my_list.count('신지은'))

#del(): 리스트의 특정 원소 제거/insert(): 원소 삽입
# my_list=['신지은','곽소영', '신지은', '변지은']
# del my_list[0:3]
# my_list.insert(0,'박지훈')
# my_list.append('박지훈')
# print(my_list)