# try:
#     print(3/2)
# except:
#     print('0으로는 나눌수 없습니다.')
# else:
#     print('예외없이 성공적으로 실행되었습니다.')
# finally:
#     print('예외처리를 마칩니다.')


try:
    print(3/0)
except Exception as e:
    print(e)