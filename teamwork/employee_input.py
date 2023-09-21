# 이한재
# 입력 프로그램

def myInput(employee):
    try:
        employeeNumber = int(input("사원번호 : "))
        if not (1 <= employeeNumber < 100):
            raise ValueError("Error: please input an integer between 1 and 99")
        
        gLevel = int(input("급 : "))
        if not (1 <= gLevel < 10):
            raise ValueError("Error: please input an integer between 1 and 9")
        
        hLevel = int(input("호 : "))
        if not (1 <= hLevel < 10):
            raise ValueError("Error: please input an integer between 1 and 9")
        
        bonus = int(input("수당 : "))
        
        employee["employeeNumber"] = employeeNumber
        employee["gLevel"] = gLevel
        employee["hLevel"] = hLevel
        employee["bonus"] = bonus
    
    except ValueError as e:
        print(e)
