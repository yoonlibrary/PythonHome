# 양재준
# 계산 프로그램

def calc(employee) :
    #급, 호봉에 따라 급여 수당 declare
    if employee["gLevel"]==1 and employee["hLevel"]==1 : 
        money = 95000
    elif employee["gLevel"]==1 and employee["hLevel"]==2 : 
        money = 92000
    elif employee["gLevel"]==1 and employee["hLevel"]==3 : 
        money = 89000
    elif employee["gLevel"]==1 and employee["hLevel"]==4 : 
        money = 86000
    elif employee["gLevel"]==1 and employee["hLevel"]==5 : 
        money = 83000
    elif employee["gLevel"]==2 and employee["hLevel"]==1 : 
        money = 80000
    elif employee["gLevel"]==2 and employee["hLevel"]==2 : 
        money = 75000
    elif employee["gLevel"]==2 and employee["hLevel"]==3 : 
        money = 70000
    elif employee["gLevel"]==2 and employee["hLevel"]==4 : 
        money = 65000
    else : 
        money = 60000

    #지급액 = 급여 + 수당
    gMoney = money + employee["bonus"]

    if gMoney < 70000 : 
        taxRate = 0
        jMoney = 0
    elif 70000 <= gMoney <= 79999 : 
        taxRate = 0.005
        jMoney = 300
    elif 80000 <= gMoney <= 89999 : 
        taxRate = 0.007
        jMoney = 500
    else : 
        taxRate = 0.012
        jMoney = 1000
    # #세금 = (지급액 * 세율) - 조정액
    tax = gMoney * taxRate - jMoney


    # #차인지급액 = 지급액 - 세금
    cMoney = gMoney - tax

    employee["gMoney"] = gMoney
    employee["tax"] = int(tax)
    employee["cMoney"] = int(cMoney)


    


