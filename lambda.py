#lambda 람다식: 함수의 형태를 더욱 짧게 쓸 수 있도록 해주는 문법
#map(): 다수의 원소에 대한 함수의 결과를 한번에 얻을 수 있게 도와줌
# add = lambda x,y: x+y
# print(add(1,3))
list1 = [1,2,3,4]
list2 = [5,6,7,8]
add_list = lambda a,b: a+b
# result = list(map(add_list, list1, list2))
# print(result)
result = map(add_list, list1, list2)
print(list(result))