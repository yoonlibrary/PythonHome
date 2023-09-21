import copy            #copy라는 라이브러리 땡겨옴



original = [1,2,3]
target = copy.deepcopy(original)      #mutable type을 immutable type으로 만드는 명령어 deepcopy
print(original, target)
original[0] = 10000
print(original, target)