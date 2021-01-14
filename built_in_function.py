#내장함수

# user_input = input('정수를 입력하시오: ')
# print('제곱:',int(user_input) ** 2)

# a = '12345'
# print(int(a))
# b = 12.5
# print(int(b))
# a = 10
# print(float(a))

# list=[4,5,7,2,6,9,1,8]
# print(max(list))
# print(min(list))

#bin() - 10진수 -> 2진수로 변환,hex() - 10진수 ->16진수로 변환
# print(bin(12))
# print(hex(12))
# print(int('0xc',16))
# print(int('0b1100',2))

#round() 반올림
# print(round(123.567))
# print(round(123.567,2))
# print(round(123.567,-1))

#type() 자료형의 종류
# int = 1
# str = '문자열'
# list = [1,2,3,4]
# dict = {'apple':'사과'}
# print(type(int))
# print(type(str))
# print(type(list))
# print(type(dict))

#문자열 자료형 뒤집기 : 슬라이싱 활용
# str = 'Hello world'
# print(str[::-1])
# print(len(str))

#isalpha(): 특정한 문자열이 문자로만 이루어졌는지 확인 <-> isdigit() : 숫자로만
#isalnum(): 특정 문자+숫자
#join(): 문자열 합칠때
# str = 'Hello world'
# str = 'Helloworld'
# str = '하늘'
# print(str.isalpha())
# str = '12345'
# print(str.isdigit())
# str = '1234A'
# print(str.isalnum())
# list = ['hello', 'world', '홍길동']
# print('-'.join(list))
# print(','.join(list))

#문자열 정렬 sorted()
# str = 'helloworld'
# list = sorted(str)
# print(list)
# print('-'.join(list))
# list = sorted(str,reverse=True)
# print(''.join(list))

#split() : 문자열 분리
# str = 'i wanna watch a movie.'
# list = str.split(' ')
# print(list)

# find() : 문자열 찾기
# str = 'i like you'
# print(str.find('like'))
# str = 'i like like you'
# print(str.find('like'))
# print(str.find('like',5))
# print(str.find('love'))

#upper(),lower(): 대문자 소문자
# str = 'hello world'
# print(str.upper())
# print(str.lower())

#strip(): 좌우로 특정한 문자열 제거 (벗겨내다)
# str = '  hello wolrd  '
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())
# str = 'ahello wolrda'
# print(str.rstrip(a))

#eval(): 문자열 수식 계산
exp = "(20345+3495)*10-(30/6)"
print(eval(exp))