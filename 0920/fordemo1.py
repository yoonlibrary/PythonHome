#for i in range(65, 91) :           #ASCII 코드 65=대문자 A, 90=대문자 Z
#    print(chr(i), end = '\t')      #chr(숫자)=숫자에 해당하는 문자로 바꿔줌
#print()

#for i in range(97, 123) :           #ASCII 코드 97=소문자 a, 122=소문자 Z
#    print(chr(i), end = '\t')      #chr(숫자)=숫자에 해당하는 문자로 바꿔줌
#print()

count, line = 0, 1               # line 추가
for i in range(65, 91) :
    if line % 2 == 1 : print(chr(i), end = '\t')      # line이 홀수라면 대문자를 찍기
    else : print(chr(i + 32), end = '\t')             # line이 짝수라면 소문자를 찍기
    count += 1
    if count % 5 == 0 :
        print()
        line += 1
print()