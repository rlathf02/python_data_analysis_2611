
text = '파이썬'

print(text)
print(len(text))

#문자 변환

print(ord('가')) #문자를 유니코드 숫자로 변환
print(chr(44032)) #숫자를 다시 문자로 변환

# 인코딩 
# Encode : 문자열을 바이트(byte)로 바꾸는 작업
# 파일이나 저장이나 네트워크 전송 시 사용됨

encoded = text.encode('utf-8')
print(encoded)
print(type(encoded))

# decode : 인코딩의 반대과정 / 문자열로 다시 복원하는 과정
decoded = encoded.decode('utf-8')
print(decoded)
print(type(encoded))

# 인코딩이 맞지 않으면 오류 발생 
try:
    wrong = encoded.decode('cp949')
    print(wrong)
except UnicodeDecodeError:
    print('인코딩 방식이 맞지 않아 오류 발생')




