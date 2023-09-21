def calc_sum(start, end) :   #Parameter, 매개변수
    sum = 0
    for i in range(start, end + 1) :
        sum += i

    return sum    #sum을 가지고 복귀
#함수의 끝

start = 50        #실질적인 시작은 여기부터 시작
end = 70
result = calc_sum(start, end)
print("%d부터 %d까지의 합은 %d입니다." % (start, end, result))
   
