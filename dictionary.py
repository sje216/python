# dict={}
# dict['안녕'] = 'Hello'
# dict['기적'] = 'Miracle'
# dict['노력'] = 'effort'
# dict['안녕'] = 'Hi'
# del dict['기적']
# print(dict)
# # dict.clear()
# for i,k in enumerate(dict):
#     print("[인덱스:",i, "] 한글:",k, "/ 영어:", dict[k])
# print('사전 자료형 길이',len(dict))
# keys = dict.keys()
# key_list = list(keys)
# value = dict.values()
# value_list = list(value)
# print(value_list)
# print(keys)
# print(key_list)

# if '노력' in dict:
#     print("[노력] 존재")

scores = {}
scores['sje'] = 100
scores['sde'] = 90
print(sorted(scores))
print(sorted(scores, reverse=True))
print(sorted(scores.values()))


dict = {}
dict["하늘"] = 'sky'
dict["언덕"] = 'hill'
dict["파란색"] = 'blue'
print(len(dict))
print(dict)
keys = dict.keys()
print(keys)
values = dict.values()
value_list = list(values)
print(value_list)